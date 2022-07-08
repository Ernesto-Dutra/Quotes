import os
import re
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#db configuration
##local database
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:thanos666@localhost/quotes'


  #  uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

#heroku database


app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://eiqxlrbmswjofl:9b581a895c3639239a21c39e08c365a0543032e46efbb39c6bcf06b982ce2cd1@ec2-3-222-74-92.compute-1.amazonaws.com:5432/d98s17u5iq47ki'.replace("://", "ql://", 1)
 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#sqlalchemy instance
db = SQLAlchemy(app)

class Favquotes (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    author = db.Column (db.String(20))
    quotes = db.Column (db.String(200))

#routes
@app.route('/')
def index():
    result = Favquotes.query.all()    
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quotes = request.form['quotes']
    quotedata = Favquotes(author=author, quotes=quotes)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))

#database manipulation

