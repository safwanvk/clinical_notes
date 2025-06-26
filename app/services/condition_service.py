from app.models import Condition, Patient
from app.db import SessionLocal
from app.graphql.types import ConditionType, ConditionInput
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy import select

async def create_condition(input: ConditionInput) -> ConditionType:
      try:
            async with SessionLocal() as session:
                  patient_result = await session.execute(select(Patient).where(Patient.id == input.patient_id))
                  patient = patient_result.scalars().first()
                  if not patient:
                        raise GraphQLError(f"Patient with id {input.patient_id} not found.")

                  existing = await session.execute(select(Condition).where( Condition.patient_id == input.patient_id, Condition.name == input.name))
                  if existing.scalars().first():
                        raise GraphQLError("Condition with this name already exists for this patient.")

                  condition = Condition(
                        patient_id=input.patient_id,
                        name=input.name,
                  )
                  session.add(condition)
                  await session.commit()
                  await session.refresh(condition)
                  return ConditionType(
                        id=condition.id,
                        name=condition.name
                  )
      except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
      except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")