from app.models import ClinicalFinding, Patient
from app.db import SessionLocal
from app.graphql.types import ClinicalFindingType, ClinicalFindingInput
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from strawberry.exceptions import GraphQLError
from sqlalchemy import select

async def create_clinical_finding(input: ClinicalFindingInput) -> ClinicalFindingType:
      try:
            async with SessionLocal() as session:
                  patient_result = await session.execute(select(Patient).where(Patient.id == input.patient_id))
                  patient = patient_result.scalars().first()
                  if not patient:
                        raise GraphQLError(f"Patient with id {input.patient_id} not found.")

                  existing = await session.execute(select(ClinicalFinding).where( ClinicalFinding.patient_id == input.patient_id, ClinicalFinding.note == input.note))
                  if existing.scalars().first():
                        raise GraphQLError("Clinical finding with this note already exists for this patient.")

                  clinical_finding = ClinicalFinding(
                        patient_id=input.patient_id,
                        note=input.note,
                  )
                  session.add(clinical_finding)
                  await session.commit()
                  await session.refresh(clinical_finding)
                  return ClinicalFindingType(
                        id=clinical_finding.id,
                        note=clinical_finding.note
                  )
      except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
      except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")