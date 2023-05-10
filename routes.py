from fastapi import APIRouter, Path
#from fastapi.encoders import jsonable_encoder
from database import collection
from models import Todo
from schema import todo_serializer, todos_serializer
from bson.objectid import ObjectId

app_router = APIRouter()
@app_router.get("/")
def index():
	return {"book": "Root page"}

@app_router.get("/books")
async def get_todos():
    todos = todos_serializer(collection.find())
    #return {"status": "ok", "data": todos}
    return {"data": todos}

@app_router.get("/books/{book_id}")
async def get_todos_id(book_id:str=Path(...,min_length=24, max_length=24)):
    #64370af1915d810bfbe7a08e - not valid book
    #6452df1b790b5f84a6061c74 - valid book
    #db.catalog.find({ _id: "64370af1915d810bfbe7a08d"})
    todos = todos_serializer(collection.find({ "_id": ObjectId(book_id)}))
    #if (todos == )
    #return {"status": "ok", "data": todos}
    return {"Results": todos}
    #return {"Results": jsonable_encoder(todos)}