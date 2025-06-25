import strawberry
from app.graphql.types import PatientInput, PatientType
from app.services.patient_service import create_patient
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