from flask_restful import Resource
import logging as logger
from flask import jsonify, request
import json
from app import  app
import pandas as pd


class Nickel(Resource):
    def get(self):
        logger.debug('Inside Nickel get method')
        with open('D:\my_learning\stk_dashboard_backend\Json\CONFIG_NICKEL.json') as f:
            data = json.load(f)
            return data

    def post(self):
        logger.debug('Inside CONFIG_NICKEL post method')
        json_request = request.get_json()
        logger.debug("this is the json", json_request)
        logger.debug("CONFIG_NICKEL", json_request)
        with open('D:\my_learning\stk_dashboard_backend\Json\CONFIG_NICKEL.json') as f:
            data = json.load(f)
        for value in json_request:
            data[value] = json_request[value]
        jsonFile = open("D:\my_learning\stk_dashboard_backend\Json\CONFIG_NICKEL.json", "w+")
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