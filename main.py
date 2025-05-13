from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"data": 'blog list'}

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    publoshed: Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data': f"Blog is created with title as {blog.title}"}

# Chnage port 8000 to 9000
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port= 9000)

# uvicorn main:app ==> uvicorn filename.py(main):object(app)
# @app - path operation decorator
# .get - operation
# ('/') - path or end points
# def fuct all - path operation function
# it is interpreator. so path type panrapa orderwise than pannanum.
# unpublish first path ahh vatha outpu varum. andha function ahh last ahh vachu run panna type error varum bcz iterpretor.
# enpoint = swaggler ui {doc} or redocs {redoc}. testing and read panna use pannalam
