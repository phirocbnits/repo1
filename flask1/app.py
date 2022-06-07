from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:root@localhost/flask1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY'] = '9b3eeae24ff5b6a5ca11c479'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    email_id = db.Column(db.String(length=50), nullable=False, unique=True)
    passwd = db.Column(db.String(length=16), nullable=False)
    def __init__(self,name,email_id,passwd):
        self.name=name
        self.email_id=email_id
        self.passwd=passwd
def __repr__(self):
        return f'User{self.name}'
def dictify(u):
    return {"id":u.id, "name":u.name, "email_id":u.email_id, "passwd":u.passwd}
@app.route("/", methods=["GET", "POST", "PUT", "PATCH"])
def home():
    if request.method == "GET" :
        u=User.query.all()
        d=list(map(dictify,u))
        response = jsonify({"users":d})
        response.status_code = 200 # or 400 or whatever
        return response
    if request.method == "POST" :
        bar = request.get_json()
        db.session.add(User(name=bar['name'],email_id=bar['email_id'],passwd=bar['passwd']))
        db.session.commit()
        return 'successfully inserted', 201
    if request.method == "PUT" :
        bar = request.get_json()
        admin = User.query.filter_by(id = bar['id']).update(bar)
        db.session.commit()
        return 'successfully updated', 201
    if request.method == "PATCH" :
        bar = request.get_json()
        admin = User.query.filter_by(id = bar['id']).update(bar)
        db.session.commit()
        return 'successfully updated', 201
@app.route("/details/<id>", methods=["GET", "DELETE"])
def details(id):
    if request.method == "GET" :
        u = User.query.filter_by(id = id).first()
        response = jsonify(dictify(u))
        response.status_code = 200 # or 400 or whatever
        return response
    if request.method == "DELETE" :
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return 'successfully deleted', 200

if __name__=='__main__':
    app.run(debug=True)

