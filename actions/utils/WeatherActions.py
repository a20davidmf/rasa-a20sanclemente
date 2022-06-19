import requests

def search_weather(location, number):

    if number > 4:
        return None

    api_key = "6a36faf4f8d939b909d9b60b5a7ef038"

    base_url = "http://api.openweathermap.org/data/2.5/forecast?"

    complete_url = base_url + "appid=" + api_key + "&q=" + location + "&units=metric&cnt=5"

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        list_days = x["list"]

        current_day = list_days[number]

        current_temperature = current_day["main"]["temp"]
        weather_description = current_day["weather"][0]["description"]

        message = ""
        if number == 0:
            message = f"The temperature in {location} is {str(current_temperature)} °C and the description says: {str(weather_description)}"
        else:
            message = f"The temperature in {location} will be {str(current_temperature)} °C and the description says: {str(weather_description)}"
        return message

    else:
        return None