"""
Supported Cities
================
Metadata for every city GeoExplore-AI supports.
Add new cities here to expand coverage.
"""

SUPPORTED_CITIES: dict[str, dict] = {
    "nyc": {
        "id": "nyc",
        "name": "New York City",
        "state": "New York",
        "country": "US",
        "center": {"lat": 40.7128, "lng": -74.0060},
        "zoom": 12,
        "bounds": {
            "north": 40.92,
            "south": 40.49,
            "east": -73.70,
            "west": -74.26,
        },
        "description": "The city that never sleeps — unmatched culture, food, and history.",
        "highlights": ["Statue of Liberty", "Central Park", "Times Square", "Brooklyn Bridge"],
    },
    "sf": {
        "id": "sf",
        "name": "San Francisco",
        "state": "California",
        "country": "US",
        "center": {"lat": 37.7749, "lng": -122.4194},
        "zoom": 12,
        "bounds": {
            "north": 37.83,
            "south": 37.70,
            "east": -122.35,
            "west": -122.52,
        },
        "description": "Hills, fog, the Golden Gate, and a legendary food scene.",
        "highlights": ["Golden Gate Bridge", "Alcatraz", "Fisherman's Wharf", "Chinatown"],
    },
    "boston": {
        "id": "boston",
        "name": "Boston",
        "state": "Massachusetts",
        "country": "US",
        "center": {"lat": 42.3601, "lng": -71.0589},
        "zoom": 13,
        "bounds": {
            "north": 42.40,
            "south": 42.30,
            "east": -70.99,
            "west": -71.13,
        },
        "description": "Where American history began — cobblestone streets and world-class universities.",
        "highlights": ["Freedom Trail", "Fenway Park", "Harvard Square", "Boston Common"],
    },
}
