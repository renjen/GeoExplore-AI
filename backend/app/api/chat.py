"""
Chat endpoint  —  main conversational interface.
Receives a user message → runs the LangChain agent → returns response.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.tour_agent import TourAgent

router = APIRouter()


# ── Request / Response Schemas ───────────────────────────────────────
class ChatRequest(BaseModel):
    message: str
    city: str = "nyc"
    preferences: dict | None = None


class ChatResponse(BaseModel):
    reply: str
    tour: dict | None = None
    map_data: dict | None = None


# ── Endpoint ─────────────────────────────────────────────────────────
@router.post("/", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """Process a user chat message through the tour-generation agent."""
    agent = TourAgent()
    result = await agent.run(
        message=req.message,
        city=req.city,
        preferences=req.preferences,
    )
    return ChatResponse(
        reply=result.get("reply", ""),
        tour=result.get("tour"),
        map_data=result.get("map_data"),
    )
