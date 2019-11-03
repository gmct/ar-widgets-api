# Hooks into soilgrids coarse soil composition GIS data.

from flask import Blueprint, jsonify, request
import requests
import json

agriculture = Blueprint('agriculture', __name__)

# Gets all available soil data at desired coordinates
@agriculture.route("/soilconditions", defaults ={'latitude':None, 'longitude':None})
def get_soil_conditions(latitude, longitude):
    if (latitude == None):
        latitude = request.args.get('lat')
    if (longitude == None):    
        longitude = request.args.get('lon')
    send_url = "https://rest.soilgrids.org/query?lat=" + str(latitude) + "&lon=" + str(longitude)
    r = requests.get(send_url)
    j = json.loads(r.text)
    resp = jsonify(j)
    resp.status_code = r.status_code
    return resp

# Only returns soil type data at desired coordinates.
@agriculture.route("/soiltype", defaults ={'latitude':None, 'longitude':None})
def get_soil_type(latitude, longitude):
    if (latitude == None):
        latitude = request.args.get('lat')
    if (longitude == None):    
        longitude = request.args.get('lon')
    send_url = "https://rest.soilgrids.org/query?lat=" + str(latitude) + "&lon=" + str(longitude) + "&attributes=TAXNWRB"
    r = requests.get(send_url)
    j = json.loads(r.text)
    resp = jsonify(j)
    resp.status_code = r.status_code
    return resp

# Returns temperature and precipitation data
@agriculture.route("/climate", defaults ={'latitude':None, 'longitude':None})
def get_climate(latitude, longitude):
    if (latitude == None):
        latitude = request.args.get('lat')
    if (longitude == None):    
        longitude = request.args.get('lon')
    send_url = "https://rest.soilgrids.org/query?lat=" + str(latitude) + "&lon=" + str(longitude) + "&attributes=PREMRG,TM"
    r = requests.get(send_url)
    j = json.loads(r.text)
    resp = jsonify(j)
    resp.status_code = r.status_code
    return resp