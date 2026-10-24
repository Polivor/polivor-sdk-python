from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PersonCreate")



@_attrs_define
class PersonCreate:
    """ 
        Attributes:
            name (str):
            email (str):
            title (str | Unset):
     """

    name: str
    email: str
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "email": email,
        })
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        title = d.pop("title", UNSET)

        person_create = cls(
            name=name,
            email=email,
            title=title,
        )

        return person_create

