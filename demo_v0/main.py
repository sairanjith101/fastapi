from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': "Hi"}

@app.get('/blog/unpublished')
def unpublished():
    return {"data": "This is Unpublished blogs"}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

# @app.get('/blog/{id}/comments')
# def comments(id, limit=10):
#     return {"data": {"1", "2"}}

@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10, published: bool=True):
    all_comments = ["Comment 1", "Comment 2", "Comment 3", "Comment 4", "Comment 5"]
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


