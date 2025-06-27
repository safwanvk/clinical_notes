from app.services.medication_service import MedicationService
from app.services.symptom_service import SymptomService
from app.services.condition_service import ConditionService
from app.services.clinical_finding_service import ClinicalFindingService
from app.services.medical_history_service import MedicalHistoryService

async def get_service_context():
    return {
        "symptom_service": SymptomService(),
        "medication_service": MedicationService(),
        "condition_service": ConditionService(),
        "clinical_finding_service": ClinicalFindingService(),
        "medical_history_service": MedicalHistoryService()
    }