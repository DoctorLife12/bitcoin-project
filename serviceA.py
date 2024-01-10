from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/ServiceA')
def get_bitcoin_value_a():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        bitcoin_data = response.json()
        value_in_dollars = bitcoin_data['bpi']['USD']['rate']

        timestamp = datetime.utcnow().strftime('%d-%m-%y %H:%MUTC')
        response_message = f"ServiceA, bitcoin value is {value_in_dollars} for '{timestamp}'"

        return jsonify(response_message), 200
    except Exception as e:
        return jsonify({'error': 'Error fetching bitcoin value'}), 500

@app.route('/ServiceB')
def get_bitcoin_value_b():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        bitcoin_data = response.json()
        value_in_dollars = bitcoin_data['bpi']['USD']['rate']

        timestamp = datetime.utcnow().strftime('%d-%m-%y %H:%MUTC')
        response_message = f"ServicB, bitcoin value is {value_in_dollars} for '{timestamp}'"

        return jsonify(response_message), 200
    except Exception as e:
        return jsonify({'error': 'Error fetching bitcoin value'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)