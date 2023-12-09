from twilio.rest import Client

account_sid = "TOKEN"
auth_token = "TOKEN"


class NotificationManager:

    def __init__(self, price, dep_city, dep_city_iata, arr_city, arr_air_iata,
                 outbound_date, inbound_date):
        client = Client(account_sid, auth_token, )
        self.message = client.messages \
            .create(
            body=f"You will depart from {dep_city}({dep_city_iata}) on {outbound_date}"
                 f"going to {arr_city}({arr_air_iata}) and return home on{inbound_date}."
                 f"The price of this flight is {price}",
            from_="+1Num",
            to="+1Num"
        )

    #This class is responsible for sending notifications with the deal flight details.