from enum import StrEnum

class ApiKeyCreatedRole(StrEnum):
    ADMIN = "admin"
    AGENT = "agent"
    ENFORCER = "enforcer"

    def __str__(self) -> str:
        return str(self.value)
