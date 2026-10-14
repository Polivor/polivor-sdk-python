from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="EvidenceBundleAuthorizationsItem")



@_attrs_define
class EvidenceBundleAuthorizationsItem:
    """ 
        Attributes:
            id (UUID):
            decision_id (UUID):
            jws (str):
            expires_at (datetime.datetime):
     """

    id: UUID
    decision_id: UUID
    jws: str
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        decision_id = str(self.decision_id)

        jws = self.jws

        expires_at = self.expires_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "decision_id": decision_id,
            "jws": jws,
            "expires_at": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        decision_id = UUID(d.pop("decision_id"))




        jws = d.pop("jws")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))




        evidence_bundle_authorizations_item = cls(
            id=id,
            decision_id=decision_id,
            jws=jws,
            expires_at=expires_at,
        )


        evidence_bundle_authorizations_item.additional_properties = d
        return evidence_bundle_authorizations_item

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
