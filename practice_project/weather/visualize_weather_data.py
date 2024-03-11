import matplotlib.pyplot as plt

def visualize_weather_data(processed_data):
    labels = ['Temperature', 'Humidity', 'Wind Speed']
    values = [processed_data['temperature'], processed_data['humidity'], processed_data['wind_speed']]
    plt.bar(labels, values)
    plt.xlabel('Weather Parameter')
    plt.ylabel('Value')
    plt.title('Weather Data Visualization')
    plt.show()
