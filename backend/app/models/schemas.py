"""
Pydantic schemas shared across the app.
"""

from pydantic import BaseModel


class Location(BaseModel):
    lat: float
    lng: float


class POI(BaseModel):
    name: str
    category: str
    location: Location
    address: str = ""
    description: str = ""
    rating: float | None = None
    image_url: str | None = None


class TourStop(BaseModel):
    order: int
    poi: POI
    narrative: str = ""
    duration_min: int = 15


class Tour(BaseModel):
    id: str
    name: str
    city: str
    category: str
    stops: list[TourStop]
    total_distance_miles: float = 0
    total_time_min: float = 0


class ChatMessage(BaseModel):
    role: str  # "user" | "assistant"
    content: str
    tour: Tour | None = None
