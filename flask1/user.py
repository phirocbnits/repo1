from app import db
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