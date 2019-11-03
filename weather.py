from flask import Blueprint, jsonify, request
import requests
import json
import os

weather = Blueprint('weather', __name__)

# Unused method for getting IP of client.
def get_IP():
    ip = request.remote_addr
    data = {'ip':ip}
    resp = jsonify(data)
    resp.status_code = 200
    return resp

# Uses freeish API to get coordinates.
def get_location_by_ip(ipAddress):
    send_url = "http://api.ipstack.com/" + ipAddress +  "?access_key=" + os.environ.get("IPSTACK_KEY")
    r = requests.get(send_url)
    j = json.loads(r.text)
    resp = jsonify(j)
    resp.status_code = r.status_code
    return resp

# Converts GPS coordinates into location code for Accuweather API
@weather.route("/locationcode")
def get_location_by_coord(latitude=None, longitude=None):
    if (latitude == None):
        latitude = request.args.get('lat')
    if (longitude == None):        
        longitude = request.args.get('lon')
    send_url = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
    coords_string = str(latitude) + "," + str(longitude)
    payload = {'apikey':os.environ.get('WEATHER_KEY'), 'q':coords_string}
    # data_json = json.dumps(data)
    # payload = {'json_payload': data_json, 'apikey': 'YOUR_API_KEY_HERE'}
    r = requests.get(url=send_url, params=payload)
    j = json.loads(r.text)
    return j

# Gets current weather conditions at desired coordinates.
@weather.route("/currentconditions", defaults ={'location_key':None})
@weather.route("/currentconditions/<location_key>")
def get_current_conditions(location_key):
    # Checks to see if location key is provided in URL to save API call
    if (location_key == None):
        latitude = request.args.get('lat')
        longitude = request.args.get('lon')
        location = get_location_by_coord(latitude, longitude)
        location_key = location['Key']
    send_url = "http://dataservice.accuweather.com/currentconditions/v1/" + str(location_key)
    payload = {'apikey':os.environ.get('WEATHER_KEY')}
    r = requests.get(url=send_url, params=payload)
    j = json.loads(r.text)
    return j[0]

# Gets 1 day forecast at desired coordinates.
@weather.route("/forecasts/1day", defaults ={'location_key':None})
@weather.route("/forecasts/1day/<location_key>")
def get_1_day_forecast(location_key, language='en-us', details='false', metric='false'):
    # Checks to see if location key is provided in URL to save API call
    if (location_key == None):
        latitude = request.args.get('lat')
        longitude = request.args.get('lon')
        location = get_location_by_coord(latitude, longitude)
        location_key = location['Key']
    send_url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/' + str(location_key)
    payload = {'apikey':os.environ.get('WEATHER_KEY'), 'language':language, 'details':details, 'metric':metric}
    r = requests.get(url=send_url, params=payload)
    j = json.loads(r.text)
    print(j)
    return j

# Gets 5 day forecast at desired coordinates.
@weather.route("/forecasts/5day", defaults ={'location_key':None})
@weather.route("/forecasts/5day/<location_key>")
def get_5_day_forecast(location_key, language='en-us', details='false', metric='false'):
    # Checks to see if location key is provided in URL to save API call
    if (location_key == None):
        latitude = request.args.get('lat')
        longitude = request.args.get('lon')
        location = get_location_by_coord(latitude, longitude)
        location_key = location['Key']
    send_url = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' + str(location_key)
    payload = {'apikey':os.environ.get('WEATHER_KEY'), 'language':language, 'details':details, 'metric':metric}
    r = requests.get(url=send_url, params=payload)
    j = json.loads(r.text)
    return j

# Gets 10 day forecast at desired coordinates. Doesn't work with limited account
@weather.route("/forecasts/10day", defaults ={'location_key':None})
@weather.route("/forecasts/10day/<location_key>")
def get_10_day_forecast(location_key, language='en-us', details='false', metric='false'):
    # Checks to see if location key is provided in URL to save API call
    if (location_key == None):
        latitude = request.args.get('lat')
        longitude = request.args.get('lon')
        location = get_location_by_coord(latitude, longitude)
        location_key = location['Key']
    send_url = 'http://dataservice.accuweather.com/forecasts/v1/daily/10day/' + str(location_key)
    payload = {'apikey':os.environ.get('WEATHER_KEY'), 'language':language, 'details':details, 'metric':metric}
    r = requests.get(url=send_url, params=payload)
    j = json.loads(r.text)
    print(j)
    return j

# Gets 10 day forecast at desired coordinates. Doesn't work with limited account
@weather.route("/forecasts/15day", defaults ={'location_key':None})
@weather.route("/forecasts/15day/<location_key>")
def get_15_day_forecast(location_key, language='en-us', details='false', metric='false'):
    # Checks to see if location key is provided in URL to save API call
    if (location_key == None):
        latitude = request.args.get('lat')
        longitude = request.args.get('lon')
        location = get_location_by_coord(latitude, longitude)
        location_key = location['Key']
    send_url = 'http://dataservice.accuweather.com/forecasts/v1/daily/15day/' + str(location_key)
    payload = {'apikey':os.environ.get('WEATHER_KEY'), 'language':language, 'details':details, 'metric':metric}
    r = requests.get(url=send_url, params=payload)
    j = json.loads(r.text)
    return j