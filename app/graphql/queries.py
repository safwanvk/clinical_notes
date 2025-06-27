import strawberry
from app.graphql.types import PatientType
from app.services.patient_service import get_patient_details
from app.permission import IsAuthenticated
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession

@strawberry.type
class Query:
      @strawberry.field(permission_classes=[IsAuthenticated])
      async def patient(self, id: int, info: Info) -> PatientType:
            session: AsyncSession = info.context["session"]
            return await get_patient_details(id, session)