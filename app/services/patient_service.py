from app.models import Patient
from app.db import SessionLocal
from app.graphql.types import (PatientType, PatientInput, PatientUpdateInput, ResponsePatientType)
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.graphql.utilities import serialize_patient, serialize_response_patient

class PatientService:
      def __init__(self, session: AsyncSession):
            self.session = session

      async def create_patient(self, input: PatientInput) -> ResponsePatientType:
            try:
                  existing = await self.session.execute(select(Patient).where(Patient.name == input.name))
                  if existing.scalars().first():
                        raise GraphQLError("A patient with this name already exists.")
                  patient = Patient(**input.to_pydantic().dict())
                  self.session.add(patient)
                  await self.session.commit()
                  await self.session.refresh(patient)
                  return serialize_response_patient(patient)
            except SQLAlchemyError as e:
                  raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
            except Exception as e:
                  raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

      async def update_patient_details(self, patient_id: int, input: PatientUpdateInput) -> ResponsePatientType:
            try:
                  result = await self.session.execute(select(Patient).where(Patient.id == patient_id))
                  patient = result.scalars().first()

                  if not patient:
                        raise GraphQLError(f"Patient with id {patient_id} not found.")

                  for field in input.__annotations__:
                        value = getattr(input, field)
                        if value is not None:
                              setattr(patient, field, value)

                  await self.session.commit()
                  await self.session.refresh(patient)

                  return serialize_response_patient(patient)
            except SQLAlchemyError as e:
                  raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
            except Exception as e:
                  raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

      async def get_patient_details(self, patient_id: int) -> PatientType:
            try:
                  stmt = select(Patient).options(
                        selectinload(Patient.symptoms),
                        selectinload(Patient.medical_history),
                        selectinload(Patient.conditions),
                        selectinload(Patient.medications),
                        selectinload(Patient.clinical_findings)
                  ).where(Patient.id == patient_id)
                  result = await self.session.execute(stmt)
                  patient = result.scalars().first()
                  if not patient:
                        raise GraphQLError(f"Patient with id {patient_id} not found.")

                  return serialize_patient(patient)
            except SQLAlchemyError as e:
                  raise GraphQLError(f"Database error: {str(e)}")