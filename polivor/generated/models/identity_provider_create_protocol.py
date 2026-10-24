from enum import StrEnum

class IdentityProviderCreateProtocol(StrEnum):
    OIDC = "OIDC"
    SAML = "SAML"

    def __str__(self) -> str:
        return str(self.value)
