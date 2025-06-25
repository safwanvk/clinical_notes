from app.models import Patient
from app.db import SessionLocal
from app.graphql.types import PatientType, PatientInput
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy import select

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
      async with SessionLocal() as session:
            patient = await session.get(Patient, patient_id)
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
                  heart_rate=patient.heart_rate
            )