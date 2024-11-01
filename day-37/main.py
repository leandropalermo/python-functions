import datetime

import requests

USERNAME = 'leandropalermo'
TOKEN = 'jkasdjkf9384kjDDKD'
GRAPH_NAME = 'graph1'

pixela_end_point = 'https://pixe.la/v1/users'
leandro_pixela_end_point = ' https://pixe.la/@leandropalermo'
pixela_graph_end_point = f"{pixela_end_point}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=pixela_end_point, json=user_params)
    print(response.text)

def create_graph():
    graph_params = {
        "id": GRAPH_NAME,
        "name": "Cycling graph",
        "unit": "Km",
        "type": "float",
        "color": "sora"
    }

    requests.post(url=pixela_graph_end_point, json=graph_params, headers=headers)


def add_graph_pixel():
    today = datetime.datetime.now()
    pixel_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "5.2",
    }

    response = requests.post(url=f"{pixela_graph_end_point}/{GRAPH_NAME}", json=pixel_params, headers=headers)
    response.raise_for_status()
    print(response.text)

def delete_request():
    some_day = datetime.datetime(year=2024, month=2, day=21).strftime("%Y%m%d")
    response = requests.delete(url=f"{pixela_graph_end_point}/{GRAPH_NAME}/{some_day}", headers=headers)
    response.raise_for_status()

def update_request():

    some_day = datetime.datetime(year=2024, month=2, day=21).strftime("%Y%m%d")
    request_body = {
        "quantity": "10.4"
    }

    response = requests.put(url=f"{pixela_graph_end_point}/{GRAPH_NAME}/{some_day}", json=request_body, headers=headers)
    response.raise_for_status()

# create_user()
# create_graph()
# add_graph_pixel()
# update_request()
delete_request()