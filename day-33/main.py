import requests
import datetime as dt

URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=URL)
print(response)  # It will print <Response [200]>
print(response.status_code)  # It wil print 200

response.raise_for_status()  # Throws an exception in case of fail return

data = response.json()
print(data)
iss_lat = float(data['iss_position']['latitude'])
iss_lng = float(data['iss_position']['longitude'])


SUNRISE_URL = "https://api.sunrise-sunset.org/json"
PG_LAT = -23.998890
PG_LNG = -46.413540

sunrise_request_parameters = {
    "lat": PG_LAT,
    "lng": PG_LNG,
    "formatted": 0
}

sunrise_api_response = requests.get(url=SUNRISE_URL, params=sunrise_request_parameters)
sunrise_api_response.raise_for_status()
print(sunrise_api_response)
print(sunrise_api_response.json())
data = sunrise_api_response.json()
sunrise_hour = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset_hour = int(data['results']['sunset'].split('T')[1].split(':')[0])
print(sunset_hour)

