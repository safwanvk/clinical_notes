from app.models import MedicalHistory, Patient
from app.db import SessionLocal
from app.graphql.types import MedicalHistoryInput, MedicalHistoryType
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy import select

async def create_medical_history(input: MedicalHistoryInput) -> MedicalHistoryType:
      try:
            async with SessionLocal() as session:
                  patient_result = await session.execute(select(Patient).where(Patient.id == input.patient_id))
                  patient = patient_result.scalars().first()
                  if not patient:
                        raise GraphQLError(f"Patient with id {input.patient_id} not found.")

                  existing = await session.execute(select(MedicalHistory).where(MedicalHistory.patient_id == input.patient_id, MedicalHistory.description == input.description))
                  if existing.scalars().first():
                        raise GraphQLError("Medical history with this description already exists for this patient.")

                  medical_history = MedicalHistory(
                        patient_id=input.patient_id,
                        description=input.description,
                  )
                  session.add(medical_history)
                  await session.commit()
                  await session.refresh(medical_history)
                  return MedicalHistoryType(
                        id=medical_history.id,
                        description=medical_history.description
                  )
      except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
      except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")