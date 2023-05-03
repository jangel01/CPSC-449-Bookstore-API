#to run this code
#uvicorn book:app --reload 

# libraries needed: Uvicorn
# pip install uvicorn


from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def index():
	return {"book": "Test page"}
