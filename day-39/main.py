# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import *

import pandas

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

prices = data_manager.fetch_flight_data()
lowest_prices = []
for price in prices:
    iata_code = price['iataCode']
    if not iata_code:
        iata_code = flight_search.get_destination_code(price['city'])
        price['iataCode'] = iata_code
        data_manager.update_iata_code(price_id=price['id'], iata_code=iata_code)

    low_price = flight_data.find_best_price(iata_code)
    if low_price[0]['price'] < price['lowestPrice']:
        lowest_prices.append(low_price[0])

notification_manager = NotificationManager()
print(lowest_prices)
notification_manager.notify_low_price(lowest_prices)