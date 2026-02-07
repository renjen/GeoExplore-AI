"""
ArcGIS Service
==============
Low-level wrapper around the ArcGIS REST API for geocoding,
feature queries, and basemap access.
"""

import httpx
from app.config import settings


ARCGIS_GEOCODE_URL = "https://geocode-api.arcgis.com/arcgis/rest/services/World/GeocodeServer"
ARCGIS_FEATURE_URL = "https://services.arcgis.com"


class ArcGISService:
    """Thin async client for ArcGIS location services."""

    def __init__(self):
        self.api_key = settings.ARCGIS_API_KEY
        self._client = httpx.AsyncClient(timeout=30)

    # ── Geocoding ────────────────────────────────────────────────────

    async def geocode(self, address: str) -> dict | None:
        """Forward-geocode an address → {lat, lng, label}."""
        params = {
            "f": "json",
            "singleLine": address,
            "token": self.api_key,
            "maxLocations": 1,
        }
        resp = await self._client.get(
            f"{ARCGIS_GEOCODE_URL}/findAddressCandidates", params=params
        )
        data = resp.json()
        candidates = data.get("candidates", [])
        if not candidates:
            return None
        best = candidates[0]
        return {
            "lat": best["location"]["y"],
            "lng": best["location"]["x"],
            "label": best["address"],
            "score": best["score"],
        }

    async def reverse_geocode(self, lat: float, lng: float) -> str | None:
        """Reverse-geocode lat/lng → address string."""
        params = {
            "f": "json",
            "location": f"{lng},{lat}",
            "token": self.api_key,
        }
        resp = await self._client.get(
            f"{ARCGIS_GEOCODE_URL}/reverseGeocode", params=params
        )
        data = resp.json()
        return data.get("address", {}).get("LongLabel")

    # ── Feature Queries ──────────────────────────────────────────────

    async def query_features(
        self, service_url: str, where: str = "1=1", out_fields: str = "*", limit: int = 50
    ) -> list[dict]:
        """Query an ArcGIS Feature Service and return records."""
        params = {
            "f": "json",
            "where": where,
            "outFields": out_fields,
            "resultRecordCount": limit,
            "token": self.api_key,
        }
        resp = await self._client.get(f"{service_url}/query", params=params)
        data = resp.json()
        return data.get("features", [])

    async def close(self):
        await self._client.aclose()
