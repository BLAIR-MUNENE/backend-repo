from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
 
@app.get('/now')
def now():
    return [{"name" :"blair"}]