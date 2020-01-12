from requests import get
import click



def is_json_key_present(json, key):
    try:
        buf = json[key]
    except KeyError:
        return False
    return True

@click.command()
@click.option('--token', 'token', help='Token for my weather site')
@click.option('--city', 'city', help='List of cities')
@click.option('--T', 'temp', help='Celsius or Fahrenheit')
def get_weather(token, city, temp):
    cities = city.split(",")
    if temp == "Fahrenheit":
        unit = "f"
    else:
        unit = "m"
    for city in cities:
        api_url = "http://api.weatherstack.com/current?access_key={}&query={}&units={}".format(token, city, unit)
        result = get(api_url)
        json_result = result.json()
        if is_json_key_present(json_result, "success"):
            if json_result["error"]["type"] == "invalid_access_key":
                print("Please provide a valid key.")
                exit()
            else:
                print("Please choose an existing city like New York, Antwerp and Kathmandu.")
                exit()
        temperature = json_result["current"]["temperature"]
        print("The weather in {} today is {} {}.".format(city, temperature, temp))



if __name__ == '__main__':
    get_weather()
