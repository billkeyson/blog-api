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
from .import comment_model as Comment
# from . from post
class PostModel():
    @classmethod
    def connection(cls):
        db = MongoClient(settings.DATABASE_URL,settings.DATABASE_PORT)
        return db[settings.DATABASE_NAME]
    
    @classmethod
    def add_post(cls,user_id,title,name,author,content,\
        status,post_status,post_count,post_parent,mime_type,meta,excerpt=[]):
        post = {}
        post['id'] = datetime.datetime.now().strftime('%Y%m%d') + \
                     uuid.uuid4().urn[9:].replace('-', '').upper()
        post['user_id'] = user_id
        post['title'] = title
        post['name'] = title
        post['status'] =status
        post['post_count'] = post_count
        post['post_status'] = post_status
        post['post_parent'] = post_parent
        post['mime_type']= mime_type
        post['content']= content
        post['meta']= meta
        post['excerpt']= meta
        post['created'] = datetime.datetime.utcnow()
        post['modified'] = datetime.datetime.utcnow()

        if cls.connection()['post'].insert_one(post).inserted_id:
            return post
        return {}
    
    @classmethod 
    def find_all_post(cls):
        posts = cls.connection()['post'].find({})
        all_post = []
        if posts.count()>0:
            for post in posts:
                post.pop("_id")
                post['created'] =str(post['created'])
                post['modified'] =str(post['modified'])
                all_post.append(post)
        return all_post

    @classmethod 
    def find_post_by_name(cls,slug):
        posts = cls.connection()['post'].find_one({'slug':slug})
        # all_post = []
        # if posts.count()>0:
        #     for post in posts:
        #         post.pop("_id")
        #         post['created'] =str(post['created'])
        #         post['modified'] =str(post['modified'])
        #         all_post.append(post)
        # return all_post
        if posts:
            posts.pop("_id")
            posts['created'] =str(posts['created'])
            posts['modified'] =str(posts['modified'])
            return posts
        return {}
    
    @classmethod 
    def find_post_by_id(cls,post_id):
        posts = cls.connection()['post'].find({'id':post_id})
        all_post = []
        if posts.count()>0:
            for post in posts:
                post.pop("_id")
                post['created'] =str(post['created'])
                post['modified'] =str(post['modified'])
                all_post.append(post)
        return all_post
    
    @classmethod 
    def find_post_by_userid(cls,user_id):
        posts = cls.connection()['post'].find({'user_id':user_id})
        all_post = []
        if posts.count()>0:
            for post in posts:
                post.pop("_id")
                post['created'] =str(post['created'])
                post['modified'] =str(post['modified'])
                all_post.append(post)
        return all_post
    
    @classmethod
    def find_all_data_by_name(cls,name =None,post_id=None):
        db = cls.connection()
        if name is None:
            query = {'id':post_id}
        else:
            query = {"name":name}
        posts = db['post'].find(query)
        all_post = []
        if posts.count()>0:
            for post in posts:
                post.pop("_id")
                post['created'] =str(post['created'])
                post['modified'] =str(post['modified'])
                # get pafent commment(s) plus sub comment(s)
                main_comment =[]
                sub_comments = []
                # parent comment
                post_comments = db['comment'].find({'id':post['id'],'parent_comment':''})
                if post_comments.count()>0:
                    for comment in post_comments:
                        comment.pop("_id")
                        comment['created'] =str(post['created'])
                        comment['modified'] =str(post['modified'])
                        # get sub-comment 
                        sub_post_comments = db['comment'].find({'parent_comment':comment['id']})
                        if sub_post_comments.count()>0:
                            for sub_comment in sub_post_comments:
                                sub_comment.pop("_id")
                                sub_comment['created'] = str(sub_comment['created'])
                                sub_comment['modified'] = str(sub_comment['modified'])
                                sub_comments.append(sub_comment)
                        # add sub comment to main comment
                        comment['sub_comment'] =sub_comments
                        # add main comment to list
                        main_comment.append(comment)
                    
                    post['comment'] = main_comment
                else:
                    main_comments['sub_comment'] = sub_comments
                    post['comment'] = main_comment
                all_post.append(post)
        return all_post


# POST
# id
# uid
# title
# name
# author
# created
# modified
# content
# excerpt{list of exludes}
# status
# post_status
# post_count
# post_parent
# mime_type{example text,video,etc}
# meta


###

####