from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient


#client = MongoClient("mongodb+srv://prince:secret@cluster0.finu.mongo.net/myFirstDatabase?retryWrites=true&w=majority")
client = MongoClient("mongodb://localhost:27017")
#client = AsyncIOMotorClient("mongodb://localhost:27017")

db = client.bookstore
collection = db.catalog

#collection_name = db("todos_app")