from flask import jsonify
from flask1_mongo import app
from werkzeug.wrappers import Request,Response
from flask1_mongo.user import BlacklistToken
import jwt
import datetime
from werkzeug.exceptions import Unauthorized,abort


class Middleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # not Flask request - from werkzeug.wrappers import Request
        req = Request(environ)
        if(req.path!="/login" and req.path!="/register"):
            token = None
            if 'x-access-tokens' in req.headers:
                token = req.headers['x-access-tokens']

            if not token:
                return jsonify({'message': 'a valid token is missing'})
            try:
                if not(BlacklistToken.objects(token=token)):
                    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
                    return self.app(environ, start_response)
                else:
                    print("token is Blacklisted you Hacker")
                    raise Exception
            except Exception as e:
                #print(e)
                #return Unauthorized()(environ, start_response)
                x="avcd"
                res = Response("invalid token {}".format(e), mimetype='text/plain', status=401)
                return res(environ, start_response)
        return self.app(environ, start_response)



"""if(req.path!="/login" and req.path!="/register"):
            t = req.headers['x-access-tokens']
            if not(BlacklistToken.objects(token=t)):
                return self.app(environ, start_response)
            return jsonify({'message': 'token is Blacklisted you Hacker'})
        else:
            return self.app(environ, start_response)"""

