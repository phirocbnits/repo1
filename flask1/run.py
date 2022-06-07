
from flask import Flask,render_template,redirect,url_for,flash, get_flashed_messages, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
import email_validator

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///flask1.db'
#for #!/usr/bin/env python3form security
#app.config['SECRET_KEY'] = '9b3eeae24ff5b6a5ca11c479'
db = SQLAlchemy(app)
#usr/<int:user_id>/
@app.route("/", methods=["GET","POST","PUT","DELETE","PATCH"])
def usr():
    if(request.method == 'GET'):
        cur = User.query.all()
        #user =cur.execute('SELECT * FROM User WHERE id = {}'.format(user_id))
        return jsonify(cur)
"""        cur = mysql.connection.cursor() 
        user =cur.execute('SELECT * FROM User WHERE id = {}'.format(user_id))
         #cur.fetchone()
        return user """

"""class RegisterForm(FlaskForm):
    def validate_email_id(self,check_email_id):
        usr = User.query.filter_by(email_id=check_email_id.data).first()
        if usr:
            raise ValidationError("mail-id already exist!!")
    name = StringField(label='Name:', validators=[Length(min=2, max=20), DataRequired()])
    email_id = StringField(label='E-mail:',validators=[Email(), DataRequired()])
    passwd1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    passwd2 = PasswordField(label='Confirm Password', validators=[EqualTo('passwd1')])
    submit = SubmitField(label='submit')"""

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    email_id = db.Column(db.String(length=50), nullable=False, unique=True)
    passwd = db.Column(db.String(length=16), nullable=False)

def __repr__(self):
    return f'User{self.name}'
#must call the main method
if __name__=='__main__':
    #execute code in debugging mode
    app.run(debug=True,port=8000)

"""@app.route("/prod")
def prod():
    return render_template("view.html")
@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        create_usr = User(name=form.name.data,email_id=form.email_id.data,passwd=form.passwd1.data)
        db.session.add(create_usr)
        db.session.commit()
        return redirect(url_for('home'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}')

    return render_template("register.html", form = form)"""






