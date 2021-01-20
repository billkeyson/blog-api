from flask import request,Blueprint
import datetime
from . import make_response
from . import content_type_response
from pymongo import MongoClient

from models.comment_model import CommentModel as Comment
routes = Blueprint('comment_routes', __name__,url_prefix="/comment")

from flask_jwt_extended import (
    jwt_required, create_access_token
)

@routes.route("/add",methods=['POST'])
def add_post():
    required_post = ['post_id','content','user_id','author','author_email','author_ip','author_url','content_type','meta']
    if not request.is_json:
        return make_response('0','json content header  required')
    request_data= request.get_json()

    for key in required_post:
        if key not in request_data.keys():
            return make_response('0',f'{key} required field(s) missing')
    
    if not isinstance(request_data.get("meta"),list):
        return make_response('0','meta field is a list')
    
    save_post = Comment.add_comment(
        request_data.get("user_id"),request_data.get("post_id"),request_data.get("author"),request_data.get("author_email"),request_data.get("author_ip"),request_data.get("author_url"),request_data.get("content"),request_data.get("content_type"),request_data.get("meta"))
        
    return content_type_response(save_post)


@routes.route('/<postid>')
def findAll(postid):
    post_result = Comment.find_comment_by_post(postid)
    return content_type_response(post_result)
