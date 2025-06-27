from app.models import Patient
from app.db import SessionLocal
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

class BasePatientService:
      model = None
      type_cls = None
      unique_fields = []
      response_fields = []
      base_fields = ["patient_id"]

      async def validate_patient(self, patient_id: int, session: AsyncSession):
            result = await session.execute(select(Patient).where(Patient.id == patient_id))
            if not result.scalars().first():
                  raise GraphQLError(f"Patient with id {patient_id} not found.")

      async def create_or_update(self, input_data: dict, session: AsyncSession):
            try:
                  await self.validate_patient(input_data["patient_id"], session)

                  filters = [getattr(self.model, field) == input_data[field] for field in self.unique_fields + self.base_fields if field in input_data]
                  result = await session.execute(select(self.model).where(*filters))
                  instance = result.scalars().first()

                  if instance:
                        # Update all fields (or just relevant ones)
                        for key, value in input_data.items():
                              setattr(instance, key, value)
                  else:
                        instance = self.model(**input_data)
                        session.add(instance)

                  await session.commit()
                  await session.refresh(instance)
                  data = {k: getattr(instance, k) for k in self.response_fields}
                  return self.type_cls(**data)

            except SQLAlchemyError as e:
                  raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")