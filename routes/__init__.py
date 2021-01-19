from flask import Response
from flask_httpauth import HTTPTokenAuth
from bson import json_util
import json

def make_response(code, message):
    if code == '1':
        status = 200
    elif code == '0':
        status = 401
    return Response(response=json.dumps({
        'code': code, 'message': message},
        default=json_util.default),
        status=status,
        mimetype="application/json")

def make_ussd_response(response, statusCode,min_type="application/json"):
  return Response(response= response if min_type=='text/plain'else
    json.dumps(response,
      default=json_util.default),
      status=statusCode,
      mimetype=min_type)

def content_type_response(data):
    return Response(response=json.dumps(data,default=json_util.default),status=200,mimetype= 'application/json')
