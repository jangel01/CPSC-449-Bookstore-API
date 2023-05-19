# CPSC 449 - Final Project

## Group Members: 
Daniel Chen Wu, Jason Angel

## How to run 
1. Clone the repository to your machine.
2. Create a database named 'bookstore' and a collection named 'catalog' witihn Mongo Compass. You then need to import catalog.json to the catalog collection.
3. Create and run the virtual environment (venv) within the local repository.
4. Run the following command within your venv: ```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt``` if you're on a mac. If for whatever reason this command fails, you need to inidivudally install the required packages. Again, if you're on a mac make sure to use pip3:
    - ```pip install Flask-PyMongo```
    - ```python -m pip install fastapi```
    - ```pip install uvicorn```
    - ```pip install motor```
5. Head to http://127.0.0.1:8000/docs to test the APIs.

## Testing APIs
### GET /books -- Retrieve all books
Paramters: None

Expected Response:
```
{
  "data": [
    {
      "id": "6452df1b790b5f84a6061c74",
      "title": "My Book",
      "author": "Someone",
      "description": "This is a sample book",
      "price": 1.99,
      "stock": 10,
      "sales": 1
    },
    {
      "id": "64597fef66b96d943c73403e",
      "title": "My Book2",
      "author": "Someone",
      "description": "This is a sample book2",
      "price": 2.99,
      "stock": 200,
      "sales": 2
    },
    {
      "id": "645c0982e749dae0b40a1fd4",
      "title": "My Book3",
      "author": "Someone3",
      "description": "This is a sample book3",
      "price": 3.99,
      "stock": 30,
      "sales": 3
    },
    {
      "id": "645c0996e749dae0b40a1fd6",
      "title": "My Book4",
      "author": "Someone4",
      "description": "This is a sample book4",
      "price": 4.99,
      "stock": 40,
      "sales": 4
    },
    {
      "id": "645c09a9e749dae0b40a1fd8",
      "title": "My Book5",
      "author": "Someone5",
      "description": "This is a sample book5",
      "price": 5.99,
      "stock": 50,
      "sales": 5
    },
    {
      "id": "645c1505e749dae0b40a1fda",
      "title": "My Book6",
      "author": "Someone6",
      "description": "This is a sample book6",
      "price": 6.99,
      "stock": 50,
      "sales": 5
    },
    {
      "id": "645c16a5e749dae0b40a1fdc",
      "title": "My Book7",
      "author": "Someone7",
      "description": "This is a sample book7",
      "price": 7.99,
      "stock": 70,
      "sales": 2
    },
    {
      "id": "645c16bde749dae0b40a1fde",
      "title": "My Book8",
      "author": "Someone8",
      "description": "This is a sample book8",
      "price": 2.99,
      "stock": 20,
      "sales": 8
    },
    {
      "id": "645c18cbe749dae0b40a1fe0",
      "title": "My Book9",
      "author": "Someone9",
      "description": "This is a sample book9",
      "price": 2.99,
      "stock": 0,
      "sales": 0
    },
    {
      "id": "6467e7d3bdc581f6e78220da",
      "title": "My Book10",
      "author": "Someone9",
      "description": "This is a sample book10",
      "price": 1.99,
      "stock": 10,
      "sales": 1
    },
    {
      "id": "6467e815bdc581f6e78220db",
      "title": "My Book11",
      "author": "Someone9",
      "description": "This is a sample book11",
      "price": 0.99,
      "stock": 5,
      "sales": 0
    }
  ]
}
```

### GET /books/{book_id} -- Retrieves a specific book by ID
Paramters: 24 character string (e.g 6467e815bdc581f6e78220db) 

Expected Response: 
```
{
  "Results": [
    {
      "id": "6467e815bdc581f6e78220db",
      "title": "My Book11",
      "author": "Someone9",
      "description": "This is a sample book11",
      "price": 0.99,
      "stock": 5,
      "sales": 0
    }
  ]
}
```
### POST /books -- Add a new book to the store
Paramters: None

Request Body:
```
{
  "title": "My Book12",
  "author": "Someone10",
  "description": "This is a sample book 12",
  "price": 9.99,
  "stock": 10,
  "sales": 2
}
```

Expected Response:
```
{
  "data": {
    "id": "646803e05a4d484aaea8ded8",
    "title": "My Book12",
    "author": "Someone10",
    "description": "This is a sample book 12",
    "price": 9.99,
    "stock": 10,
    "sales": 2
  }
}
```

### PUT /books/{book_id} - Update an existing book by ID
Paramters: 24 character string (e.g 646803e05a4d484aaea8ded8)

Request Body:
```
{
  "title": "My Book12",
  "author": "Someone10",
  "description": "This is an updated sample book 12",
  "price": 0,
  "stock": 0,
  "sales": 0
}
```

Expected Response:
```
{
  "data": {
    "id": "646803e05a4d484aaea8ded8",
    "title": "My Book12",
    "author": "Someone10",
    "description": "This is an updated sample book 12",
    "price": 0,
    "stock": 0,
    "sales": 0
  }
}
```

### DELETE /books/{book_id} -- Delete a book from the store by ID
Paramters: 24 character string (e.g 646803e05a4d484aaea8ded8)

Expected Response (shows deleted book):
```
{
  "data": {
    "id": "646803e05a4d484aaea8ded8",
    "title": "My Book12",
    "author": "Someone10",
    "description": "This is an updated sample book 12",
    "price": 0,
    "stock": 0,
    "sales": 0
  }
}
```

### GET /search?title={}&author={}&min_price={}&max_price={} -- Search by title, author, minimum price, and maximum price
Paramters: You can leave all the paramters empty, search by one paramter, or by all paramters

Example 1:

Paramters: author = Someone9

Expected Response:
```
{
  "data": [
    {
      "id": "645c18cbe749dae0b40a1fe0",
      "title": "My Book9",
      "author": "Someone9",
      "description": "This is a sample book9",
      "price": 2.99,
      "stock": 0,
      "sales": 0
    },
    {
      "id": "6467e7d3bdc581f6e78220da",
      "title": "My Book10",
      "author": "Someone9",
      "description": "This is a sample book10",
      "price": 1.99,
      "stock": 10,
      "sales": 1
    },
    {
      "id": "6467e815bdc581f6e78220db",
      "title": "My Book11",
      "author": "Someone9",
      "description": "This is a sample book11",
      "price": 0.99,
      "stock": 5,
      "sales": 0
    }
  ]
}
```
