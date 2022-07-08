# Python
from typing import Optional, Union

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

class Item(BaseModel):
    """Item Model"""
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get('/')
def home():
    """API endpoint"""
    return {'Message': 'Welcome to the API - Everything is OK'}


@app.get('/status')
def status():
    """Status endpoint"""
    return {'Status': 'OK',
            'message': 'API status',
            'status_code': 200}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    """URL Params"""
    return {'item_id': item_id, 'q': q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    """Update endpoint"""
    return {'item_name': item.name, 'item_id': item_id}


# Request and Response body
@app.post('/person/new')
def create_person(person: Person = Body(...)):
    """Allows to create new person"""
    return person
