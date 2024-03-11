from practice_project.weather.fetch_weather_data import fetch_weather_data
from practice_project.weather.process_weather_data import process_weather_data
from practice_project.weather.visualize_weather_data import visualize_weather_data

def main():
    raw_data = fetch_weather_data()
    processed_data = process_weather_data(raw_data)
    visualize_weather_data(processed_data)

if __name__ == '__main__':
    main()
