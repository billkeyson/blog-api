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

class UserModel():
    @classmethod
    def connection(cls):
        db = MongoClient(settings.DATABASE_URL,settings.DATABASE_PORT)
        return db[settings.DATABASE_NAME]
    
    @classmethod
    def add_user(cls,username,password,email,nickname,status,meta):
        users = {}
        users['uid'] = datetime.datetime.now().strftime('%Y%m%d') + \
                     uuid.uuid4().urn[9:].replace('-', '').upper()

        users['username'] = username
        users['email'] = email
        users['nickname'] = nickname
        users['status'] = status
        users['meta']= meta
        users['created'] = datetime.datetime.utcnow()
        users['modified'] = datetime.datetime.utcnow()

        if cls.connection()['users'].insert_one(users).inserted_id:
            return users
        return {}
