import pandas

from flight_search import FlightSearch
from datetime import *


class FlightData:

    def __init__(self):
        self.flight_search = FlightSearch()

    def find_best_price(self, fly_to) -> dict:
        flights = self.flight_search.search_flight(fly_to=fly_to,
                                                   date_from=datetime.now() + timedelta(days=1),
                                                   date_to=datetime.now() + timedelta(days=180))
        columns = ['cityTo', 'price', 'cityCodeFrom', 'cityCodeTo', 'utc_departure', 'duration', 'cityFrom']
        full_data = pandas.DataFrame.from_dict(flights.json()['data'])
        data = pandas.DataFrame(full_data, columns=columns)
        s = data.loc[(data['price']) == data['price'].min()]
        return s.to_dict('records')
