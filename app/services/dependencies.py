from app.services.medication_service import MedicationService
from app.services.symptom_service import SymptomService
from app.services.condition_service import ConditionService
from app.services.clinical_finding_service import ClinicalFindingService
from app.services.medical_history_service import MedicalHistoryService
from app.services.patient_service import PatientService
from sqlalchemy.ext.asyncio import AsyncSession

async def get_service_context(session: AsyncSession):
    return {
        "symptom_service": SymptomService(session),
        "medication_service": MedicationService(session),
        "condition_service": ConditionService(session),
        "clinical_finding_service": ClinicalFindingService(session),
        "medical_history_service": MedicalHistoryService(session),
        "patient_service": PatientService(session),
    }