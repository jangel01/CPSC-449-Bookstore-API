from fastapi import APIRouter
from database import collection
from models import Todo
from schema import todo_serializer, todos_serializer

todo_api_router = APIRouter()
#retrieve
@todo_api_router.get("/")
def index():
	return {"book": "Root page"}

@todo_api_router.get("/all")
async def get_todos():
    #todos = todos_serializer(collection.find())
    todos = todos_serializer(collection.find())
    return {"status": "ok", "data": todos}

