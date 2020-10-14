from flask_restful import Resource
import logging as logger
from flask import jsonify, request
import json
from app import  app
import pandas as pd


class UsdInr(Resource):
    def get(self):
        logger.debug('Inside UsdInr get method')
        with open(app.config["json_file_path"] + '\CONFIG_USDINR.json') as f:
            data = json.load(f)
            return data

    def post(self):
        logger.debug('Inside CONFIG_USDINR post method')
        json_request = request.get_json()
        logger.debug("this is the json", json_request)
        logger.debug("CONFIG_USDINR", json_request)
        with open(app.config["json_file_path"] +'\CONFIG_USDINR.json') as f:
            data = json.load(f)
        for value in json_request:
            data[value] = json_request[value]
        jsonFile = open(app.config["json_file_path"] + "\CONFIG_USDINR.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()






@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': "error in routing or some fields"
    }
    response = jsonify(message)
    response.status_code = 404
    return response