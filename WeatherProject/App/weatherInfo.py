import requests
from datetime import datetime

def check_weather(cityName):
    api_key = "f25e4e03093c02ed3c52668dd29ebc4e"

    city = cityName

# "http://api.openweathermap.org/data/2.5/weather?q=lahore&units=metric&appid=f25e4e03093c02ed3c52668dd29ebc4e"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    try:
        data = requests.get(url).json()
    except Exception as e:
        print(f"Error: {e}")
        return "Error"

    print("******************\nData Value: ")
    print(data)
    print("******************")
    if data['cod'] == '404' or data['cod'] == '400':
        return "Error"
    else:
        weather = {
            'name' : "",
            'country' : "",
            'temp' : "",
            'feels_like' : "",
            'lat' : "",
            'lon' : "",
            'pressure' : "",
            'humidity' : "",
            'visibility' : "",
            'wather_type' : "",
            'datetime' : datetime.now()
        }

        weather['name'] = (f'{data["name"]}')  # City Name
        weather['country'] = (f'{data["sys"]["country"]}')  # Country
        weather['temp'] = (f'{int(round(data["main"]["temp"]))}°C')  # Temperature
        weather['feels_like'] = (f'{data["main"]["feels_like"]}°C')  # Feels Like
        weather['weather_type'] = (f'{data["weather"][0]["main"]}')  # Weather
        weather['lat'] = (f'{data["coord"]["lat"]}')  # Latitude
        weather['lon'] = (f'{data["coord"]["lon"]}')  # Longitude
        weather['pressure'] = (f'{data["main"]["pressure"]}hPa')  # Pressure (hecto Pascal)
        weather['humidity'] = (f'{data["main"]["humidity"]}%')  # Humidity
        weather['visibility'] = (f'{data["visibility"]/1000} km')  # Visibility

        for k,v in weather.items():
            print(k,': ',v)
        
        return weather

# check_weather()