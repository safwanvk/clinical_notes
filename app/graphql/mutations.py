import strawberry
from app.graphql.types import (PatientInput, PatientUpdateInput, SymptomInput, SymptomType, MedicalHistoryInput, MedicalHistoryType,
                               ConditionInput, ConditionType, MedicationType, MedicationInput, ClinicalFindingType, ClinicalFindingInput, ResponsePatientType)
from strawberry.exceptions import GraphQLError
from pydantic import ValidationError
from app.permission import IsAuthenticated
from strawberry.types import Info
from app.services.patient_service import PatientService

@strawberry.type
class Mutation:
      @strawberry.mutation(permission_classes=[IsAuthenticated])
      async def add_patient(
                  self,
                  input: PatientInput,
                  info: Info
            ) -> ResponsePatientType:
            try:
                  validated = input.to_pydantic()
                  service: PatientService = info.context["patient_service"]
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await service.create_patient(input)
      @strawberry.mutation(permission_classes=[IsAuthenticated])
      async def update_patient(
                  self,
                  id: int,
                  input: PatientUpdateInput,
                  info: Info
            ) -> ResponsePatientType:
            try:
                  validated = input.to_pydantic()
                  service: PatientService = info.context["patient_service"]
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await service.update_patient_details(id, validated)
      @strawberry.mutation(permission_classes=[IsAuthenticated])
      async def add_or_update_symptom(
                  self,
                  input: SymptomInput,
                  info: Info
            ) -> SymptomType:
            try:
                  service = info.context["symptom_service"]
                  validated = input.to_pydantic()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await service.create_or_update(validated)
      @strawberry.mutation(permission_classes=[IsAuthenticated])
      async def add_or_update_medical_history(
                  self,
                  input: MedicalHistoryInput,
                  info: Info
            ) -> MedicalHistoryType:
            try:
                  service = info.context["medical_history_service"]
                  validated = input.to_pydantic().dict()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await service.create_or_update(validated)
      @strawberry.mutation(permission_classes=[IsAuthenticated])
      async def add_or_update_condition(
                  self,
                  input: ConditionInput,
                  info: Info
            ) -> ConditionType:
            try:
                  service = info.context["condition_service"]
                  validated = input.to_pydantic().dict()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await service.create_or_update(validated)
      @strawberry.mutation(permission_classes=[IsAuthenticated])
      async def add_or_update_medication(
                  self,
                  input: MedicationInput,
                  info: Info
            ) -> MedicationType:
            try:
                  service = info.context["medication_service"]
                  validated = input.to_pydantic().dict()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await service.create_or_update(validated)
      @strawberry.mutation(permission_classes=[IsAuthenticated])
      async def add_or_update_clinical_finding(
                  self,
                  input: ClinicalFindingInput,
                  info: Info
            ) -> ClinicalFindingType:
            try:
                  service = info.context["clinical_finding_service"]
                  validated = input.to_pydantic().dict()
            except ValidationError as e:
                  error_messages = "\n".join(f"{err['loc'][0]}: {err['msg']}" for err in e.errors())
                  raise GraphQLError(f"Validation failed:\n{error_messages}")
            return await service.create_or_update(validated)