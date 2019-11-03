# Entry point for API server

from flask import Flask
import requests
import json
import os
from weather import weather
from agriculture import agriculture
# if os.path.isfile('.env'):
#     load_dotenv('.env')

app = Flask(__name__)

# Blueprints for API sets the API hooks into
app.register_blueprint(weather, url_prefix='/api/weather')
app.register_blueprint(agriculture, url_prefix='/api/agriculture')


# Route for API server check
@app.route("/api")
def home():
    # ip = get_IP()
    # coords = get_location_by_ip(ip['ip'])
    # location = get_location_by_coord(coords['latitude'], coords['longitude'])
    return "Hi"


if __name__ == "__main__":
    app.run(debug=True)


