import datetime

import requests

NUTRITION_API_ID = '2e8901be'
NUTRITION_API_KEY = 'bf39d4c9a3ff6658042f2f293efb2e88'

natural_exercise_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = {
    "query": "workout 80 minutes",
    "gender": "male",
    "weight_kg": 74.5,
    "height_cm": 181.50,
    "age": 38
}

headers = {
    'x-app-id': NUTRITION_API_ID,
    'x-app-key': NUTRITION_API_KEY,
    'content-type': 'application/json'
}

response = requests.post(url=natural_exercise_end_point, json=query, headers=headers)
response.raise_for_status()

exercises_list = response.json()['exercises']
sheety_url = 'https://api.sheety.co/e1448678a6f2c025a184a32ca9961485/myWorkouts/workouts';
sheety_headers = {
    "Authorization": "Bearer asdFASDfasdfasdf"
}
for exercise in exercises_list:
    duration_min = exercise['duration_min']
    calories = exercise['nf_calories']
    exercise_name = exercise['name']
    date = datetime.datetime(year=2024, month=2, day=21).strftime("%d/%m/%Y")
    t = datetime.time(hour=5, minute=40, second=0).strftime("%H:%M:%S")

    body = {
        "workout": {
            "date": date,
            "time": t,
            "exercise": exercise_name,
            "duration": duration_min,
            "calories": calories
        }
    }

    response = requests.post(url=sheety_url, json=body, headers=sheety_headers)
    response.raise_for_status()
    print(response.text)


sheety_response = requests.get(url=sheety_url, headers=sheety_headers)
sheety_response.raise_for_status()

print(sheety_response.text)
