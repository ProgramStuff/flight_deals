import requests

GOOGLE_SHEETS_API = "https://api.sheety.co/1c7f573af857a5ac847015cb60d49933/copyOfFlightDeals/prices"
SHEETY_TOKEN = "TOKEN"
SHEETY_HEADERS = {
    "Content=Type": "application/json",
    "method": "POST",
    "body": "JSON.stringify",
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}



class DataManager:

    def __init__(self):
        self.cities_list = []
        self.dict = {}
        self.response = requests.get(GOOGLE_SHEETS_API, SHEETY_HEADERS)
        self.response.raise_for_status()
        self.sheet_data = self.response.json()["prices"]


    def city_list(self):
        for city in self.sheet_data:
            self.cities_list.append(city["city"])
        return self.cities_list

    def city_price_dict(self):
        for item in self.sheet_data:
            city = item["city"]
            price = item["lowestPrice"]
            data_dict = {city: price}
            self.dict.update(data_dict)
        return self.dict

#This class is responsible for talking to the Google Sheet.