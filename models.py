from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    author: str
    description: str
    price: float
    stock: int
    sales: int

books = {
    1: {
        "title": "My Book",
        "author" : "Someone",
        "description" : "This is a sample book",
		"price" : 1.99,
		"stock" : 10,
        "sales" : 1
    },
    2: {
        "title": "My Book2",
        "author" : "Someone2",
        "description" : "This is a sample book2",
		"price" : 2.99,
		"stock" : 20,
        "sales" : 2
    }
}