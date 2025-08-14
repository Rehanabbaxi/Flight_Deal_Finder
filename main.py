#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *


data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
print(sheet_data["prices"])