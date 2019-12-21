from requests import get
import sys

def is_json_key_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False
    return True

def get_weather(key, city, unit):
    try:
        api_url = "http://api.weatherstack.com/current?access_key={}&query={}&units={}".format(key, city, unit)
        result = get(api_url)
        json_result = result.json()
        if is_json_key_present(json_result, "success"):
            raise ValueError("No data for city")
        temperature = json_result["current"]["temperature"]
        if unit == "f":
            unit = "Fahrenheit"
        else:
            unit = "Celsius"
        print("The weather in {} today is {} {}.".format(city, temperature, unit))
    except ValueError:
        print("Please choose an existing city like New York, Antwerp and Kathmandu.")



if __name__ == '__main__':
    key = sys.argv[1]
    cities = sys.argv[2].split(",")
    if sys.argv[3] == "-f":
        unit = "f"
    elif sys.argv[3] == "-c":
        unit = "m"
    else:
        print("Please choose -f or -c for type of degrees")
        exit()
    for city in cities:
        get_weather(key, city, unit)
