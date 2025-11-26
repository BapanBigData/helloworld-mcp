import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
from mcp.server.fastmcp import FastMCP
from src.config import Config

mcp = FastMCP("Weather-mcp")


@mcp.tool()
def get_weather(location: str) -> str:
    """
    Retrieves the real current weather for a specified location.

    Args:
        location: City name, 'city,country', or ZIP code.
    """

    api_key = Config.OPENWEATHER_API_KEY

    if not api_key:
        return "Missing OPENWEATHER_API_KEY environment variable."

    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Decide if it's a ZIP code or city
    if location.replace(" ", "").isdigit():
        params = {"zip": location, "appid": api_key}
    else:
        params = {"q": location, "appid": api_key}

    resp = requests.get(base_url, params=params)
    data = resp.json()

    # Handle errors from OpenWeather
    if data.get("cod") != 200:
        return f"Could not fetch weather for '{location}': {data.get('message')}"

    desc = data["weather"][0]["description"]
    temp_c = round(data["main"]["temp"] - 273.15, 1)
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    city = data["name"]
    country = data["sys"]["country"]

    return (
        f"Weather in {city}, {country}: {desc}. "
        f"{temp_c}°C, humidity {humidity}%, wind {wind} m/s."
    )


if __name__ == "__main__":
    mcp.run()
