from fastapi import FastAPI, HTTPException

app = FastAPI(title="Location Service")

CITIES = {
    "bucharest": {"city": "Bucharest", "lat": 44.4268, "lon": 26.1025},
    "london": {"city": "London", "lat": 51.5074, "lon": -0.1278},
    "paris": {"city": "Paris", "lat": 48.8566, "lon": 2.3522},
}


@app.get("/health")
def health():
    return {"status": "ok", "service": "location_service"}


@app.get("/locations/resolve")
def resolve_city(city: str):
    """
    Resolve a city name to coordinates.
    Example: /locations/resolve?city=Bucharest
    """
    key = city.strip()
    if key not in CITIES:
        raise HTTPException(status_code=404, detail="City not supported")

    return CITIES[key]
