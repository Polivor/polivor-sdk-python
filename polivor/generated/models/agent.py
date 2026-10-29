from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_status import AgentStatus
from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="Agent")



@_attrs_define
class Agent:
    """ 
        Attributes:
            id (UUID):
            name (str):
            principal_id (UUID):
            owner_person_id (UUID):
            status (AgentStatus):
            agent_key (str | Unset): Shown once, on agent creation only
     """

    id: UUID
    name: str
    principal_id: UUID
    owner_person_id: UUID
    status: AgentStatus
    agent_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        principal_id = str(self.principal_id)

        owner_person_id = str(self.owner_person_id)

        status = self.status.value

        agent_key = self.agent_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "principal_id": principal_id,
            "owner_person_id": owner_person_id,
            "status": status,
        })
        if agent_key is not UNSET:
            field_dict["agent_key"] = agent_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        principal_id = UUID(d.pop("principal_id"))




        owner_person_id = UUID(d.pop("owner_person_id"))




        status = AgentStatus(d.pop("status"))




        agent_key = d.pop("agent_key", UNSET)

        agent = cls(
            id=id,
            name=name,
            principal_id=principal_id,
            owner_person_id=owner_person_id,
            status=status,
            agent_key=agent_key,
        )


        agent.additional_properties = d
        return agent

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
