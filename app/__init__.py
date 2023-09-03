import os
from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo

load_dotenv()
app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)