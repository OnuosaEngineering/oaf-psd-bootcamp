def process_weather_data(raw_data):
    processed_data = {
        'temperature': raw_data['temperature'],
        'humidity': raw_data['humidity'],
        'wind_speed': raw_data['wind']['speed']
    }
    return processed_data
