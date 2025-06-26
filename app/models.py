from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
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

    symptoms = relationship("Symptom", back_populates="patient")
    medical_history = relationship("MedicalHistory", back_populates="patient")
    conditions = relationship("Condition", back_populates="patient")

class Symptom(Base):
    __tablename__ = 'symptoms'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship("Patient", back_populates="symptoms")

class MedicalHistory(Base):
    __tablename__ = 'medical_history'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship("Patient", back_populates="medical_history")

class Condition(Base):
    __tablename__ = 'conditions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship("Patient", back_populates="conditions")