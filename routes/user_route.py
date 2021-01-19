from flask import request,Blueprint
import datetime
from . import make_response
from . import content_type_response
from pymongo import MongoClient

routes = Blueprint('user_routes', __name__,url_prefix="/user")

from flask_jwt_extended import (
    jwt_required, create_access_token
)

# username = ["uid","username","password","email","created","modified","status","nickname","meta{list of obj}"]

@routes.route("/add")
def add_user():
    pass