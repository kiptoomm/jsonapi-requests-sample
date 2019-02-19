import json
from pprint import pprint
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello, world!'

# set trailing slash on route to accommodate jsonapi_requests'
# request format - "GET /api/2.0/car/2/ HTTP/1.1"
# https://stackoverflow.com/a/33285603/1145905
@app.route('/api/2.0/car/<int:car_id>/')
def get_data(car_id):
	print('requested car id: ', car_id)
	with open('data.json') as f:
		data = json.load(f)
	#pprint(type(data))
	return jsonify(data)
