from app.models import ClinicalFinding
from app.graphql.types import ClinicalFindingType
from app.services.base_patient_service import BasePatientService
from sqlalchemy.ext.asyncio import AsyncSession

class ClinicalFindingService(BasePatientService):
    def __init__(self, session: AsyncSession):
        self.session = session

    model = ClinicalFinding
    type_cls = ClinicalFindingType
    unique_fields = ["note"]
    response_fields = ["id", "note"]