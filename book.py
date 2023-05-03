# create a new VENV
# python -m venv /path/to/new/virtual/environment

#to run this code
#uvicorn book:app --reload 

# libraries needed:
# Uvicorn
# pip install uvicorn

# mongoDB
# https://csufullerton.instructure.com/courses/3356200/discussion_topics/20522290
# pip install Flask-PyMongo

#motor
# pip install motor

from fastapi import FastAPI
from pydantic import BaseModel
#mongoDB
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
#from motor.motor_asyncio import AsyncIOMotorClient

from flask import jsonify

app = FastAPI()

books = {
    1: {
        "title": "My Book",
        "author" : "Someone",
        "description" : "This is a sample book",
		"price" : 1.99,
		"stock" : 100,
        "sales" : 1
    }
}

class Book (BaseModel):
    title: str
    author: str
    description: str
    price: float
    stock: int

#initialize MongoDB
#mongo_client = AsyncIOMotorClient("mongodb://localhost:27017")
#db = mongo_client["bookstore"]
#collection = db["catalog"]

@app.get("/")
def index():
	return {"book": "Test page"}

@app.post("/all")
async def all_data():
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client["bookstore"]
    collection = db['bookstore']
    cursor = collection.find({})
    for document in cursor:
          print(document)