from enum import StrEnum

class DenialCode(StrEnum):
    AGENT_NOT_ENABLED = "AGENT_NOT_ENABLED"
    APPROVAL_EXPIRED = "APPROVAL_EXPIRED"
    APPROVAL_REQUIRED = "APPROVAL_REQUIRED"
    APPROVER_DENIED = "APPROVER_DENIED"
    OUTSIDE_AUTHORITY = "OUTSIDE_AUTHORITY"
    UNAVAILABLE = "UNAVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
