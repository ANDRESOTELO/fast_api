# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body


app = FastAPI()


# Models

class Person(BaseModel):
    """Person model"""
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get('/api')
def home():
    """First endpoint"""
    return {'Status': 'OK',
            'message': 'API home',
            'status_code': 200}


# Request and Response body

@app.post('/person/new')
def create_person(person: Person = Body(...)):
    """Allows to create new person"""
    return person