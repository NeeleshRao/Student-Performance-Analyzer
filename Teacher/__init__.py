from flask import Flask, render_template, redirect, current_app
from flask_sqlalchemy import SQLAlchemy
import os, pytest
from flask_login import LoginManager
import pymysql

secret_key = os.urandom(32)

app = Flask(__name__)
        
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key
app.config['UPLOAD_FOLDER'] = "C:/Users/Neelesh Thonse Rao/Desktop/programming/Student Performance Analyzer/after cie/nextone/Teacher/static/uploads/"
app.config['SAMPLES_FOLDER'] = "C:/Users/Neelesh Thonse Rao/Desktop/programming/Student Performance Analyzer/after cie/nextone/Teacher/static/samples/"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from Teacher import routes
