from operator import gt
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()
class Article(BaseModel):
    id: int
    title: str
    description: str

class NewEmployee(BaseModel):
    emp_id: int
    name: str
    age: int = Body(None, gt=18)
    teams: list

@app.post('/article/')
def add_article(article: Article):
    return article


@app.post("/add_employee")
def add_employee(employee: NewEmployee):
    new_employee = NewEmployee(emp_id=employee.emp_id, 
                            name=employee.name, age = employee.age, teams = employee.teams )
    
    new_employee.save()
    return {"message": "Employee added successfully."}



