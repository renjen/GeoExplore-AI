"""
Route Service
=============
Builds optimised routes between POI stops using the Esri Routing API.
"""

import httpx
from app.config import settings

ARCGIS_ROUTE_URL = (
    "https://route-api.arcgis.com/arcgis/rest/services/"
    "World/Route/NAServer/Route_World/solve"
)


class RouteService:
    """Async route-optimisation via ArcGIS Routing."""

    def __init__(self):
        self.api_key = settings.ARCGIS_API_KEY
        self._client = httpx.AsyncClient(timeout=30)

    async def optimise(self, pois: list[dict]) -> dict | None:
        """
        Given a list of POI dicts (each with 'location': {lat, lng}),
        call the Esri Routing API and return the optimised route.
        """
        if len(pois) < 2:
            return self._fallback_route(pois)

        stops = ";".join(
            f"{p['location']['lng']},{p['location']['lat']}" for p in pois
        )

        params = {
            "f": "json",
            "token": self.api_key,
            "stops": stops,
            "findBestSequence": "true",
            "returnDirections": "true",
            "returnRoutes": "true",
            "directionsLanguage": "en",
        }

        try:
            resp = await self._client.get(ARCGIS_ROUTE_URL, params=params)
            data = resp.json()
            routes = data.get("routes", {}).get("features", [])
            directions = data.get("directions", [])

            if routes:
                attrs = routes[0].get("attributes", {})
                return {
                    "total_distance_miles": round(attrs.get("Total_Miles", 0), 2),
                    "total_time_min": round(attrs.get("Total_TravelTime", 0), 1),
                    "directions": self._parse_directions(directions),
                    "center": self._compute_center(pois),
                    "geometry": routes[0].get("geometry"),
                }
        except Exception as e:
            print(f"⚠️  Route API error: {e}")

        return self._fallback_route(pois)

    # ── Helpers ──────────────────────────────────────────────────────

    @staticmethod
    def _parse_directions(directions: list) -> list[str]:
        steps: list[str] = []
        for group in directions:
            for feat in group.get("features", []):
                text = feat.get("attributes", {}).get("text")
                if text:
                    steps.append(text)
        return steps

    @staticmethod
    def _compute_center(pois: list[dict]) -> dict:
        lats = [p["location"]["lat"] for p in pois]
        lngs = [p["location"]["lng"] for p in pois]
        return {
            "lat": sum(lats) / len(lats),
            "lng": sum(lngs) / len(lngs),
        }

    @staticmethod
    def _fallback_route(pois: list[dict]) -> dict:
        """Return a basic route object when the API isn't available."""
        if not pois:
            return {"total_distance_miles": 0, "total_time_min": 0, "directions": [], "center": None}
        center = RouteService._compute_center(pois)
        return {
            "total_distance_miles": 0,
            "total_time_min": 0,
            "directions": ["Route calculation requires an ArcGIS API key."],
            "center": center,
        }

    async def close(self):
        await self._client.aclose()
