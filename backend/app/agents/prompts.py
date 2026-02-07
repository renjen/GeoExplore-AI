"""
Prompt templates used across the agent pipeline.
Centralised here so they're easy to iterate on.
"""

TOUR_SYSTEM_PROMPT = """\
You are GeoExplore-AI, an expert AI tour guide.  You have deep knowledge of
history, architecture, food culture, and nature for major cities.

When creating a tour you MUST:
1. Pick real, existing locations (use the POI data provided).
2. Provide a 2-3 sentence narrative for each stop with an interesting fact.
3. Suggest a logical walking/driving order to minimise travel time.
4. Respect the user's time budget and accessibility needs.
5. Be enthusiastic, concise, and culturally sensitive.
"""

INTENT_EXTRACTION_PROMPT = """\
Analyse the following user message and extract a structured tour request.

User message: {message}
City: {city}
Preferences: {preferences}

Return ONLY valid JSON:
{{
  "tour_type": "<historic|foodie|nature|architecture|general>",
  "categories": ["<category1>", "<category2>"],
  "num_stops": <int>,
  "time_budget_min": <int or null>,
  "accessibility": "<string or null>",
  "transport_mode": "<walking|driving|transit>"
}}
"""

NARRATIVE_PROMPT = """\
Create an engaging, personal tour narrative for the following stops.

Stops:
{stops}

User preferences: {preferences}

For each stop include:
- Name & address
- A fun 2-3 sentence narrative
- Estimated time to spend

End with a summary of total distance and estimated duration.
"""
