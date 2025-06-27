from app.models import Patient
from app.graphql.types import (PatientType, SymptomType, MedicalHistoryType,
                               ConditionType, MedicationType, ClinicalFindingType, ResponsePatientType)

def serialize_response_patient(patient: Patient) -> ResponsePatientType:
      return ResponsePatientType(
            id=patient.id,
            name=patient.name,
            gender=patient.gender,
            age=patient.age,
            blood_group=patient.blood_group,
            height_cm=patient.height_cm,
            weight_kg=patient.weight_kg,
            bmi=patient.bmi,
            bp=patient.bp,
            glucose=patient.glucose,
            heart_rate=patient.heart_rate,
      )

def serialize_patient(patient: Patient) -> PatientType:
      return PatientType(
            id=patient.id,
            name=patient.name,
            gender=patient.gender,
            age=patient.age,
            blood_group=patient.blood_group,
            height_cm=patient.height_cm,
            weight_kg=patient.weight_kg,
            bmi=patient.bmi,
            bp=patient.bp,
            glucose=patient.glucose,
            heart_rate=patient.heart_rate,
            medical_history=[MedicalHistoryType(id=m.id, description=m.description) for m in patient.medical_history],
            symptoms=[SymptomType(id=s.id, name=s.name) for s in patient.symptoms],
            conditions=[ConditionType(id=c.id, name=c.name) for c in patient.conditions],
            medications=[MedicationType(id=med.id, name=med.name) for med in patient.medications],
            clinical_findings=[ClinicalFindingType(id=cf.id, note=cf.note) for cf in patient.clinical_findings]
      )
