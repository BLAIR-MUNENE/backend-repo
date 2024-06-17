from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.events import Event
from models.bookings import Booking
from models.myevents import MyEvents
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(CORSMiddleware,allow_origins = ["*"],allow_credentials = True,allow_methods = ["*"] ,allow_headers = ["*"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
 
@app.get('/myevents')
def myevents():
    myevents = MyEvents.find_all
    return myevents


@app.get('/events')
def events():
    events = Event.find_all()
    return events


class BookingModel(BaseModel):
    name : str
    age : int
    phoneNumber : int
    email : str
    Paymentdetails : str
@app.post("/booking")
def save_booking(data: BookingModel):
    booking = Booking(data.name,data.age,data.phoneNumber,data.email,data.Paymentdetails )
    booking.save()
    return booking.to_dict()
    
    
