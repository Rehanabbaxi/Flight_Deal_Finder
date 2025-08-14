import requests

class DataManager:
    def __init__(self ):
        self.url = 'https://api.sheety.co/48150efc13c26d390381a34f7aa31cef/copyOfFlightDeals/prices'
    def get_sheet_data(self):
        self.response = requests.get(url=self.url)
        return self.response.json()
