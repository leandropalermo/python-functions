import requests


class DataManager:

    def __init__(self):
        self.url = "https://api.sheety.co/e1448678a6f2c025a184a32ca9961485/flightDeals/prices"
        self.bearer_token = "Bearer sdklsdkldflklsdk"
        self.headers = {
            "Authorization": self.bearer_token
        }

    def fetch_flight_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        response.raise_for_status()

        return response.json()['prices']

    def update_iata_code(self, price_id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.url}/{price_id}", json=body, headers=self.headers)
        response.raise_for_status()

