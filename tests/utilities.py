from app.models import Patient
from sqlalchemy.ext.asyncio import AsyncSession

async def create_patient(session: AsyncSession, name="Test Patient"):
      patient = Patient(
            name=name,
            gender="Male",
            age=30,
            blood_group="A+",
            height_cm=170,
            weight_kg=70,
            bmi=24.2,
            bp="120/80",
            glucose=90,
            heart_rate=70
      )
      session.add(patient)
      await session.commit()
      await session.refresh(patient)
      return patient

def graphql_request(query: str, token="testtoken"):
      return {
            "json": {"query": query},
            "headers": {"Authorization": f"Bearer {token}"} if token else {}
      }