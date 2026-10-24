from enum import StrEnum

class UserRoleRole(StrEnum):
    ADMIN = "ADMIN"
    APPROVER = "APPROVER"
    VIEWER = "VIEWER"

    def __str__(self) -> str:
        return str(self.value)
