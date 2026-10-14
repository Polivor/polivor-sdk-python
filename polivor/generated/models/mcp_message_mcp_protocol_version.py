from enum import StrEnum

class McpMessageMCPProtocolVersion(StrEnum):
    VALUE_0 = "2025-06-18"
    VALUE_1 = "2025-03-26"
    VALUE_2 = "2024-11-05"

    def __str__(self) -> str:
        return str(self.value)
