# Python
from email.policy import default
from typing import Optional, Union

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()


# Models

class Agent(BaseModel):
    """Agent model"""
    first_name: str
    last_name: str
    userid: int
    date: str
    role: Optional[str] = None
    active: bool

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


@app.get('/users/{name}')
def query_param(name: str, age: int=None):
    user = {'user_name': name}
    if age:
       user.update({'age': age})
    return user


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    """Update endpoint"""
    return {'item_name': item.name, 'item_id': item_id}


# Request and Response body
@app.post('/agent/new')
def create_agent(agent: Agent = Body(...)):
    """Allows to create new agent"""
    return agent


# Validations query parameters
@app.get('/agent/detail')
def show_detail(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title='Person Name',
        description='This is the person name'),
    age: Optional[str] = None
):
    """Show agent details"""
    return {name: age}


# Validations Path Parameters
@app.get('/agent/detail/{user_id}')
def show_agent(
    user_id: int = Path(
        ...,
        gt=0,
        title='This is the person id',
        description='This id must be greater than 0')
):
    """Show agent detail based on id"""
    pass
