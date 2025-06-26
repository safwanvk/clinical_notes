from app.models import Patient
from app.db import SessionLocal
from app.graphql.types import (PatientType, PatientInput, PatientUpdateInput, SymptomType, MedicalHistoryType,
                               ConditionType, MedicationType)
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

async def create_patient(input: PatientInput) -> PatientType:
      try:
            async with SessionLocal() as session:
                  existing = await session.execute(select(Patient).where(Patient.name == input.name))
                  if existing.scalars().first():
                        raise GraphQLError("A patient with this name already exists.")
                  patient = Patient(
                        name=input.name,
                        gender=input.gender,
                        age=input.age,
                        blood_group=input.blood_group,
                        height_cm=input.height_cm,
                        weight_kg=input.weight_kg,
                        bmi=input.bmi,
                        bp=input.bp,
                        glucose=input.glucose,
                        heart_rate=input.heart_rate
                  )
                  session.add(patient)
                  await session.commit()
                  await session.refresh(patient)
                  return PatientType(
                        id=patient.id,
                        name=patient.name,
                        gender=patient.gender,
                        age=patient.age,
                        blood_group=patient.blood_group,
                        height_cm=patient.height_cm,
                        weight_kg=patient.weight_kg,
                        bmi=patient.bmi,
                        bp=patient.bp,
                        glucose=patient.glucose,
                        heart_rate=patient.heart_rate
                  )
      except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
      except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

async def get_patient_details(patient_id: int) -> PatientType:
      try:
            async with SessionLocal() as session:
                  stmt = select(Patient).options(
                        selectinload(Patient.symptoms),
                        selectinload(Patient.medical_history),
                        selectinload(Patient.conditions),
                        selectinload(Patient.medications)
                  ).where(Patient.id == patient_id)
                  result = await session.execute(stmt)
                  patient = result.scalars().first()
                  if not patient:
                        raise GraphQLError(f"Patient with id {patient_id} not found.")

                  return PatientType(
                        id=patient.id,
                        name=patient.name,
                        gender=patient.gender,
                        age=patient.age,
                        blood_group=patient.blood_group,
                        height_cm=patient.height_cm,
                        weight_kg=patient.weight_kg,
                        bmi=patient.bmi,
                        bp=patient.bp,
                        glucose=patient.glucose,
                        heart_rate=patient.heart_rate,
                        medical_history=[MedicalHistoryType(id=m.id, description=m.description) for m in patient.medical_history],
                        symptoms=[SymptomType(id=s.id, name=s.name) for s in patient.symptoms],
                        conditions=[ConditionType(id=c.id, name=c.name) for c in patient.conditions],
                        medications=[MedicationType(id=med.id, name=med.name) for med in patient.medications]
                  )
      except SQLAlchemyError as e:
            raise GraphQLError(f"Database error: {str(e)}")

async def update_patient_details(patient_id: int, input: PatientUpdateInput) -> PatientType:
      try:
            async with SessionLocal() as session:
                  result = await session.execute(select(Patient).where(Patient.id == patient_id))
                  patient = result.scalars().first()

                  if not patient:
                        raise GraphQLError(f"Patient with id {patient_id} not found.")

                  if input.name is not None:
                        patient.name = input.name
                  if input.gender is not None:
                        patient.gender = input.gender
                  if input.age is not None:
                        patient.age = input.age
                  if input.blood_group is not None:
                        patient.blood_group = input.blood_group
                  if input.height_cm is not None:
                        patient.height_cm = input.height_cm
                  if input.weight_kg is not None:
                        patient.weight_kg = input.weight_kg
                  if input.bmi is not None:
                        patient.bmi = input.bmi
                  if input.bp is not None:
                        patient.bp = input.bp
                  if input.glucose is not None:
                        patient.glucose = input.glucose
                  if input.heart_rate is not None:
                        patient.heart_rate = input.heart_rate

                  await session.commit()
                  await session.refresh(patient)

                  return PatientType(
                        id=patient.id,
                        name=patient.name,
                        gender=patient.gender,
                        age=patient.age,
                        blood_group=patient.blood_group,
                        height_cm=patient.height_cm,
                        weight_kg=patient.weight_kg,
                        bmi=patient.bmi,
                        bp=patient.bp,
                        glucose=patient.glucose,
                        heart_rate=patient.heart_rate
                  )
      except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
      except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")