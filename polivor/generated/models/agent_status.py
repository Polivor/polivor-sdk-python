from enum import StrEnum

class AgentStatus(StrEnum):
    ACTIVE = "ACTIVE"
    RETIRED = "RETIRED"
    SUSPENDED = "SUSPENDED"

    def __str__(self) -> str:
        return str(self.value)
