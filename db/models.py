from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    available = Column(Boolean, default=True)
    rating = Column(Float, default=5.0)

class Ride(Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    driver_id = Column(Integer)
    vehicle_type = Column(String)
    destination_x = Column(Integer)
    destination_y = Column(Integer)
    fare = Column(Float)
    status = Column(String)
