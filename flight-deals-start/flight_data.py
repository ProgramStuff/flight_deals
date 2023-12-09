import requests
from datetime import datetime as dt
from datetime import timedelta

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"
FLIGHTS_API_KEY = "KEY"
now = dt.now()
tomorrow = now + timedelta(1)
tomorrow = tomorrow.strftime("%d/%m/%Y")
six_months = now + timedelta(180)
six_months = six_months.strftime("%d/%m/%Y")


class FlightData:

    #This class is responsible for structuring the flight data.

    def search_flights(self, code):
        search_endpoint = f"{TEQUILA_ENDPOINT}v2/search"
        headers = {
            "apikey": FLIGHTS_API_KEY,
        }

        params = {
            "fly_from": "LON",
            "fly_to": code,
            "date_from": tomorrow,
            "date_to": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "one_for_city": 1,
            "curr": "GBP",

        }

        response = requests.get(url=search_endpoint, headers=headers, params=params)
        response.raise_for_status()
        flights = response.json()
        return flights
