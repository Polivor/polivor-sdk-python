from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="IdentityProviderCreateRequiredClaim")



@_attrs_define
class IdentityProviderCreateRequiredClaim:
    """ A claim (OpenID Connect) or attribute (SAML) the sign-in must carry, for example tid for a Microsoft Entra tenant or
    hd for a Google Workspace domain.

        Attributes:
            name (str):
            value (str):
     """

    name: str
    value: str





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        identity_provider_create_required_claim = cls(
            name=name,
            value=value,
        )

        return identity_provider_create_required_claim

