from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager as nm


search = FlightSearch()
cities = DataManager().city_list()
data_dict = DataManager().city_price_dict()

code_list = []
for item in cities:
    code_list.append(search.get_code(item))

fl_data = []
for code in code_list:
    fl_data.append(FlightData().search_flights(code))

#create dictionary
for data in fl_data:
    to_city = data["data"][0]["cityTo"]
    price = data["data"][0]["price"]
    lowest_price = int(data_dict.get(to_city))

    if price <= lowest_price:
        to_city_code = data["data"][0]["cityCodeTo"]
        from_city = data["data"][0]["cityFrom"]
        from_city_code = data["data"][0]["cityCodeFrom"]
        outbound_date = data["data"][0]["route"][0]["local_departure"]
        inbound_date = data["data"][0]["route"][1]["local_departure"]
        nm(price=price, dep_city=from_city, dep_city_iata=from_city_code, arr_city=to_city,
           arr_air_iata=to_city_code, outbound_date=outbound_date, inbound_date=inbound_date)
