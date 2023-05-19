# CPSC 449 - Final Project

## Group Members: 
Daniel Chen Wu, Jason Angel

## How to run 
1. Clone the repository to your machine.
2. Create a database named 'bookstore' and a collection named 'catalog' witihn Mongo Compass. You then need to import catalog.json to the catalog collection.
3. Create and run the virtual environment (venv) within the local repository
4. Run the following command with your venv: ```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt``` if you're on a mac. If for whatever reason this command fails, you need to inidivudally install the required packages. Again, if you're on a mac make sure to use pip3:
    - ```pip install Flask-PyMongo```
    - ```python -m pip install fastapi```
    - ```pip install uvicorn```
    - ```pip install motor```
5. Head to http://127.0.0.1:8000/docs to test the API

## Testing APIs

