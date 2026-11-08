from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="ReplaceIdentityProviderClientSecretBody")



@_attrs_define
class ReplaceIdentityProviderClientSecretBody:
    """ 
        Attributes:
            client_secret (str):
            client_secret_expires_on (datetime.date | Unset): Optional. The day the new secret stops working; the admins are
                warned before it.
     """

    client_secret: str
    client_secret_expires_on: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        client_secret = self.client_secret

        client_secret_expires_on: str | Unset = UNSET
        if not isinstance(self.client_secret_expires_on, Unset):
            client_secret_expires_on = self.client_secret_expires_on.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "client_secret": client_secret,
        })
        if client_secret_expires_on is not UNSET:
            field_dict["client_secret_expires_on"] = client_secret_expires_on

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_secret = d.pop("client_secret")

        _client_secret_expires_on = d.pop("client_secret_expires_on", UNSET)
        client_secret_expires_on: datetime.date | Unset
        if isinstance(_client_secret_expires_on,  Unset):
            client_secret_expires_on = UNSET
        else:
            client_secret_expires_on = datetime.date.fromisoformat(_client_secret_expires_on)




        replace_identity_provider_client_secret_body = cls(
            client_secret=client_secret,
            client_secret_expires_on=client_secret_expires_on,
        )

        return replace_identity_provider_client_secret_body

