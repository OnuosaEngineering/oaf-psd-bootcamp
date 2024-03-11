import requests
import matplotlib.pyplot as plt

def fetch_weather_data():
    url = f'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def process_weather_data(data):
    processed_data = {
        'temperature': data['temperature'],
        'humidity': data['humidity'],
        'wind_speed': data['wind']['speed']
    }
    return processed_data

def visualize_weather_data(processed_data):
    labels = ['Temperature', 'Humidity', 'Wind Speed']
    values = [processed_data['temperature'], processed_data['humidity'], processed_data['wind_speed']]
    plt.bar(labels, values)
    plt.xlabel('Weather Parameter')
    plt.ylabel('Value')
    plt.title('Weather Data Visualization')
    plt.show()


def main():
    raw_data = fetch_weather_data()
    processed_data = process_weather_data(raw_data)
    visualize_weather_data(processed_data)

if __name__ == '__main__':
    main()

