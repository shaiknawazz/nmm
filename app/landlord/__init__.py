from flask import Blueprint

landlord = Blueprint('landlord', __name__)

from . import views