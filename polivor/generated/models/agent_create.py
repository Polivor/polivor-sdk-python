from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="AgentCreate")



@_attrs_define
class AgentCreate:
    """ 
        Attributes:
            name (str):
            principal_id (UUID):
            owner_person_id (UUID):
     """

    name: str
    principal_id: UUID
    owner_person_id: UUID





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        principal_id = str(self.principal_id)

        owner_person_id = str(self.owner_person_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "principal_id": principal_id,
            "owner_person_id": owner_person_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        principal_id = UUID(d.pop("principal_id"))




        owner_person_id = UUID(d.pop("owner_person_id"))




        agent_create = cls(
            name=name,
            principal_id=principal_id,
            owner_person_id=owner_person_id,
        )

        return agent_create

