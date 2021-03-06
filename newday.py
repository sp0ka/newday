import requests, json, math
api_key = "8305f8b53083f1201af409b013409f95"
base_url = "http://api.openweathermap.org/data/2.5/onecall?"
lat = "40.701780"
lon = "-73.930750"
complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&exclude=minutely&units=imperial&appid=" + api_key
response = requests.get(complete_url)
x = response.json()
y = x["current"]
z = x["daily"]
city_name = "Bushwick"
current_temperature = round(y["temp"])
feels_like = round(y["feels_like"])
current_humidity = y["humidity"]
chances_rain = round((z[4]["pop"]) * 100)

print ( str(city_name) +
            "\n Temperature (F) = " +
                str(current_temperature) +
            "\n Feels like = " +
                str(feels_like) +
            "\n Humidity = " +
                str(current_humidity) + '%' +
            "\n Chance of Rain = " +
                str(chances_rain) + "%" )