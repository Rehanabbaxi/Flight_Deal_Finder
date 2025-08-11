class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass

import requests
from dotenv import  load_dotenv
import  os

load_dotenv()
flight_api = os.getenv("AMADEUS_API_KEY")
flight_api_secret = os.getenv("AMADEUS_API_SECRET")

url = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {
    "grant_type": "client_credentials",
    "client_id": flight_api,
    "client_secret": flight_api_secret
}

response = requests.post(url, headers=headers, data=data)
token = response.json()["access_token"]

flight_search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
params = {
    "originLocationCode": "NYC",
    "destinationLocationCode": "LON",
    "departureDate": "2025-08-11",
    "adults": "1"
}
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(flight_search_url, headers=headers, params=params)
data = response.json()
for i in range(len(data)+1):
    print(data["data"][i]["price"]["total"])





