from flask import jsonify,make_response
from flask1_mongo import app
from werkzeug.wrappers import Request
from flask1_mongo.user import BlacklistToken


class Middleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # not Flask request - from werkzeug.wrappers import Request
        req = Request(environ)
        # just do here everything what you need
        if(req.path!="/login" and req.path!="/register"):
            t = req.headers['x-access-tokens']
            if not(BlacklistToken.objects(token=t)):
                return self.app(environ, start_response)
            else:
                return self.app(environ, make_response('could not verify', 401, {'Authentication': 'login required"'}))
        else:
            return self.app(environ, start_response)
