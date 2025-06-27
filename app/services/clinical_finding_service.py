from app.models import ClinicalFinding
from app.graphql.types import ClinicalFindingType
from app.services.base_patient_service import BasePatientService

class ClinicalFindingService(BasePatientService):
    model = ClinicalFinding
    type_cls = ClinicalFindingType
    unique_fields = ["note"]
    response_fields = ["id", "note"]