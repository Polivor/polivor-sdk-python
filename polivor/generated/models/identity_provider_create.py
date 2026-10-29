from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.identity_provider_create_protocol import IdentityProviderCreateProtocol
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.identity_provider_create_required_claim import IdentityProviderCreateRequiredClaim





T = TypeVar("T", bound="IdentityProviderCreate")



@_attrs_define
class IdentityProviderCreate:
    """ 
        Attributes:
            name (str):
            domains (list[str]):
            protocol (IdentityProviderCreateProtocol | Unset):  Default: IdentityProviderCreateProtocol.OIDC.
            issuer (str | Unset): OIDC only. The issuer URL; its /.well-known/openid-configuration must answer.
            client_id (str | Unset): OIDC only.
            client_secret (str | Unset): OIDC only.
            saml_metadata (str | Unset): SAML only. The identity provider's metadata XML. Give this or saml_metadata_url.
            saml_metadata_url (str | Unset): SAML only. An https URL that serves the identity provider's metadata.
            require_mfa (bool | Unset): Refuse a sign-in that does not show multi-factor authentication (amr for OpenID
                Connect
            required_claim (IdentityProviderCreateRequiredClaim | Unset): A claim (OpenID Connect) or attribute (SAML) the
                sign-in must carry, for example tid for a Microsoft Entra tenant or hd for a Google Workspace domain.
     """

    name: str
    domains: list[str]
    protocol: IdentityProviderCreateProtocol | Unset = IdentityProviderCreateProtocol.OIDC
    issuer: str | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    saml_metadata: str | Unset = UNSET
    saml_metadata_url: str | Unset = UNSET
    require_mfa: bool | Unset = UNSET
    required_claim: IdentityProviderCreateRequiredClaim | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.identity_provider_create_required_claim import IdentityProviderCreateRequiredClaim # noqa: PLC0415
        name = self.name

        domains = self.domains



        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value


        issuer = self.issuer

        client_id = self.client_id

        client_secret = self.client_secret

        saml_metadata = self.saml_metadata

        saml_metadata_url = self.saml_metadata_url

        require_mfa = self.require_mfa

        required_claim: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required_claim, Unset):
            required_claim = self.required_claim.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "domains": domains,
        })
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if saml_metadata is not UNSET:
            field_dict["saml_metadata"] = saml_metadata
        if saml_metadata_url is not UNSET:
            field_dict["saml_metadata_url"] = saml_metadata_url
        if require_mfa is not UNSET:
            field_dict["require_mfa"] = require_mfa
        if required_claim is not UNSET:
            field_dict["required_claim"] = required_claim

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_create_required_claim import IdentityProviderCreateRequiredClaim # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        domains = cast(list[str], d.pop("domains"))


        _protocol = d.pop("protocol", UNSET)
        protocol: IdentityProviderCreateProtocol | Unset
        if isinstance(_protocol,  Unset):
            protocol = UNSET
        else:
            protocol = IdentityProviderCreateProtocol(_protocol)




        issuer = d.pop("issuer", UNSET)

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        saml_metadata = d.pop("saml_metadata", UNSET)

        saml_metadata_url = d.pop("saml_metadata_url", UNSET)

        require_mfa = d.pop("require_mfa", UNSET)

        _required_claim = d.pop("required_claim", UNSET)
        required_claim: IdentityProviderCreateRequiredClaim | Unset
        if isinstance(_required_claim,  Unset):
            required_claim = UNSET
        else:
            required_claim = IdentityProviderCreateRequiredClaim.from_dict(_required_claim)




        identity_provider_create = cls(
            name=name,
            domains=domains,
            protocol=protocol,
            issuer=issuer,
            client_id=client_id,
            client_secret=client_secret,
            saml_metadata=saml_metadata,
            saml_metadata_url=saml_metadata_url,
            require_mfa=require_mfa,
            required_claim=required_claim,
        )

        return identity_provider_create

