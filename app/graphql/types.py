import strawberry
from app.graphql.validators import PatientInputValidator, PatientUpdateValidator

@strawberry.type
class PatientType:
      id: int
      name: str
      gender: str
      age: int
      blood_group: str
      height_cm: int
      weight_kg: int
      bmi: float
      bp: str
      glucose: int
      heart_rate: int

@strawberry.experimental.pydantic.input(model=PatientInputValidator, all_fields=True)
class PatientInput:
      pass

@strawberry.experimental.pydantic.input(model=PatientUpdateValidator, all_fields=True)
class PatientUpdateInput:
      pass