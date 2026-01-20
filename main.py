import requests

# Function to convert WMO weather codes to human-readable descriptions
def get_weather_desc(code):
    # WMO Weather interpretation codes
    weather_codes = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤", 2: "Partly cloudy ⛅", 3: "Overcast ☁️",
        45: "Foggy 🌫", 48: "Depositing rime fog 🌫",
        51: "Light drizzle 🌧", 53: "Moderate drizzle 🌧", 55: "Dense drizzle 🌧",
        61: "Slight rain 🌦", 63: "Moderate rain 🌧", 65: "Heavy rain ⛈",
        71: "Slight snow ❄️", 73: "Moderate snow ❄️", 75: "Heavy snow ❄️",
        77: "Snow grains ❄️",
        80: "Slight rain showers 🌦", 81: "Moderate rain showers 🌧", 82: "Violent rain showers ⛈",
        95: "Thunderstorm 🌩"
    }
    return weather_codes.get(code, "Unknown Conditions")

# Fetch current weather data for Ashby-de-la-Zouch using the Open-Meteo API
def get_ashby_weather():
    # API endpoint for weather forecasts
    url = "https://api.open-meteo.com/v1/forecast"
    # Parameters: location coordinates and requested weather variables
    params = {
        "latitude": 52.747,
        "longitude": -1.474,
        "current": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m"],
        "timezone": "Europe/London"
    }

    try:
        # Make HTTP GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status() # Check for HTTP errors
        # Extract current weather data from JSON response
        data = response.json()["current"]
        
        # Extract and format individual weather metrics
        desc = get_weather_desc(data["weather_code"])
        temp = data["temperature_2m"]
        hum = data["relative_humidity_2m"]
        wind = data["wind_speed_10m"]

        # Display formatted weather information
        print(f"\n--- Ashby-de-la-Zouch Weather ---")
        print(f"Status:      {desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity:    {hum}%")
        print(f"Wind Speed:  {wind} km/h")
        print("-" * 34)

    except Exception as e:
        # Handle any errors from API requests or data processing
        print(f"Error fetching weather: {e}")

# Entry point: run the weather fetch when script is executed directly
if __name__ == "__main__":
    get_ashby_weather()