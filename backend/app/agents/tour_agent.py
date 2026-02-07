"""
Tour Agent
==========
The main LangChain agent that orchestrates:
  1. Understanding the user request
  2. Fetching POI data from ArcGIS
  3. Optimizing the route
  4. Generating a rich narrative for each stop
"""

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage

from app.config import settings
from app.services.arcgis_service import ArcGISService
from app.services.route_service import RouteService
from app.services.poi_service import POIService


SYSTEM_PROMPT = """\
You are GeoExplore-AI, an expert tour guide and travel planner.
You create personalized walking/driving tours for cities using real
geographic data.  For every stop you suggest, provide:
  • Name & address
  • A 2-3 sentence narrative with a fun historical or cultural fact
  • Estimated time to spend there

Always consider the user's preferences (interests, time constraints,
accessibility needs).  Be enthusiastic but concise.
"""


class TourAgent:
    """High-level agent that chains together the LangChain pipeline."""

    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.7,
            api_key=settings.OPENAI_API_KEY,
        )
        self.arcgis = ArcGISService()
        self.route_service = RouteService()
        self.poi_service = POIService()

    async def run(
        self,
        message: str,
        city: str = "nyc",
        preferences: dict | None = None,
    ) -> dict:
        """
        Full pipeline:
        user message → intent parsing → POI retrieval → route optimisation → narrative
        """

        # Step 1  — Understand intent & extract parameters
        intent = await self._parse_intent(message, city, preferences)

        # Step 2  — Retrieve relevant POIs from ArcGIS
        pois = await self.poi_service.search(
            city=city,
            categories=intent.get("categories", ["landmarks"]),
            limit=intent.get("num_stops", 5),
        )

        # Step 3  — Build an optimised route
        route = await self.route_service.optimise(pois)

        # Step 4  — Generate the narrative response
        narrative = await self._generate_narrative(
            pois=pois,
            route=route,
            preferences=preferences,
        )

        return {
            "reply": narrative,
            "tour": {
                "stops": pois,
                "route": route,
                "category": intent.get("tour_type", "general"),
            },
            "map_data": {
                "center": route.get("center") if route else None,
                "waypoints": [p.get("location") for p in pois],
            },
        }

    # ── Private helpers ──────────────────────────────────────────────

    async def _parse_intent(
        self, message: str, city: str, preferences: dict | None
    ) -> dict:
        """Use the LLM to extract structured intent from the user message."""
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "Extract the tour intent from the user message. "
                 "Return JSON with keys: tour_type, categories (list), "
                 "num_stops (int), time_budget_min (int or null)."),
                ("human", "{message}\nCity: {city}\nPreferences: {preferences}"),
            ]
        )
        chain = prompt | self.llm
        result = await chain.ainvoke(
            {"message": message, "city": city, "preferences": str(preferences)}
        )
        # TODO: parse the JSON from the LLM response
        return {
            "tour_type": "general",
            "categories": ["landmarks"],
            "num_stops": 5,
        }

    async def _generate_narrative(
        self, pois: list, route: dict | None, preferences: dict | None
    ) -> str:
        """Generate a rich, engaging tour narrative from the POI list."""
        stops_text = "\n".join(
            f"- {p.get('name', 'Unknown')} ({p.get('category', '')})"
            for p in pois
        )
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=(
                    f"Create an engaging tour narrative for these stops:\n"
                    f"{stops_text}\n\n"
                    f"User preferences: {preferences}"
                )
            ),
        ]
        response = await self.llm.ainvoke(messages)
        return response.content
