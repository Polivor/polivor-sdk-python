from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.identity_provider_protocol import IdentityProviderProtocol
from ..models.identity_provider_status import IdentityProviderStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.identity_provider_domains_item import IdentityProviderDomainsItem
  from ..models.identity_provider_required_claim import IdentityProviderRequiredClaim
  from ..models.identity_provider_service_provider import IdentityProviderServiceProvider
  from ..models.identity_provider_warnings_item import IdentityProviderWarningsItem





T = TypeVar("T", bound="IdentityProvider")



@_attrs_define
class IdentityProvider:
    """ 
        Attributes:
            id (UUID):
            protocol (IdentityProviderProtocol):
            name (str):
            issuer (str): The issuer (OpenID Connect) or the entity id (SAML).
            require_mfa (bool):
            require_confirmed_email (bool):
            warnings (list[IdentityProviderWarningsItem]): What the provider's own description says about the settings
                chosen, for example that it does not list the email claim. Only on the response that creates the provider; never
                blocking.
            status (IdentityProviderStatus): A new provider is PENDING: it routes nobody until an admin signs in once
                through it as a test, which makes it ACTIVE.
            domains (list[IdentityProviderDomainsItem]):
            client_id (str | Unset): OpenID Connect only.
            service_provider (IdentityProviderServiceProvider | Unset): SAML only. What the customer enters at its identity
                provider.
            credential_expires_at (datetime.datetime | None | Unset): When the client secret (as the admin gave it) or the
                earliest SAML signing certificate expires; null when not known.
            required_claim (IdentityProviderRequiredClaim | Unset):
     """

    id: UUID
    protocol: IdentityProviderProtocol
    name: str
    issuer: str
    require_mfa: bool
    require_confirmed_email: bool
    warnings: list[IdentityProviderWarningsItem]
    status: IdentityProviderStatus
    domains: list[IdentityProviderDomainsItem]
    client_id: str | Unset = UNSET
    service_provider: IdentityProviderServiceProvider | Unset = UNSET
    credential_expires_at: datetime.datetime | None | Unset = UNSET
    required_claim: IdentityProviderRequiredClaim | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.identity_provider_domains_item import IdentityProviderDomainsItem # noqa: PLC0415
        from ..models.identity_provider_required_claim import IdentityProviderRequiredClaim # noqa: PLC0415
        from ..models.identity_provider_service_provider import IdentityProviderServiceProvider # noqa: PLC0415
        from ..models.identity_provider_warnings_item import IdentityProviderWarningsItem # noqa: PLC0415
        id = str(self.id)

        protocol = self.protocol.value

        name = self.name

        issuer = self.issuer

        require_mfa = self.require_mfa

        require_confirmed_email = self.require_confirmed_email

        warnings = []
        for warnings_item_data in self.warnings:
            warnings_item = warnings_item_data.to_dict()
            warnings.append(warnings_item)



        status = self.status.value

        domains = []
        for domains_item_data in self.domains:
            domains_item = domains_item_data.to_dict()
            domains.append(domains_item)



        client_id = self.client_id

        service_provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_provider, Unset):
            service_provider = self.service_provider.to_dict()

        credential_expires_at: None | str | Unset
        if isinstance(self.credential_expires_at, Unset):
            credential_expires_at = UNSET
        elif isinstance(self.credential_expires_at, datetime.datetime):
            credential_expires_at = self.credential_expires_at.isoformat()
        else:
            credential_expires_at = self.credential_expires_at

        required_claim: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required_claim, Unset):
            required_claim = self.required_claim.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "protocol": protocol,
            "name": name,
            "issuer": issuer,
            "require_mfa": require_mfa,
            "require_confirmed_email": require_confirmed_email,
            "warnings": warnings,
            "status": status,
            "domains": domains,
        })
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if service_provider is not UNSET:
            field_dict["service_provider"] = service_provider
        if credential_expires_at is not UNSET:
            field_dict["credential_expires_at"] = credential_expires_at
        if required_claim is not UNSET:
            field_dict["required_claim"] = required_claim

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity_provider_domains_item import IdentityProviderDomainsItem # noqa: PLC0415
        from ..models.identity_provider_required_claim import IdentityProviderRequiredClaim # noqa: PLC0415
        from ..models.identity_provider_service_provider import IdentityProviderServiceProvider # noqa: PLC0415
        from ..models.identity_provider_warnings_item import IdentityProviderWarningsItem # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        protocol = IdentityProviderProtocol(d.pop("protocol"))




        name = d.pop("name")

        issuer = d.pop("issuer")

        require_mfa = d.pop("require_mfa")

        require_confirmed_email = d.pop("require_confirmed_email")

        warnings = []
        _warnings = d.pop("warnings")
        for warnings_item_data in (_warnings):
            warnings_item = IdentityProviderWarningsItem.from_dict(warnings_item_data)



            warnings.append(warnings_item)


        status = IdentityProviderStatus(d.pop("status"))




        domains = []
        _domains = d.pop("domains")
        for domains_item_data in (_domains):
            domains_item = IdentityProviderDomainsItem.from_dict(domains_item_data)



            domains.append(domains_item)


        client_id = d.pop("client_id", UNSET)

        _service_provider = d.pop("service_provider", UNSET)
        service_provider: IdentityProviderServiceProvider | Unset
        if isinstance(_service_provider,  Unset):
            service_provider = UNSET
        else:
            service_provider = IdentityProviderServiceProvider.from_dict(_service_provider)




        def _parse_credential_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_expires_at_type_0 = datetime.datetime.fromisoformat(data)



                return credential_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        credential_expires_at = _parse_credential_expires_at(d.pop("credential_expires_at", UNSET))


        _required_claim = d.pop("required_claim", UNSET)
        required_claim: IdentityProviderRequiredClaim | Unset
        if isinstance(_required_claim,  Unset):
            required_claim = UNSET
        else:
            required_claim = IdentityProviderRequiredClaim.from_dict(_required_claim)




        identity_provider = cls(
            id=id,
            protocol=protocol,
            name=name,
            issuer=issuer,
            require_mfa=require_mfa,
            require_confirmed_email=require_confirmed_email,
            warnings=warnings,
            status=status,
            domains=domains,
            client_id=client_id,
            service_provider=service_provider,
            credential_expires_at=credential_expires_at,
            required_claim=required_claim,
        )


        identity_provider.additional_properties = d
        return identity_provider

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
