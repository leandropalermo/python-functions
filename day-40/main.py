from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
users = []


def register_user():
    first_name = input("What's your first name?\n")
    last_name = input("What's your last name?\n")
    email = input("What's your email?\n")

    global users
    users = data_manager.fetch_users()
    is_user_exists = [user for user in users if user['email'] == email]
    if is_user_exists:
        print("Users already registered")
    else:
        data_manager.register_new_user(first_name=first_name.title(), last_name=last_name.title(), email=email)


def process_flight_data_and_notify_users():
    flight_search = FlightSearch()
    flight_data = FlightData()

    flight_prices = data_manager.fetch_flight_data()
    lowest_prices = []
    for flight_price in flight_prices:
        iata_code = flight_price.get('iataCode', None)
        if not iata_code:
            city = flight_price.get('city', None)
            iata_code = flight_search.get_destination_code(city)
            flight_price['iataCode'] = iata_code
            data_manager.update_iata_code(price_id=flight_price['id'], iata_code=iata_code)

        best_price = flight_data.find_best_price(iata_code)
        if best_price[0]['price'] < flight_price['lowestPrice']:
            lowest_prices.append(best_price[0])

    notification_manager = NotificationManager()
    [notification_manager.notify_low_price(lowest_prices, user['email']) for user in users]


register_user()
process_flight_data_and_notify_users()
