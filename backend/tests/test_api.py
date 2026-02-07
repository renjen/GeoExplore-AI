"""
Backend tests.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "healthy"


def test_list_cities():
    resp = client.get("/api/cities/")
    assert resp.status_code == 200
    data = resp.json()
    assert "nyc" in data


def test_get_city():
    resp = client.get("/api/cities/nyc")
    assert resp.status_code == 200
    assert resp.json()["name"] == "New York City"


def test_list_tour_templates():
    resp = client.get("/api/tours/templates")
    assert resp.status_code == 200
    assert len(resp.json()) > 0


def test_get_tour_template():
    resp = client.get("/api/tours/templates/nyc-historic")
    assert resp.status_code == 200
    assert resp.json()["city"] == "nyc"
