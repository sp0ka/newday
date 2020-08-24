import requests, json, math
api_key = "8305f8b53083f1201af409b013409f95"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_id = "5110302"
complete_url = base_url + "id=" + city_id + "&appid=" + api_key
response = requests.get(complete_url)
x = response.json()
y = x["main"]
city_name = x["name"]
current_temperature = y["temp"]
feels_like = y["feels_like"]
current_humidity = y["humidity"]
z = x["weather"]
weather_description = z[0]["description"]
celsius_temp = current_temperature - 273.15
fahrenheit_temp = round(celsius_temp * (9/5) + 32)
celsius_feels = feels_like - 273.15
fahrenheit_feels = round(celsius_feels * (9/5) + 32)

print ( str(city_name) +
            "\n Temperature (fahrenheit) = " +
                str(fahrenheit_temp) +
            "\n Feels like = " +
                str(fahrenheit_feels) +
            "\n Humidity = " +
                str(current_humidity) + '%' +
            "\n Description = " +
                str(weather_description))