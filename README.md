# HelloWorld-mcp: Weather MCP Server with FastMCP

A simple yet effective MCP server (Python microservice) for retrieving real-time weather information using the [OpenWeatherMap API](https://openweathermap.org/current), built on FastMCP (a server framework from the MCP ecosystem).

## Features

- Get current weather by city name, country, or zip code
- Humidity, temperature (°C), wind speed, and description
- Simple API interface using MCP toolbox

## Requirements

- Python 3.11+
- OpenWeatherMap API key ([see here](https://home.openweathermap.org/api_keys))

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-git-url>
   cd HelloWorld-mcp
   ```
2. **Install dependencies** (uses PEP 621 with `pyproject.toml`)
   ```bash
   uv pip install -r requirements.txt  # or use your preferred tool for PEP 621 dependencies
   ```
3. **Configure Environment**
   - Copy `.env.example` to `.env` and fill in your `OPENWEATHER_API_KEY`.

## Usage

### As a Python Module

```bash
python -m src.weather
```

### With MCP CLI

```bash
mcp dev src/weather.py
```

### Running as a Local MCP Server in Popular Clients

You can also run this MCP server locally from clients/hosts like Claude Desktop, Cursor, VS Code, etc., using the following configuration. **Make sure you have the `uv` package manager installed. Adjust the `--directory` path to match your own project location.**

Add or update your mcpServers configuration (e.g. in your host/editor settings):

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "D:\\model-context-protocol\\HelloWorld-mcp",
        "run",
        "src/weather.py"
      ]
    }
  }
}
```

> **Note:**
>
> - Change the directory path to where your project is located.
> - `uv` must be installed globally or available in your environment. ([see uv documentation](https://github.com/astral-sh/uv))

## Tool Implemented

`get_weather(location: str) -> str`: Returns formatted weather information for a specific city, country, or ZIP code.

#### Example

```
Weather in London, GB: light rain. 14.2°C, humidity 82%, wind 5.1 m/s.
```

## Configuration

Create a `.env` file in the project root:

```
OPENWEATHER_API_KEY=your_actual_api_key_here
```

## File Structure

- `src/weather.py` – main MCP server with weather tool logic
- `src/config.py` – loads settings (API key) from environment
- `pyproject.toml` – project metadata & dependencies
