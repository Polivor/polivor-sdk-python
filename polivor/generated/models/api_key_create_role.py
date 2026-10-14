from enum import StrEnum

class ApiKeyCreateRole(StrEnum):
    ADMIN = "admin"
    AGENT = "agent"
    ENFORCER = "enforcer"

    def __str__(self) -> str:
        return str(self.value)
