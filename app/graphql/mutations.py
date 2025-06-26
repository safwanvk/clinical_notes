import strawberry
from app.graphql.types import (PatientInput, PatientType, PatientUpdateInput, SymptomInput, SymptomType, MedicalHistoryInput, MedicalHistoryType,
                               ConditionInput, ConditionType)
from app.services.patient_service import create_patient, update_patient_details
from app.services.symptom_service import create_symptom
from app.services.medical_history_service import create_medical_history
from app.services.condition_service import create_condition
from strawberry.exceptions import GraphQLError
from pydantic import ValidationError

@strawberry.type
class Mutation:
      @strawberry.mutation
      async def add_patient(self, input: PatientInput) -> PatientType:
            try:
                  validated = input.to_pydantic()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await create_patient(input)
      @strawberry.mutation
      async def update_patient(self, id: int, input: PatientUpdateInput) -> PatientType:
            try:
                  validated = input.to_pydantic()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await update_patient_details(id, input)
      @strawberry.mutation
      async def add_symptom(self, input: SymptomInput) -> SymptomType:
            try:
                  validated = input.to_pydantic()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await create_symptom(input)
      @strawberry.mutation
      async def add_medical_history(self, input: MedicalHistoryInput) -> MedicalHistoryType:
            try:
                  validated = input.to_pydantic()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await create_medical_history(input)
      @strawberry.mutation
      async def add_condition(self, input: ConditionInput) -> ConditionType:
            try:
                  validated = input.to_pydantic()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await create_condition(input)