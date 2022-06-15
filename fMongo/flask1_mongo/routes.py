from flask import Flask,jsonify,request,make_response
#from werkzeug.security import generate_password_hash
import jwt
import datetime
from flask_restful import Api,Resource
from flask1_mongo.user import User,BlacklistToken
from flask1_mongo.tokens import token_required
from flask1_mongo import app,db
from base64 import b64decode
from flask1_mongo.middleware import Middleware

def dictify(u):
    return {"id":u.id, "name":u.name, "email_id":u.email_id, "passwd":u.passwd}



#register a user
#insert a user ... returns user details
class signup_usr(Resource):
    def post(self): 
        try:
            data = request.get_json()
            new_user = User(**data).save()
            u=User.objects(email_id=data["email_id"])
            d=list(map(dictify,u))
            response = jsonify({"registered users":u})
            response.status_code = 200 # or 400 or whatever
            return response

        except:
            return make_response('could not verify', 401, {'response': 'error'})


class login_user(Resource):
    def post(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password: 
            return make_response('could not verify', 401, {'Authentication': 'login required"'})   
        user = User.objects.get(name=auth.username.strip())
        if (user.passwd==auth.password):
            run_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=500)
            token = jwt.encode({'email_id':user.email_id, 'exp' :run_at}, app.config['SECRET_KEY'])
            return jsonify({'token' : token})
        return make_response('could not verify',  401, {'Authentication': '"login required"'})

class home(Resource):
    @token_required
    def get(self):
        #returns all users' details
        u=User.objects()
        d=list(map(dictify,u))
        response = jsonify({"users":u})
        response.status_code = 200 # or 400 or whatever
        return response
    
    #edit an attribute for a user... returns user details
    def put(self):
        bar = request.get_json()
        admin = User.objects(email_id = bar['email_id']).first().update(bar)
        u = User.objects(email_id = bar['email_id']).first()
        response = jsonify(dictify(u))
        response.status_code = 201 # or 400 or whatever
        return response
    #edit all details for a user ... returns user details
    def patch(self):
        bar = request.get_json()
        admin = User.objects(email_id = bar['email_id']).first().update(bar)
        u = User.objects(email_id = bar['email_id']).first()
        response = jsonify(dictify(u))
        response.status_code = 201 # or 400 or whatever
        return response

class details(Resource):

    @token_required
    def get(self,id):
        u = User.objects(id=id).first()
        response = jsonify(u)
        response.status_code = 200 # or 400 or whatever
        return response
    #delete a user by id
    def delete(self,id):
        print(id)
        user = User.objects(id=id).first()
        user.delete()
        return 'successfully deleted', 200

class logout(Resource):
    def post(self):
        token = request.headers['x-access-tokens']
        BlacklistToken(token=token).save()
api = Api(app)

api.add_resource(signup_usr, '/register')
api.add_resource(login_user, '/login')
api.add_resource(logout, '/logout')

app.wsgi_app = Middleware(app.wsgi_app)
#api1 = Api(app)"""

api.add_resource(home, '/')
api.add_resource(details,'/details/<id>')
