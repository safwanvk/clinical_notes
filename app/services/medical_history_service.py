from app.models import MedicalHistory
from app.graphql.types import MedicalHistoryType
from app.services.base_patient_service import BasePatientService

class MedicalHistoryService(BasePatientService):
    model = MedicalHistory
    type_cls = MedicalHistoryType
    unique_fields = ["description"]
    response_fields = ["id", "description"]