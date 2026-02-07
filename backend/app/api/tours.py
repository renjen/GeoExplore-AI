"""
Tours endpoint  —  CRUD-style access to pre-built & generated tours.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.tour_templates import TOUR_TEMPLATES

router = APIRouter()


class TourSummary(BaseModel):
    id: str
    name: str
    category: str
    description: str
    estimated_duration_min: int
    city: str


@router.get("/templates", response_model=list[TourSummary])
async def list_templates(city: str | None = None):
    """Return available tour templates, optionally filtered by city."""
    templates = TOUR_TEMPLATES
    if city:
        templates = [t for t in templates if t["city"] == city]
    return templates


@router.get("/templates/{tour_id}")
async def get_template(tour_id: str):
    """Return full detail for a single tour template."""
    for t in TOUR_TEMPLATES:
        if t["id"] == tour_id:
            return t
    return {"error": "Tour not found"}
