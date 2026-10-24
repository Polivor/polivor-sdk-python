from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IdentityProviderDomainsItem")



@_attrs_define
class IdentityProviderDomainsItem:
    """ 
        Attributes:
            domain (str):
            verified (bool):
            record_host (str): Where to publish the TXT record.
            record_value (str): What the TXT record must contain.
     """

    domain: str
    verified: bool
    record_host: str
    record_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        verified = self.verified

        record_host = self.record_host

        record_value = self.record_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "domain": domain,
            "verified": verified,
            "record_host": record_host,
            "record_value": record_value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        verified = d.pop("verified")

        record_host = d.pop("record_host")

        record_value = d.pop("record_value")

        identity_provider_domains_item = cls(
            domain=domain,
            verified=verified,
            record_host=record_host,
            record_value=record_value,
        )


        identity_provider_domains_item.additional_properties = d
        return identity_provider_domains_item

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
