from pydantic import BaseModel, Field, field_validator
from typing import Optional

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


class PatientUpdateValidator(BaseModel):
      name: Optional[str] = Field(None, min_length=3, description="Full name (min 3 characters)")
      gender: Optional[str] = Field(None, description="Gender must be Male, Female, or Other")
      age: Optional[int] = Field(None, gt=0, description="Age must be greater than 0")
      blood_group: Optional[str] = Field(None, description="Example: O+ / A-")
      height_cm: Optional[int] = Field(None, gt=0, description="Height in cm")
      weight_kg: Optional[int] = Field(None, gt=0, description="Weight in kg")
      bmi: Optional[float] = Field(None, gt=0, description="BMI must be greater than 0")
      bp: Optional[str] = Field(None, description="Blood pressure like 120/80")
      glucose: Optional[int] = Field(None, ge=0, description="Glucose level")
      heart_rate: Optional[int] = Field(None, ge=0, description="Heart rate")

      @field_validator("gender")
      def validate_gender(cls, v: Optional[str]) -> Optional[str]:
            if v is not None and v not in {"Male", "Female", "Other"}:
                  raise ValueError("Gender must be Male, Female, or Other")
            return v.title() if v else v

class SymptomInputValidator(BaseModel):
      patient_id: int = Field(..., gt=0, description="Patient ID must be a positive integer")
      name: str = Field(..., min_length=2, description="Symptom name must be at least 2 characters")