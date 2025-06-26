from app.models import Medication, Patient
from app.db import SessionLocal
from app.graphql.types import MedicationType, MedicationInput
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy import select

async def create_medication(input: MedicationInput) -> MedicationType:
      try:
            async with SessionLocal() as session:
                  patient_result = await session.execute(select(Patient).where(Patient.id == input.patient_id))
                  patient = patient_result.scalars().first()
                  if not patient:
                        raise GraphQLError(f"Patient with id {input.patient_id} not found.")

                  existing = await session.execute(select(Medication).where( Medication.patient_id == input.patient_id, Medication.name == input.name))
                  if existing.scalars().first():
                        raise GraphQLError("Medication with this name already exists for this patient.")

                  medication = Medication(
                        patient_id=input.patient_id,
                        name=input.name,
                  )
                  session.add(medication)
                  await session.commit()
                  await session.refresh(medication)
                  return MedicationType(
                        id=medication.id,
                        name=medication.name
                  )
      except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
      except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")