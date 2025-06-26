from app.models import Symptom, Patient
from app.db import SessionLocal
from app.graphql.types import SymptomType, SymptomInput
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy import select

async def create_symptom(input: SymptomInput) -> SymptomType:
      try:
            async with SessionLocal() as session:
                  patient_result = await session.execute(select(Patient).where(Patient.id == input.patient_id))
                  patient = patient_result.scalars().first()
                  if not patient:
                        raise GraphQLError(f"Patient with id {input.patient_id} not found.")

                  existing = await session.execute(select(Symptom).where( Symptom.patient_id == input.patient_id, Symptom.name == input.name))
                  if existing.scalars().first():
                        raise GraphQLError("Symptom with this name already exists for this patient.")

                  symptom = Symptom(
                        patient_id=input.patient_id,
                        name=input.name,
                  )
                  session.add(symptom)
                  await session.commit()
                  await session.refresh(symptom)
                  return SymptomType(
                        id=symptom.id,
                        name=symptom.name
                  )
      except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
      except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")