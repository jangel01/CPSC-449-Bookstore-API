from fastapi import APIRouter, Path
from database import collection
from models import Todo
from schema import todo_serializer, todos_serializer
from bson.objectid import ObjectId
from fastapi.responses import HTMLResponse

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
    return {"Results": todos}

@app_router.get("/inventory")
async def get_todos_inventory():
    #mongosh query - total titles
    #db.catalog.aggregate( [ { $match: { sales: { $gte: 0 } } }, { $count: "total books" } ] )
    #db.catalog.aggregate([{ "$group": { "_id": "$None", "total collections": { "$sum": 1 } } }])
    #pipeline = [ { "$match": { "sales": { "$gte": 0 } } }, { "$count": "total books" } ]
    #pipeline = ([{"$group": {"_id":"$None", "total collections":{"$sum": 1}}}])
    #totalBooks = collection.aggregate( pipeline )

    #mongosh query - total books
    #db.catalog.aggregate([{ $group: {_id: null, sumOfBooks: {$sum: "$stock"} }}])
    pipeline = [{ "$group": {"_id": None, "sumOfBooks": {"$sum": "$stock"} }}]

    totalBooks = collection.aggregate( pipeline )
    #return list(totalBooks)
    return list(totalBooks)

@app_router.get("/bestSeller", response_class=HTMLResponse)
async def get_todos_best_seller():

    #mongosh query for best seller
    #db.catalog.aggregate([{"$group": {"_id": "$sales", "titles": {"$push": "$title"}}}, {"$sort": {"_id" : -1}}, {"$limit" : 5}])
    #db.catalog.aggregate( [{"$unwind": "$title" }, { $group: { _id: "$sales", title: { $topN: { output: ["$title", "$sales"], sortBy: { "sale": -1 }, n : 5 } } } }, {"$sort": {"_id" : -1}}, {"$limit" : 5}])
    
    pipeline = [{"$group": {"_id": "$sales", "title": {"$push": "$title"}}}, {"$sort": {"_id" : -1}}, {"$limit" : 5}]
    bestSeller = collection.aggregate(pipeline)
    bestList = ""
    x = 1
    for item in bestSeller:
        print(item)
        bestList = bestList + str(item) + "<br>"
        x = x +1
        if (x == 5): break

    return bestList

@app_router.get("/topAuthors", response_class=HTMLResponse)
async def get_todos_top_author():
        #mongosh query for best seller
    #db.catalog.aggregate([{'$group': {'_id': '$author', 'countStock': {'$sum': "$stock"}}},{'$sort': {'countStock': -1}}, {"$limit" : 5}])
    
    pipeline = [{'$group': {'_id': '$author', 'countStock': {'$sum': "$stock"}}},{'$sort': {'countStock': -1}}, {"$limit" : 5}]
    topAuthors = collection.aggregate(pipeline)
    topList = ""
    x = 1
    for item in topAuthors:
        print(item)
        topList = topList + str(item) + "<br>"
        x = x +1
        if (x == 5): break

    return topList

@app_router.post("/books")
async def insert_book(todo: Todo):
    todo = todo.dict()
    todo = todo_serializer(collection.insert_one(dict(todo)))
    return {"data": todo}

@app_router.put("/books/{book_id}")
async def update_book(todo: Todo, book_id:str=Path(...,min_length=24, max_length=24)):
    todo = todo.dict()
    todo = todo_serializer(collection.find_one_and_update({"_id": ObjectId(book_id)}, {"$set": dict(todo)}, return_document=True))
    return {"data": todo}