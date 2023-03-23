import uvicorn
from fastapi import FastAPI, status, HTTPException, Depends 
from fastapi.middleware.cors import CORSMiddleware
import fastapi.responses as rep
import os
from app.database import engine, SessionLocal , Base
from sqlalchemy.orm import Session
import app.schema as schema
import app.models as models
from typing import List
import re
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import great_circle
from geopy.distance import distance
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


geolocator = Nominatim(user_agent="address book API")

app = FastAPI(title="Address Book API",
              debug=True)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# origins = [
#     'http://localhost:3000'
# ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)

@app.get("/")
def root():
    return "Root"
 
@app.post("/details",response_model=schema.AddressBase, status_code=status.HTTP_201_CREATED)
def create_details(details: schema.AddressBase, session: Session = Depends(get_session)):

    coor=schema.AddressC
    
    location = geolocator.geocode(details.addDesc)
    coordinate_list=[location.latitude, location.longitude]
    coordinate_list2=[str(a) for a in coordinate_list]
    schema.AddressC.coordinate_add=', '.join(coordinate_list2)
    addressDB = models.Addresses(username=details.username,address=schema.AddressC.coordinate_add,addDesc=details.addDesc)
    
    session.add(addressDB)
    session.commit()
    session.refresh(addressDB)
 
    return addressDB
 
@app.get("/details/{id}", response_model=schema.AddressBase)
def read_details(id: int, session: Session = Depends(get_session)):

    get_ID = session.query(models.Addresses).get(id)
    if not get_ID:
        raise HTTPException(status_code=404, detail=f"Details with ID {id} not found")
 
    return get_ID
 
@app.put("/details/{id}", response_model=schema.AddressBase)
def update_details(id: int, username: str, addDesc:str, session: Session = Depends(get_session)):


    coor=schema.AddressC
    
    get_ID = session.query(models.Addresses).get(id)
    if get_ID:
        get_ID.username = username
        get_ID.addDesc=addDesc
        location = geolocator.geocode(addDesc)
        coordinate_list=[location.latitude, location.longitude]
        coordinate_list2=[str(a) for a in coordinate_list]
        coor.coordinate_add=', '.join(coordinate_list2)
        get_ID.address=coor.coordinate_add
        session.commit()
 
    # check if id exists. If not, return 404 not found response
    if not get_ID:
        raise HTTPException(status_code=404, detail=f"Details with ID {id} not found")
 
    return get_ID
 
@app.delete("/details/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_details(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    get_ID = session.query(models.Addresses).get(id)
 
    # if  item with given id exists, delete it from the database. Otherwise raise 404 error
    if get_ID:
        session.delete(get_ID)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Details with ID {id} not found")
 
    return None
 
@app.get("/details", response_model = List[schema.AddressBase])
def read_details_list(session: Session = Depends(get_session)):
 
    details_list = session.query(models.Addresses).all() 
 
    return details_list 



@app.post("/details/{address}", response_model = schema.AddressBase)
def read_coordinates(address:str, session: Session = Depends(get_session)):

    #get_add1=session.query(models.Addresses.address).get(address)
    get_add1 = session.query(models.Addresses).filter(models.Addresses.address==address).first()

    if not get_add1:
        raise HTTPException(status_code=404, detail=f"Details with Address {address} not found")


    return get_add1


@app.get("/range/{address}")
def get_cord_range(lat:float,long:float, session: Session = Depends(get_session)):

    lat_longList=[]
    ranges=[]

    details_list = session.query(models.Addresses.address).all()

    json_compatible_data = jsonable_encoder(details_list)
    
    for index in range(len(json_compatible_data)):
        for key in json_compatible_data[index]:
            lat_longList.append(json_compatible_data[index][key])
    lat_long_input=(lat,long)
    print(lat_long_input)
    for i in lat_longList:
        if distance(lat_long_input,i).km<1:
            ranges.append(i)
    
    final_list=[]
    for i in range(len(ranges)):
        location = geolocator.reverse(ranges[i])
        final_list.append(location)

    return final_list






