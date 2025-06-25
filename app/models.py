from sqlalchemy import Column, Integer, String, Float
from app.base import Base

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    age = Column(Integer)
    blood_group = Column(String)
    height_cm = Column(Integer)
    weight_kg = Column(Integer)
    bmi = Column(Float)
    bp = Column(String)
    glucose = Column(Integer)
    heart_rate = Column(Integer)