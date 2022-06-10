from flask import Flask,jsonify,request,make_response
#from werkzeug.security import generate_password_hash
import jwt
import datetime
from flask1_mongo.user import User,BlacklistToken
from flask1_mongo.tokens import token_required
from flask1_mongo import app,db
from base64 import b64decode
from apscheduler.schedulers.blocking import BlockingScheduler

def dictify(u):
    return {"id":u.id, "name":u.name, "email_id":u.email_id, "passwd":u.passwd}

#register a user
#insert a user ... returns user details
@app.route('/register', methods=['POST'])
def signup_usr(): 
#    try:
    data = request.get_json()
    new_user = User(**data).save()
    return jsonify(new_user), 201
"""    db.session.add(new_user) 
    db.session.commit()   
    
    u = User.query.filter_by(email_id = data['email_id']).first()
    response = jsonify(dictify(u))
    response.status_code = 201 # or 400 or whatever
    return data
#    except:
#       return make_response('could not verify', 401, {'response': 'error'})"""
def blacklisting(token):
    b=BlacklistToken(token=token)
    db.session.add(b) 
    db.session.commit()

@app.route('/login', methods=['POST']) 
def login_user():
   auth = request.authorization  
   if not auth or not auth.username or not auth.password: 
       return make_response('could not verify', 401, {'Authentication': 'login required"'})   
 
   user = User.query.filter_by(name=auth.username.strip()).first()  
   if (user.passwd==auth.password):
    sched = BlockingScheduler()
    run_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
    #delay = (run_at - datetime.datetime.utcnow()).total_seconds()
    token = jwt.encode({'id':user.id, 'exp' :run_at}, app.config['SECRET_KEY'])
    sched.add_job(blacklisting, run_date=run_at,args=[token])
    return jsonify({'token' : token})
   return make_response('could not verify',  401, {'Authentication': '"login required"'})
""""""

@app.route("/", methods=["GET", "PUT", "PATCH"])
@token_required
def home(current_user):
    #returns all users' details
    if request.method == "GET" :
        u=User.query.all()
        d=list(map(dictify,u))
        response = jsonify({"users":d})
        response.status_code = 200 # or 400 or whatever
        return response
    
    #edit an attribute for a user... returns user details
    if request.method == "PUT" :
        bar = request.get_json()
        admin = User.query.filter_by(id = bar['id']).update(bar)
        db.session.commit()
        u = User.query.filter_by(id = bar['id']).first()
        response = jsonify(dictify(u))
        response.status_code = 201 # or 400 or whatever
        return response
    #edit all details for a user ... returns user details
    if request.method == "PATCH" :
        bar = request.get_json()
        admin = User.query.filter_by(id = bar['id']).update(bar)
        db.session.commit()
        u = User.query.filter_by(id = bar['id']).first()
        response = jsonify(dictify(u))
        response.status_code = 201 # or 400 or whatever
        return response
@app.route("/details/<id>", methods=["GET", "DELETE"])
@token_required
def details(current_user,id):
    #view details of a user by id
    if request.method == "GET" :
        #to decode base64 encoded data...recieved id will be encoded in base64 format
        id= int(b64decode(id))
        print(id)
        u = User.query.filter_by(id = id).first()
        response = jsonify(dictify(u))
        response.status_code = 200 # or 400 or whatever
        return response
    #delete a user by id
    if request.method == "DELETE" :
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return 'successfully deleted', 200