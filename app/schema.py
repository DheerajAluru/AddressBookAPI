from typing import Optional
from pydantic import BaseModel

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class AddressBase(OurBaseModel):
    id : int 
    username: str
    addDesc : str
    #coordinate_add : str

class Config:
    orm_mode=True


class AddressC(OurBaseModel):

    coordinate_add : str

class Config:
    orm_mode=True


