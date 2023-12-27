CPSC 449 - Final Project

## Group Members: 
Daniel Chen Wu, Jason Angel

## Videos
https://drive.google.com/drive/folders/1J_DGsPa8FmbPkvwT4Sanxpv8uEzZOKRr

## How to run 
1. Clone the repository to your machine.
2. Create a database named 'bookstore' and a collection named 'catalog' witihn Mongo Compass. You then need to import catalog.json to the catalog collection.
3. Create and run the virtual environment (venv) within the local repository.
4. Run the following command within your venv: ```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt``` if you're on a mac. If for whatever reason this command fails, you need to inidivudally install the required packages. Again, if you're on a mac make sure to use pip3:
    - ```pip install Flask-PyMongo```
    - ```python -m pip install fastapi```
    - ```pip install uvicorn```
    - ```pip install motor```
5. To start the server run the command : ```uvicorn main:app --reload```
6. Head to http://127.0.0.1:8000/docs to test the APIs.

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
    ...
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
Paramters: You can leave all the paramters empty, search by one paramter, or by all paramters. Note that title and author values don't have to exactly match as we are using regex

--

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

--

Example 2:

Paramters: author = Someone9, minPrice = 1.0, maxPrice = 2.0

Expected Response:
```
{
  "data": [
    {
      "id": "6467e7d3bdc581f6e78220da",
      "title": "My Book10",
      "author": "Someone9",
      "description": "This is a sample book10",
      "price": 1.99,
      "stock": 10,
      "sales": 1
    }
  ]
}
```

### GET /inventory -- Get total stock of books
Paramters: none

Expected response:
```
[
  {
    "_id": null,
    "sumOfBooks": 485
  }
]
```

### GET /bestSeller -- Get top 5 best selling books
Paramters: none

Expected response:
```
{'_id': 'My Book8', 'author': ['Someone8'], 'sales': [8]}{'_id': 'My Book5', 'author': ['Someone5'], 'sales': [5]}{'_id': 'My Book6', 'author': ['Someone6'], 'sales': [5]}{'_id': 'My Book4', 'author': ['Someone4'], 'sales': [4]}{'_id': 'My Book3', 'author': ['Someone3'], 'sales': [3]}
```

## GET /topAuthors -- Get top 5 authors with most boosk in stock
Paramters: none

Expected Response:
```
{'_id': 'Someone', 'countStock': 210}{'_id': 'Someone7', 'countStock': 70}{'_id': 'Someone6', 'countStock': 50}{'_id': 'Someone5', 'countStock': 50}{'_id': 'Someone4', 'countStock': 40}
```
