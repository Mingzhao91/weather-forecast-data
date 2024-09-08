API_KEY = "6a1575051b1bc2d3c0c021d12e30be02"
import requests

def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    print(filter)
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))