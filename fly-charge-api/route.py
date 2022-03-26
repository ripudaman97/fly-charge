from flask import Flask, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


@app.route('/getChargingStations/<noOfChargingStations>', methods=['GET'])
def getChargingStationsNeeded(noOfChargingStations):
    return twc.getStatesInCountry(noOfChargingStations)


if __name__ == '__main__':
    app.run(debug=True)