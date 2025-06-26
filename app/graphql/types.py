import strawberry
from app.graphql.validators import (PatientInputValidator, PatientUpdateValidator, SymptomInputValidator, MedicalHistoryInputValidator,
                                    ConditionInputValidator, MedicationInputValidator)

@strawberry.type
class SymptomType:
    id: int
    name: str

@strawberry.type
class MedicalHistoryType:
    id: int
    description: str

@strawberry.type
class ConditionType:
    id: int
    name: str

@strawberry.type
class MedicationType:
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
      medical_history: list[MedicalHistoryType]
      symptoms: list[SymptomType]
      conditions: list[ConditionType]
      medications: list[MedicationType]

@strawberry.experimental.pydantic.input(model=PatientInputValidator, all_fields=True)
class PatientInput:
      pass

@strawberry.experimental.pydantic.input(model=PatientUpdateValidator, all_fields=True)
class PatientUpdateInput:
      pass

@strawberry.experimental.pydantic.input(model=SymptomInputValidator, all_fields=True)
class SymptomInput:
      pass

@strawberry.experimental.pydantic.input(model=MedicalHistoryInputValidator, all_fields=True)
class MedicalHistoryInput:
      pass

@strawberry.experimental.pydantic.input(model=ConditionInputValidator, all_fields=True)
class ConditionInput:
      pass

@strawberry.experimental.pydantic.input(model=MedicationInputValidator, all_fields=True)
class MedicationInput:
      pass