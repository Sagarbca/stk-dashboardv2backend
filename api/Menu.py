from flask_restful import Resource
import logging as logger
from flask import jsonify, request
import json
from app import  app
import pandas as pd


class Menu(Resource):
    def get(self):
        logger.debug('Inside crude get method')
        with open('D:\my_learning\stk_dashboard_backend\Json\menu.json') as f:
            data = json.load(f)
            return data







@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': "error in routing or some fields"
    }
    response = jsonify(message)
    response.status_code = 404
    return response