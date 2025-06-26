import strawberry
from app.graphql.validators import PatientInputValidator, PatientUpdateValidator, SymptomInputValidator

@strawberry.type
class SymptomType:
    id: int
    name: str

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
      symptoms: list[SymptomType]

@strawberry.experimental.pydantic.input(model=PatientInputValidator, all_fields=True)
class PatientInput:
      pass

@strawberry.experimental.pydantic.input(model=PatientUpdateValidator, all_fields=True)
class PatientUpdateInput:
      pass

@strawberry.experimental.pydantic.input(model=SymptomInputValidator, all_fields=True)
class SymptomInput:
      pass