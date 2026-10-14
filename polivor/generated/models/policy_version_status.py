from enum import StrEnum

class PolicyVersionStatus(StrEnum):
    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"
    RETIRED = "RETIRED"

    def __str__(self) -> str:
        return str(self.value)
