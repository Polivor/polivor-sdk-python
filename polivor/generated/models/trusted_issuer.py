from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast
from uuid import UUID






T = TypeVar("T", bound="TrustedIssuer")



@_attrs_define
class TrustedIssuer:
    """ 
        Attributes:
            id (UUID):
            name (str):
            format_ (Literal['AP2']):
            key_ids (list[str]): Ids of the keys registered by hand
            jwks_url (None | str | Unset):
     """

    id: UUID
    name: str
    format_: Literal['AP2']
    key_ids: list[str]
    jwks_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        format_ = self.format_

        key_ids = self.key_ids



        jwks_url: None | str | Unset
        if isinstance(self.jwks_url, Unset):
            jwks_url = UNSET
        else:
            jwks_url = self.jwks_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "format": format_,
            "key_ids": key_ids,
        })
        if jwks_url is not UNSET:
            field_dict["jwks_url"] = jwks_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        format_ = cast(Literal['AP2'] , d.pop("format"))
        if format_ != 'AP2':
            raise ValueError(f"format must match const 'AP2', got '{format_}'")

        key_ids = cast(list[str], d.pop("key_ids"))


        def _parse_jwks_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jwks_url = _parse_jwks_url(d.pop("jwks_url", UNSET))


        trusted_issuer = cls(
            id=id,
            name=name,
            format_=format_,
            key_ids=key_ids,
            jwks_url=jwks_url,
        )


        trusted_issuer.additional_properties = d
        return trusted_issuer

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
