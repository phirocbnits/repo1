from flask import Flask,render_template
from flask-sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    """create a template folder parallel to this file and keep index.html inside template folder.
       import render_template and return it from the needed route"""
    #return render_template("index.html")
    return "<p>Hello, World!</p>"
@app.route("/prod")
def prod():
    return "<p>Hello, from products!</p>"
#must call the main method
if __name__=="__main__":
    #execute code in debugging mode
    app.run(debug=True,port=8000)

###to show variables in html###  => jinja code
#......return render_template("index.html",arg1=varname) =>in .py file
#......{{arg1}} -> put variable name in html =>in .html
#......{%for x in arg1%}html code{%endfor%} =>in .html

###html inheritance###
#make a base. html file and keep the contents like nav foot int that needed in every page
#{%extends base.html%} =>every other html file

###for putting a different block of code in every page at the same place###
#{block <blockName>} {endblock} =>in base.html
#{block <blockName>}html code{endblock}=> in other html files

###for navigating to pages###
#....<a href="{{url_for('prod')}}"> home<a>

