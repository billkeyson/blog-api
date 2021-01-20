from pymongo import MongoClient
from flask import Flask, Response, g, request
from werkzeug.exceptions import HTTPException
import json
import requests
import hashlib
import hmac
from urllib.parse import urlencode
import re
from bson import json_util
from flask_cors import CORS

from routes import (
    user_route,
    post_route,
    comment_route
    )


app = Flask(__name__)
app.register_blueprint(user_route.routes)
app.register_blueprint(post_route.routes)
app.register_blueprint(comment_route.routes)


# cors fix
CORS(app)

@app.errorhandler(500)
@app.errorhandler(HTTPException)
def server_error(e):

    return Response(response=\
    json.dumps({'error':'Server Error!'},\
        default=json_util.default),status=500,\
            mimetype= 'application/json')
    

@app.errorhandler(404)
def page_not_found(e):
    return json.dumps({"error": "Page Not Found"}), 404

@app.errorhandler(400)
def json_format(e):
    return json.dumps({"error": "incorrect json object!"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=False)
