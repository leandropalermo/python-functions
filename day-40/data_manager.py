import requests


class DataManager:

    def __init__(self):
        self.prices_url = "https://api.sheety.co/e1448678a6f2c025a184a32ca9961485/flightDeals/prices"
        self.prices_bearer_token = "Bearer sdklsdkldflklsdk"
        self.prices_headers = {
            "Authorization": self.prices_bearer_token
        }
        self.users_sheety_url = 'https://api.sheety.co/e1448678a6f2c025a184a32ca9961485/flightDeals/users'
        self.users_token = 'Bearer sklfdlkflskflksklflksdfl'
        self.users_headers = {
            "Authorization": self.users_token
        }

    def fetch_flight_data(self):
        response = requests.get(url=self.prices_url, headers=self.prices_headers)
        response.raise_for_status()

        return response.json()['prices']

    def update_iata_code(self, price_id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.prices_url}/{price_id}", json=body, headers=self.prices_headers)
        response.raise_for_status()

    def register_new_user(self, first_name, last_name, email):
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=self.users_sheety_url, json=body, headers=self.users_headers)
        response.raise_for_status()


    def fetch_users(self):
        response = requests.get(self.users_sheety_url, headers=self.users_headers)
        response.raise_for_status()
        return response.json()['users']