from sqlalchemy import Column,Integer,String,REAL
from app.database import Base 


class Addresses(Base):
    __tablename__="details"
    id=Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    username=Column(String(50), index=True,nullable=False)
    address=Column(String(255), index=True, nullable=False)
    addDesc=Column(String, index=True)