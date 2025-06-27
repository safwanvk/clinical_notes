from app.models import Condition
from app.graphql.types import ConditionType
from app.services.base_patient_service import BasePatientService

class ConditionService(BasePatientService):
    model = Condition
    type_cls = ConditionType
    unique_fields = ["name"]
    response_fields = ["id", "name"]