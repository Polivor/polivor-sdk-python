from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ImportAp2MandateBody")



@_attrs_define
class ImportAp2MandateBody:
    """ 
        Attributes:
            credential (str): The SD-JWT: issuer-signed JWT, then each disclosure, each followed by ~
            issuer_id (UUID):
            principal_id (UUID):
            agent_id (UUID):
            allowed_agent_versions (list[str] | Unset):
            acknowledge_unenforced (list[str] | Unset): Constraint types the admin accepts not to have enforced natively,
                e.g. payment.allowed_payees
     """

    credential: str
    issuer_id: UUID
    principal_id: UUID
    agent_id: UUID
    allowed_agent_versions: list[str] | Unset = UNSET
    acknowledge_unenforced: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        credential = self.credential

        issuer_id = str(self.issuer_id)

        principal_id = str(self.principal_id)

        agent_id = str(self.agent_id)

        allowed_agent_versions: list[str] | Unset = UNSET
        if not isinstance(self.allowed_agent_versions, Unset):
            allowed_agent_versions = self.allowed_agent_versions



        acknowledge_unenforced: list[str] | Unset = UNSET
        if not isinstance(self.acknowledge_unenforced, Unset):
            acknowledge_unenforced = self.acknowledge_unenforced




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "credential": credential,
            "issuer_id": issuer_id,
            "principal_id": principal_id,
            "agent_id": agent_id,
        })
        if allowed_agent_versions is not UNSET:
            field_dict["allowed_agent_versions"] = allowed_agent_versions
        if acknowledge_unenforced is not UNSET:
            field_dict["acknowledge_unenforced"] = acknowledge_unenforced

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential = d.pop("credential")

        issuer_id = UUID(d.pop("issuer_id"))




        principal_id = UUID(d.pop("principal_id"))




        agent_id = UUID(d.pop("agent_id"))




        allowed_agent_versions = cast(list[str], d.pop("allowed_agent_versions", UNSET))


        acknowledge_unenforced = cast(list[str], d.pop("acknowledge_unenforced", UNSET))


        import_ap_2_mandate_body = cls(
            credential=credential,
            issuer_id=issuer_id,
            principal_id=principal_id,
            agent_id=agent_id,
            allowed_agent_versions=allowed_agent_versions,
            acknowledge_unenforced=acknowledge_unenforced,
        )

        return import_ap_2_mandate_body

