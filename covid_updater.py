import requests
from win10toast import ToastNotifier
import json
import time


def update():
    # r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    # data = r.json()
    data = {
        'cases': 10000000,
        'deaths': 14235,
        'recovered': 1000
    }
    text = (f'Confirmed cases : {data["cases"]} '
            f'\nDeaths : {data["deaths"]} '
            f'\nRecovered : {data["recovered"]}')

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates", text, duration=20)
        time.sleep(60)

update()