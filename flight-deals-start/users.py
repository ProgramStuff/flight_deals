import requests


GOOGLE_SHEETS_API = "https://api.sheety.co/1c7f573af857a5ac847015cb60d49933/copyOfFlightDeals/users"
SHEETY_TOKEN = ""

#
#
#
# class Users:
#
#
#     def create_user(self):
print("Welcome to Jordan's flight club. \n We find the best/cheapest flights and email them to you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
retype_email = input("Please retype your email to verify it is correct.\n")
user_params = {
    "First Name": first_name,
    "Last_Name": last_name,
    "Email": email
}
SHEETY_HEADERS = {
    "Content=Type": "application/json",
    "method": "POST",
    "body": f"JSON.stringify",
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
if email == retype_email:
    response = requests.put(url=GOOGLE_SHEETS_API, headers=SHEETY_HEADERS, json=user_params)
    response.raise_for_status()
    data = response.json()
    print(response)
    print("Welcome to the club!")
else:
    print("The emails you entered did not match, please try again.")

