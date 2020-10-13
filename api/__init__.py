from flask_restful import Api
from app import app
from flask import jsonify, request
from flask_cors import CORS
from .Crude import Crude
from .Menu import Menu
from .BankNifty import BankNifty
from .EurInr import EurInr
from .Gold import Gold
from .Nickel import Nickel
from .Nifty import Nifty
from .UsdInr import UsdInr
from .SilverMicro import SilverMicro


restServer = Api(app)
CORS(app)

# For Crude
restServer.add_resource(Crude, "/api/v1/crude")
# For Menu
restServer.add_resource(Menu, "/api/v1/menu")
# For Bank Nifty
restServer.add_resource(BankNifty, "/api/v1/bank_nifty")
# For Eur Inr
restServer.add_resource(EurInr, "/api/v1/eurinr")
# For Gold
restServer.add_resource(Gold, "/api/v1/gold")
# For Nickel
restServer.add_resource(Nickel, "/api/v1/nickel")
# For Nifty
restServer.add_resource(Nifty, "/api/v1/nifty")
# For usdinr
restServer.add_resource(UsdInr, "/api/v1/usdinr")
# For silver_micro
restServer.add_resource(SilverMicro, "/api/v1/silver_micro")



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': "error in routing or some fields"
    }
    response = jsonify(message)
    response.status_code = 404
    return response