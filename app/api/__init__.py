from flask import Blueprint
from flask_restful import Api

api = Blueprint('api', __name__)
rest = Api(api)

from . import views