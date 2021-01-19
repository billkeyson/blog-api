from flask import request,Blueprint
import datetime
from . import make_response
from . import content_type_response
from pymongo import MongoClient

from models import post_model as post
routes = Blueprint('post_routes', __name__,url_prefix="/post")

from flask_jwt_extended import (
    jwt_required, create_access_token
)

@routes.route("/add",methods=['POST'])
def add_post():
    required_post = ['post_id','name','user_id','status','post_count','post_status','post_parent','mime_type','content','meta']
    if not request.is_json:
        return make_response('0','json content header  required')
    request_data= request.get_json()

    for key in required_post:
        if key not in request_data.keys():
            return make_response('0',f'{key} required field(s) missing')
    
    if not isinstance(request_data.get("meta"),list):
        return make_response('0','meta field is a list')
    
    save_post = post.PostModel.add_post(
        request_data.get('user_id'),request_data.get('title'),\
        request_data.get('name'),request_data.get('author'),\
        request_data.get('content'),request_data.get('status'),\
        request_data.get('post_status'),\
        request_data.get('post_count'),\
        request_data.get('post_parent')\
        ,request_data.get('mime_type'),request_data.get('meta'),request_data.get('excerpt'))
        
    return content_type_response(save_post)


@routes.route('/findAll')
def findAll():
    post_result = post.PostModel.find_all_post()
    return content_type_response(post_result)


@routes.route('/s/<slug>')
def findByName(slug):
    post_result = post.PostModel.find_post_by_name(slug)
    return content_type_response(post_result)