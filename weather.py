import requests

def get_weather(city, api_key):
    """Fetch weather data from OpenWeatherMap API."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 401:
            print("Unauthorized error: Check your API key or account status.")
        elif response.status_code == 404:
            print("City not found: Please check the city name.")
        else:
            response.raise_for_status()
        data = response.json()

        # Extract and display data
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"Weather in {city}: {weather}, Temperature: {temp}°C")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    API_KEY = "19425894eb2607c09286e07e7abcb546"  # Replace with a valid API key
    city = input("Enter the city name: ")
    get_weather(city, API_KEY)
