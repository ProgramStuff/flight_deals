import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"
flight_api_key = "KEY"


class FlightSearch:

    #This class is responsible for talking to the Flight Search API.


    def get_code(self, city):
        location_endpoint = f"{TEQUILA_ENDPOINT}locations/query"
        headers = {
            "apikey": flight_api_key
        }
        query = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        response.raise_for_status()
        flight_data = response.json()["locations"]
        code = flight_data[0]["code"]
        return code
