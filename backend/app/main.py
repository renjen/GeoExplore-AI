"""
GeoExplore-AI  —  Application Entry Point
==========================================
Run with:  uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api import chat, tours, cities, health

app = FastAPI(
    title="GeoExplore-AI",
    description="AI-powered geographic tour generation using LangChain & ArcGIS",
    version="0.1.0",
)

# ── CORS (allow the React frontend) ──────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ──────────────────────────────────────────────────────────
app.include_router(health.router, tags=["health"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(tours.router, prefix="/api/tours", tags=["tours"])
app.include_router(cities.router, prefix="/api/cities", tags=["cities"])


@app.on_event("startup")
async def startup_event():
    print("🌍 GeoExplore-AI backend starting up …")


@app.on_event("shutdown")
async def shutdown_event():
    print("👋 GeoExplore-AI backend shutting down …")
