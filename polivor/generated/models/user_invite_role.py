from enum import StrEnum

class UserInviteRole(StrEnum):
    ADMIN = "ADMIN"
    APPROVER = "APPROVER"
    VIEWER = "VIEWER"

    def __str__(self) -> str:
        return str(self.value)
