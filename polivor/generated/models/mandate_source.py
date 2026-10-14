from enum import StrEnum

class MandateSource(StrEnum):
    AP2 = "AP2"
    NATIVE = "NATIVE"

    def __str__(self) -> str:
        return str(self.value)
