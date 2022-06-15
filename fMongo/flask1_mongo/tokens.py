from flask import Flask,jsonify,request,make_response,request
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
import jwt
import datetime
from flask1_mongo.user import User
from flask1_mongo import app

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        #try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        current_user = User.objects(email_id=data['email_id'])

        """except:
        return jsonify({'message': 'token is invalid'})"""
        return f(current_user, *args, **kwargs)
    return decorator