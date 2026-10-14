from enum import StrEnum

class BeneficiaryCreateStatus(StrEnum):
    APPROVED = "APPROVED"
    BLOCKED = "BLOCKED"

    def __str__(self) -> str:
        return str(self.value)
