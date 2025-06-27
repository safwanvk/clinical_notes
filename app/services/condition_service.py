from app.models import Condition
from app.graphql.types import ConditionType
from app.services.base_patient_service import BasePatientService
from sqlalchemy.ext.asyncio import AsyncSession

class ConditionService(BasePatientService):
    def __init__(self, session: AsyncSession):
        self.session = session

    model = Condition
    type_cls = ConditionType
    unique_fields = ["name"]
    response_fields = ["id", "name"]