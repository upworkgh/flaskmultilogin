from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jake:password@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'Thisisasecret'


Bootstrap(app)
db = SQLAlchemy(app)

from app.master.views import m
from app.webaccount.views import w 


app.register_blueprint(master.views.m, url_prefix='/master')
app.register_blueprint(webaccount.views.w, url_prefix='/webaccount')

db.create_all()