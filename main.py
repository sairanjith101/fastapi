from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": 'blog list'}

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



# uvicorn main:app ==> uvicorn filename.py(main):object(app)
# @app - path operation decorator
# .get - operation
# ('/') - path or end points
# def fuct all - path operation function
# it is interpreator. so path type panrapa orderwise than pannanum.
# unpublish first path ahh vatha outpu varum. andha function ahh last ahh vachu run panna type error varum bcz iterpretor.
# enpoint = swaggler ui {doc} or redocs {redoc}. testing and read panna use pannalam
