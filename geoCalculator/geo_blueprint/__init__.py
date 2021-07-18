from flask import Blueprint

geo_blueprint = Blueprint('geo_blueprint', __name__)

from . import views
