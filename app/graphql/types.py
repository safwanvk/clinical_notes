import strawberry
from pydantic import BaseModel, Field, field_validator

class PatientInputValidator(BaseModel):
      name: str = Field(..., min_length=3, description="Full name (min 3 characters)")
      gender: str = Field(..., description="Gender must be Male, Female, or Other")
      age: int = Field(..., gt=0, description="Age must be greater than 0")
      blood_group: str = Field(..., description="Example: O+ / A-")
      height_cm: int = Field(..., gt=0, description="Height in cm")
      weight_kg: int = Field(..., gt=0, description="Weight in kg")
      bmi: float = Field(..., gt=0, description="BMI must be greater than 0")
      bp: str = Field(..., description="Blood pressure like 120/80")
      glucose: int = Field(..., ge=0, description="Glucose level")
      heart_rate: int = Field(..., ge=0, description="Heart rate")

      @field_validator("gender")
      def validate_gender(cls, v: str) -> str:
            allowed = {"Male", "Female", "Other"}
            if v not in allowed:
                  raise ValueError("Gender must be Male, Female, or Other")
            return v.title()

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