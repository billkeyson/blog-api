import datetime
import hashlib
import uuid
import math
import re
from flask import flash
from pymongo import MongoClient
import json
import requests
from urllib.parse import urlencode
from bson import json_util
import numbers
import settings
# from . from COMMENT

class CommentModel():
    @classmethod
    def connection(cls):
        db = MongoClient(settings.DATABASE_URL,settings.DATABASE_PORT)
        return db[settings.DATABASE_NAME]
    
    @classmethod
    def add_comment(cls,user_id,post_id,author,author_email,author_ip,author_url,\
        content,content_type,meta,parent_id=''):
        comment = {}
        comment['id'] = datetime.datetime.now().strftime('%Y%m%d') + \
                     uuid.uuid4().urn[9:].replace('-', '').upper()
        comment['uid'] = user_id
        comment['author_name'] =author
        comment['author_email'] = author_email
        comment['post_id'] = post_id
        comment['author_ip'] = author_ip
        comment['author_url'] = author_url
        comment['content_type']= content_type
        comment['content']= content
        comment['parent_comment'] =parent_id 
        comment['meta']= meta
        comment['created'] = datetime.datetime.utcnow()
        comment['modified'] = datetime.datetime.utcnow()

        if cls.connection()['comment'].insert_one(comment).inserted_id:
            return comment
        return {}
    
    @classmethod 
    def find_user_comment(cls,user_id):
        comments = cls.connection()['comment'].find({'user_id':user_id})
        all_comment = []
        if comments.count()>0:
            for comment in comments:
                comment.pop("_id")
                comment['created'] =str(comment['created'])
                comment['modified'] =str(comment['modified'])
                all_comment.append(comment)
        return all_comment
    
    @classmethod 
    def find_comment_by_post(cls,post_id):
        comments = cls.connection()['comment'].find({'post_id':post_id})
        all_comment = []
        if comments.count()>0:
            for comment in comments:
                comment.pop("_id")
                comment['created'] =str(comment['created'])
                comment['modified'] =str(comment['modified'])
                all_comment.append(comment)
        return all_comment
    




# COMMENT
# uid
# id
# post_id
# author
# author_email
# author_ip
# author_url
# created
# content
# approved
# type
# comm_parent
# mata{karma,etc}



