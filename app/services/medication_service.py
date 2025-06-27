from app.models import Medication
from app.graphql.types import MedicationType
from app.services.base_patient_service import BasePatientService
from sqlalchemy.ext.asyncio import AsyncSession

class MedicationService(BasePatientService):
    def __init__(self, session: AsyncSession):
        self.session = session

    model = Medication
    type_cls = MedicationType
    unique_fields = ["name"]
    response_fields = ["id", "name"]