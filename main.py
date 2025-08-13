#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *

sheet_endpoint  = 'https://api.sheety.co/48150efc13c26d390381a34f7aa31cef/copyOfFlightDeals/prices'

data_manager = DataManager(sheet_endpoint)
data = data_manager.get_sheet_data()
print(data)