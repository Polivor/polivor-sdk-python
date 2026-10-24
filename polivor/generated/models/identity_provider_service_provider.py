from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IdentityProviderServiceProvider")



@_attrs_define
class IdentityProviderServiceProvider:
    """ SAML only. What the customer enters at its identity provider.

        Attributes:
            entity_id (str):
            assertion_consumer_url (str):
            metadata_url (str):
     """

    entity_id: str
    assertion_consumer_url: str
    metadata_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        assertion_consumer_url = self.assertion_consumer_url

        metadata_url = self.metadata_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "entity_id": entity_id,
            "assertion_consumer_url": assertion_consumer_url,
            "metadata_url": metadata_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_id = d.pop("entity_id")

        assertion_consumer_url = d.pop("assertion_consumer_url")

        metadata_url = d.pop("metadata_url")

        identity_provider_service_provider = cls(
            entity_id=entity_id,
            assertion_consumer_url=assertion_consumer_url,
            metadata_url=metadata_url,
        )


        identity_provider_service_provider.additional_properties = d
        return identity_provider_service_provider

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
