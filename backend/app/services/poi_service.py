"""
POI Service
===========
Fetches and normalises Points of Interest from ArcGIS and
supplementary open-data sources.
"""

from app.services.arcgis_service import ArcGISService
from app.data.cities import SUPPORTED_CITIES

# ArcGIS category mapping
CATEGORY_MAP = {
    "landmarks": "Landmarks and Monuments",
    "museums": "Museums",
    "restaurants": "Restaurants",
    "parks": "Parks and Gardens",
    "historical": "Historic Sites",
    "architecture": "Architecture",
    "nightlife": "Nightlife",
    "shopping": "Shopping",
}


class POIService:
    """Retrieve and normalise POI data for a given city."""

    def __init__(self):
        self.arcgis = ArcGISService()

    async def search(
        self,
        city: str,
        categories: list[str] | None = None,
        limit: int = 10,
    ) -> list[dict]:
        """
        Search for POIs in *city* matching the given categories.
        Returns a list of normalised POI dicts.
        """
        city_meta = SUPPORTED_CITIES.get(city)
        if not city_meta:
            return []

        categories = categories or ["landmarks"]
        results: list[dict] = []

        for cat in categories:
            arcgis_cat = CATEGORY_MAP.get(cat, cat)
            # TODO: replace with real ArcGIS Places API / Feature Service call
            # For now return placeholder data so the pipeline runs end-to-end
            results.extend(
                self._placeholder_pois(city_meta, arcgis_cat, limit)
            )

        return results[:limit]

    # ── Placeholder until real API is wired ──────────────────────────

    @staticmethod
    def _placeholder_pois(city_meta: dict, category: str, limit: int) -> list[dict]:
        """Return stub POIs so the rest of the stack can be developed."""
        center = city_meta["center"]
        return [
            {
                "name": f"Sample {category} #{i+1}",
                "category": category,
                "location": {"lat": center["lat"] + i * 0.002, "lng": center["lng"] + i * 0.002},
                "address": f"{100 + i} Main St, {city_meta['name']}",
                "description": f"A wonderful {category.lower()} worth visiting.",
            }
            for i in range(min(limit, 3))
        ]
