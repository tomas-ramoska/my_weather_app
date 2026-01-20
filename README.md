# My Weather App

A lightweight Python weather application that fetches and displays current weather conditions for Ashby-de-la-Zouch using the Open-Meteo API.

## Features

- **Real-time weather data**: Fetches current weather conditions via the free Open-Meteo API
- **Comprehensive metrics**: Displays temperature, humidity, wind speed, and weather conditions
- **Weather emoji indicators**: Visual weather status with emoji representations
- **WMO weather codes**: Converts standard WMO weather codes to human-readable descriptions
- **Error handling**: Graceful error messages for API failures

## Requirements

- Python 3.7+
- `requests` library

## Installation

1. Clone or download this project
2. Install dependencies:

   ```bash
   pip install requests
   ```
   Or with uv:
   ```bash
   uv add requests
   ```

## Usage

Run the application:

```bash
python main.py
```

Or with uv:

```bash
uv run main.py
```

## Output Example

```
--- Ashby-de-la-Zouch Weather ---
Status:      Partly cloudy ⛅
Temperature: 12°C
Humidity:    65%
Wind Speed:  15 km/h
----------------------------------
```

## Location Details

- **City**: Ashby-de-la-Zouch
- **Coordinates**: 52.747°N, 1.474°W
- **Country**: United Kingdom (Leicestershire)
- **Timezone**: Europe/London

## API Information

This app uses the **Open-Meteo API**, a free weather API that requires no authentication:
- **Endpoint**: https://api.open-meteo.com/v1/forecast
- **Weather Variables**:
  - `temperature_2m`: Temperature at 2 meters above ground (°C)
  - `relative_humidity_2m`: Relative humidity at 2 meters (%)
  - `weather_code`: WMO Weather Interpretation Code
  - `wind_speed_10m`: Wind speed at 10 meters (km/h)

## Weather Codes

The application interprets WMO weather codes:

| Code | Description |
|------|-------------|
| 0 | Clear sky ☀️ |
| 1 | Mainly clear 🌤 |
| 2 | Partly cloudy ⛅ |
| 3 | Overcast ☁️ |
| 45, 48 | Foggy 🌫 |
| 51-55 | Drizzle 🌧 |
| 61-65 | Rain 🌧 |
| 71-77 | Snow ❄️ |
| 80-82 | Rain showers 🌦 |
| 95+ | Thunderstorm 🌩 |

## Project Structure

```
my_weather_app/
├── main.py          # Main application script
├── pyproject.toml   # Project configuration
└── README.md        # This file
```

## Error Handling

The application includes error handling for:
- Network connectivity issues
- Invalid API responses
- Missing or malformed data

If an error occurs, a message will be displayed: `Error fetching weather: [error details]`

## Future Enhancements

- Add support for multiple locations
- Implement weather forecasts (hourly/daily)
- Add data caching to reduce API calls
- Create a GUI interface
- Export weather data to CSV/JSON

## License

This project is open source and available for personal and educational use.

## Resources

- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [WMO Weather Codes](https://www.noaa.gov/)
