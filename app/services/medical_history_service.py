from app.models import MedicalHistory
from app.graphql.types import MedicalHistoryType
from app.services.base_patient_service import BasePatientService
from sqlalchemy.ext.asyncio import AsyncSession

class MedicalHistoryService(BasePatientService):
    def __init__(self, session: AsyncSession):
        self.session = session

    model = MedicalHistory
    type_cls = MedicalHistoryType
    unique_fields = ["description"]
    response_fields = ["id", "description"]