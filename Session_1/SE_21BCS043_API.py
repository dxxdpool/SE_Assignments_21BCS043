from flask import Flask, jsonify, request

app = Flask(__name__)

# Define some example events
events = {
    "event1": {"name": "Concert", "date": "2022-05-01", "tickets_available": 100},
    "event2": {"name": "Theater", "date": "2022-06-15", "tickets_available": 50},
    "event3": {"name": "Comedy Show", "date": "2022-07-20", "tickets_available": 75}
}

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

@app.route('/buy-ticket', methods=['POST'])
def buy_ticket():
    data = request.get_json()
    event_id = data['event_id']
    if event_id in events:
        if events[event_id]['tickets_available'] > 0:
            events[event_id]['tickets_available'] -= 1
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Sold out'})
    else:
        return jsonify({'success': False, 'error': 'Event not found'})

if __name__ == '__main__':
    app.run()
