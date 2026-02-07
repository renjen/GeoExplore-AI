"""
Tour Templates
===============
Pre-defined tour archetypes that users can pick from or that
the AI agent uses as starting points.
"""

TOUR_TEMPLATES = [
    # ── NYC ──────────────────────────────────────────────────────
    {
        "id": "nyc-historic",
        "name": "Historic Manhattan Walk",
        "city": "nyc",
        "category": "historic",
        "description": "Walk through 400 years of history from Lower Manhattan to Central Park.",
        "estimated_duration_min": 180,
        "default_stops": [
            "Statue of Liberty Ferry Terminal",
            "Federal Hall",
            "Trinity Church",
            "9/11 Memorial",
            "Brooklyn Bridge",
        ],
    },
    {
        "id": "nyc-foodie",
        "name": "NYC Food Crawl",
        "city": "nyc",
        "category": "foodie",
        "description": "Taste your way through the world's most diverse food city.",
        "estimated_duration_min": 150,
        "default_stops": [
            "Katz's Delicatessen",
            "Di Fara Pizza",
            "Chinatown (Mott Street)",
            "Eataly NYC Flatiron",
            "Levain Bakery",
        ],
    },
    {
        "id": "nyc-architecture",
        "name": "NYC Iconic Architecture",
        "city": "nyc",
        "category": "architecture",
        "description": "Marvel at the skyscrapers and architectural gems that define the NYC skyline.",
        "estimated_duration_min": 160,
        "default_stops": [
            "Empire State Building",
            "Chrysler Building",
            "Flatiron Building",
            "One World Trade Center",
            "The Vessel at Hudson Yards",
        ],
    },
    # ── San Francisco ────────────────────────────────────────────
    {
        "id": "sf-nature",
        "name": "SF Parks & Nature",
        "city": "sf",
        "category": "nature",
        "description": "Explore San Francisco's stunning natural beauty from coast to forest.",
        "estimated_duration_min": 200,
        "default_stops": [
            "Golden Gate Park",
            "Lands End Trail",
            "Presidio of San Francisco",
            "Twin Peaks",
            "Muir Woods (nearby)",
        ],
    },
    {
        "id": "sf-historic",
        "name": "SF Gold Rush History",
        "city": "sf",
        "category": "historic",
        "description": "Trace San Francisco's history from the Gold Rush to the tech boom.",
        "estimated_duration_min": 170,
        "default_stops": [
            "Alcatraz Island Ferry",
            "Fisherman's Wharf",
            "Chinatown Gate",
            "Cable Car Museum",
            "Mission Dolores",
        ],
    },
    # ── Boston ───────────────────────────────────────────────────
    {
        "id": "boston-freedom",
        "name": "Freedom Trail & Beyond",
        "city": "boston",
        "category": "historic",
        "description": "Walk the Freedom Trail and discover the birthplace of American independence.",
        "estimated_duration_min": 180,
        "default_stops": [
            "Boston Common",
            "Massachusetts State House",
            "Old North Church",
            "Paul Revere House",
            "Faneuil Hall",
        ],
    },
]
