from fastapi import FastAPI
from models.events import Event
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
 
@app.get('/events')
def events():
    events = Event.find_all()
    return events