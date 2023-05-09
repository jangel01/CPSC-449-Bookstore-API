def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": str(todo["title"]),
        "author": str(todo["author"]),
        "description": str(todo["description"]),
        "price": float(todo["price"]),
        "stock": int(todo["stock"]),
        "sales": int(todo["sales"])
    }

def todos_serializer(todos) -> list:
    return[todo_serializer(todo) for todo in todos]