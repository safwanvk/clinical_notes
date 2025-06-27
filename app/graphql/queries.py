import strawberry
from app.graphql.types import PatientType
from app.permission import IsAuthenticated
from strawberry.types import Info
from app.services.patient_service import PatientService

@strawberry.type
class Query:
      @strawberry.field(permission_classes=[IsAuthenticated])
      async def patient(
                  self,
                  id: int,
                  info: Info
            ) -> PatientType:
            service: PatientService = info.context["patient_service"]
            return await service.get_patient_details(id)