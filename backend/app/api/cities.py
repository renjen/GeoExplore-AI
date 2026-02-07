"""
Cities endpoint  —  list supported cities & their metadata.
"""

from fastapi import APIRouter

from app.data.cities import SUPPORTED_CITIES

router = APIRouter()


@router.get("/")
async def list_cities():
    """Return all supported cities."""
    return SUPPORTED_CITIES


@router.get("/{city_id}")
async def get_city(city_id: str):
    """Return metadata for a specific city."""
    city = SUPPORTED_CITIES.get(city_id)
    if city:
        return city
    return {"error": "City not found"}
