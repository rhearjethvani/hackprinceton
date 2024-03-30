from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("localhost", 27017)

db = client["mydatabase"]
users_collection = db["users"]




# client = MongoClient("mongodb://localhost:27017/")  # your connection string
