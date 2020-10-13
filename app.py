from flask import Flask
import logging as logger
from flask_cors import CORS

logger.basicConfig(level="DEBUG")

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    from api import *
    app.run(host='127.0.0.1',port='9000',debug=True,use_reloader=True)