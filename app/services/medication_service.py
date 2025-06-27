from app.models import Medication
from app.graphql.types import MedicationType
from app.services.base_patient_service import BasePatientService

class MedicationService(BasePatientService):
    model = Medication
    type_cls = MedicationType
    unique_fields = ["name"]
    response_fields = ["id", "name"]