from fastapi import APIRouter, Path
from database import collection
from models import Todo
from schema import todo_serializer, todos_serializer
from bson.objectid import ObjectId
from fastapi.responses import HTMLResponse
from fastapi import HTTPException, status

app_router = APIRouter()
@app_router.get("/")
def index():
	return {"book": "Root page"}

# get all books
@app_router.get("/books")
async def get_todos():
    todos = todos_serializer(collection.find())
    return {"data": todos}

# get book by id
@app_router.get("/books/{book_id}")
async def get_todos_id(book_id:str=Path(...,min_length=24, max_length=24)):
    todos = todos_serializer(collection.find({ "_id": ObjectId(book_id)}))
    return {"Results": todos}

# get total stock of books
@app_router.get("/inventory")
async def get_todos_inventory():
    pipeline = [{ "$group": {"_id": None, "sumOfBooks": {"$sum": "$stock"} }}]

    totalBooks = collection.aggregate( pipeline )
    return list(totalBooks)

# get top 5 best seller books
@app_router.get("/bestSeller", response_class=HTMLResponse)
async def get_todos_best_seller():
    pipeline = [{"$group": {"_id": "$title", "author": {"$push": "$author"}, "sales": {"$push": "$sales"}}}, {"$sort": {"sales" : -1}}, {"$limit" : 5}]
    bestSeller = collection.aggregate(pipeline)
    bestList = ""
    x = 1
    for item in bestSeller:
        bestList = bestList + str(item)
        if (x == 5): break
        else: x = x + 1

    return bestList

# get top 5 authors with most books
@app_router.get("/topAuthors", response_class=HTMLResponse)
async def get_todos_top_author():
    pipeline = [{'$group': {'_id': '$author', 'countStock': {'$sum': "$stock"}}},{'$sort': {'countStock': -1}}, {"$limit" : 5}]
    topAuthors = collection.aggregate(pipeline)
    topList = ""
    x = 1
    for item in topAuthors:
        topList = topList + str(item)
        if (x == 5): break
        else:  x = x +1

    return topList

# insert book
@app_router.post("/books")
async def insert_book(todo: Todo):
    todo = todo.dict()
    todo = collection.insert_one(todo)
    todo = todo_serializer(collection.find_one({"_id": todo.inserted_id}))
    return {"data": todo}

# update book by id
@app_router.put("/books/{book_id}")
async def update_book(todo: Todo, book_id:str=Path(...,min_length=24, max_length=24)):
    todo = todo.dict()
    todo = collection.find_one_and_update({"_id": ObjectId(book_id)}, {"$set": todo}, return_document=True)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    todo = todo_serializer(todo)
    return {"data": todo}

# delete book by id
@app_router.delete("/books/{book_id}")
async def delete_book(book_id:str=Path(...,min_length=24, max_length=24)):
    todo = collection.find_one({"_id": ObjectId(book_id)})
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    collection.delete_one({"_id": ObjectId(book_id)})
    return {"data": todo}

# search book by title, author, minPrice, maxPrice
@app_router.get("/search")
async def search_book(title: str, author: str, minPrice: float, maxPrice: float):
    todo = todos_serializer(collection.find({"title": title, "author": author, "price": {"$gte": minPrice, "$lte": maxPrice}}))
    return {"data": todo}
