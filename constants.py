from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json, logging
from helper import read_json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqldatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key?'
db = SQLAlchemy(app)
data = read_json()[:]
