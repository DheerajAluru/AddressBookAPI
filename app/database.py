from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATA_BASE_URL="sqlite:///./addressbook2.db"

engine=create_engine(SQLALCHEMY_DATA_BASE_URL, connect_args={"check_same_thread":False})

SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

Base= declarative_base()