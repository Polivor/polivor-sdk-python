from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RefreshIdentityProviderSamlMetadataBody")



@_attrs_define
class RefreshIdentityProviderSamlMetadataBody:
    """ 
        Attributes:
            saml_metadata (str | Unset):
            saml_metadata_url (str | Unset):
     """

    saml_metadata: str | Unset = UNSET
    saml_metadata_url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        saml_metadata = self.saml_metadata

        saml_metadata_url = self.saml_metadata_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if saml_metadata is not UNSET:
            field_dict["saml_metadata"] = saml_metadata
        if saml_metadata_url is not UNSET:
            field_dict["saml_metadata_url"] = saml_metadata_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        saml_metadata = d.pop("saml_metadata", UNSET)

        saml_metadata_url = d.pop("saml_metadata_url", UNSET)

        refresh_identity_provider_saml_metadata_body = cls(
            saml_metadata=saml_metadata,
            saml_metadata_url=saml_metadata_url,
        )

        return refresh_identity_provider_saml_metadata_body

