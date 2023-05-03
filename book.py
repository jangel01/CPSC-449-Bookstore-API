#to run this code
#uvicorn book:app --reload 

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def index():
	return {"book": "Test page"}
