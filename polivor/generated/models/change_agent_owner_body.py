from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="ChangeAgentOwnerBody")



@_attrs_define
class ChangeAgentOwnerBody:
    """ 
        Attributes:
            owner_person_id (UUID):
     """

    owner_person_id: UUID





    def to_dict(self) -> dict[str, Any]:
        owner_person_id = str(self.owner_person_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "owner_person_id": owner_person_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_person_id = UUID(d.pop("owner_person_id"))




        change_agent_owner_body = cls(
            owner_person_id=owner_person_id,
        )

        return change_agent_owner_body

