import requests
import json

API_URL = "http://localhost:5000"

def get_events():
    response = requests.get(API_URL + "/events")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to retrieve events")

def buy_ticket(event_id):
    payload = {'event_id': event_id}
    response = requests.post(API_URL + "/buy-ticket", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to buy ticket")

def test_get_events():
    events = get_events()
    assert type(events) == dict, "get_events() did not return a dictionary"
    assert len(events) > 0, "get_events() returned an empty dictionary"
    print("get_events() test passed")

def test_buy_ticket():
    events = get_events()
    assert len(events) > 0, "get_events() returned an empty dictionary"
    event_id = list(events.keys())[0]
    result = buy_ticket(event_id)
    assert result['success'] == True, "buy_ticket() was not successful"
    print("buy_ticket() test passed")

if __name__ == '__main__':
    test_get_events()
    test_buy_ticket()
    print("all tests passed.")
