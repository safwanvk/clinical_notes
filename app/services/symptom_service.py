from app.models import Symptom
from app.graphql.types import SymptomType
from app.services.base_patient_service import BasePatientService
from sqlalchemy.ext.asyncio import AsyncSession

class SymptomService(BasePatientService):
    def __init__(self, session: AsyncSession):
        self.session = session

    model = Symptom
    type_cls = SymptomType
    unique_fields = ["name"]
    response_fields = ["id", "name"]