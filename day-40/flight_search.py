from datetime import *

import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://api.tequila.kiwi.com"
        self.api_key = "7PdIpGfanjqD_PzQVAa5w8p5SE96n4ss"
        self.headers = {
            "apikey": self.api_key
        }

    def search_flight(self, fly_to: str, date_from: datetime, date_to: datetime, fly_from='BRA'):
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y")
        }
        response = requests.get(url=f"{self.url}/v2/search", params=params, headers=self.headers)
        response.raise_for_status()

        return response

    def get_destination_code(self, city: str):
        params = {
            "term": city
        }
        print(params)
        response = requests.get(url=f"{self.url}/locations/query", params=params, headers=self.headers)
        response.raise_for_status()

        return response.json()['locations'][0]['code']
