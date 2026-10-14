from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.api_key_create_role import ApiKeyCreateRole
from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="ApiKeyCreate")



@_attrs_define
class ApiKeyCreate:
    """ agent_id is required if and only if role is agent

        Attributes:
            role (ApiKeyCreateRole):
            agent_id (UUID | Unset):
     """

    role: ApiKeyCreateRole
    agent_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        agent_id: str | Unset = UNSET
        if not isinstance(self.agent_id, Unset):
            agent_id = str(self.agent_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "role": role,
        })
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = ApiKeyCreateRole(d.pop("role"))




        _agent_id = d.pop("agent_id", UNSET)
        agent_id: UUID | Unset
        if isinstance(_agent_id,  Unset):
            agent_id = UNSET
        else:
            agent_id = UUID(_agent_id)




        api_key_create = cls(
            role=role,
            agent_id=agent_id,
        )

        return api_key_create

