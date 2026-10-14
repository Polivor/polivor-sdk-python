from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mandate_source import MandateSource
from ..models.mandate_status import MandateStatus
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.mandate_body import MandateBody





T = TypeVar("T", bound="Mandate")



@_attrs_define
class Mandate:
    """ 
        Attributes:
            id (UUID):
            principal_id (UUID):
            agent_id (UUID):
            status (MandateStatus):
            current_version (int): The version in force (a DRAFT's current_version is the one activation will put in force)
            latest_version (int): Highest version created; takes effect only when activated
            version (int): The version whose body is returned
            source (MandateSource):
            body (MandateBody): Native Financial Mandate body. The authoritative definition is docs/schema/financial-
                mandate.v0.json; validated against it on write. A DRAFT imported from AP2 holds only the mapped fields until a
                complete version is added.
     """

    id: UUID
    principal_id: UUID
    agent_id: UUID
    status: MandateStatus
    current_version: int
    latest_version: int
    version: int
    source: MandateSource
    body: MandateBody
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mandate_body import MandateBody # noqa: PLC0415
        id = str(self.id)

        principal_id = str(self.principal_id)

        agent_id = str(self.agent_id)

        status = self.status.value

        current_version = self.current_version

        latest_version = self.latest_version

        version = self.version

        source = self.source.value

        body = self.body.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "principal_id": principal_id,
            "agent_id": agent_id,
            "status": status,
            "current_version": current_version,
            "latest_version": latest_version,
            "version": version,
            "source": source,
            "body": body,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mandate_body import MandateBody # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        principal_id = UUID(d.pop("principal_id"))




        agent_id = UUID(d.pop("agent_id"))




        status = MandateStatus(d.pop("status"))




        current_version = d.pop("current_version")

        latest_version = d.pop("latest_version")

        version = d.pop("version")

        source = MandateSource(d.pop("source"))




        body = MandateBody.from_dict(d.pop("body"))




        mandate = cls(
            id=id,
            principal_id=principal_id,
            agent_id=agent_id,
            status=status,
            current_version=current_version,
            latest_version=latest_version,
            version=version,
            source=source,
            body=body,
        )


        mandate.additional_properties = d
        return mandate

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
