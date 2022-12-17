import json
import requests


def webhook():
    url = "http://127.0.0.1:8000/webhook"

    payload = {
        "FirstName": "First",
        "LastName": "Name",
        "Email": "name@email.com",
    }

    response = requests.post(
        url, data=json.dumps(payload), headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        raise Exception("Not OK (non-200 status code received)")

    response = response.text

    print(f"Response: {response}")


def event():
    url = "http://127.0.0.1:8000/event"

    payload = {
        "event": "event-update",
        "date": "2022-08-23",
        "clearence": {
            "min": "200",
            "max": "800",
        },
    }

    response = requests.post(
        url, data=json.dumps(payload), headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        raise Exception("Not OK (non-200 status code received)")

    response = response.text

    print(f"Response: {response}")


if __name__ == "__main__":
    webhook()
    event()
