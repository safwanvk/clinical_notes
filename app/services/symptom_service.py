from app.models import Symptom
from app.graphql.types import SymptomType
from app.services.base_patient_service import BasePatientService

class SymptomService(BasePatientService):
    model = Symptom
    type_cls = SymptomType
    unique_fields = ["name"]
    response_fields = ["id", "name"]