import strawberry
from app.graphql.types import PatientType
from app.services.patient_service import get_patient_details
from app.permission import IsAuthenticated

@strawberry.type
class Query:
      @strawberry.field(permission_classes=[IsAuthenticated])
      async def patient(self, id: int) -> PatientType:
            return await get_patient_details(id)