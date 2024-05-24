from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

#Path Operation
@app.get('/') #decorator
async def root(): #Asynchronous call
    return {'message': 'Hello Worlds'}

@app.get('/posts') 
def get_posts(): 
    return {'message': 'get_posts'}


@app.post('/posts')
def create_posts(post:Post):
    print(post.rating)
    return {'message': 'successfully created post'}