from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost/flask1_mongo'
}
app.config['SECRET_KEY']="ABC123"
db = MongoEngine(app)

from flask1_mongo import routes
