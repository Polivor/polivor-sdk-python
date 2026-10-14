from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.evidence_row_payload import EvidenceRowPayload





T = TypeVar("T", bound="EvidenceRow")



@_attrs_define
class EvidenceRow:
    """ 
        Attributes:
            seq (int):
            event_type (str):
            subject_id (UUID):
            payload (EvidenceRowPayload): RFC 8785 canonicalised before hashing
            prev_hash (str): Hex
            hash_ (str): Hex
            jws (str):
            key_version (int):
            created_at (datetime.datetime):
     """

    seq: int
    event_type: str
    subject_id: UUID
    payload: EvidenceRowPayload
    prev_hash: str
    hash_: str
    jws: str
    key_version: int
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.evidence_row_payload import EvidenceRowPayload # noqa: PLC0415
        seq = self.seq

        event_type = self.event_type

        subject_id = str(self.subject_id)

        payload = self.payload.to_dict()

        prev_hash = self.prev_hash

        hash_ = self.hash_

        jws = self.jws

        key_version = self.key_version

        created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "seq": seq,
            "event_type": event_type,
            "subject_id": subject_id,
            "payload": payload,
            "prev_hash": prev_hash,
            "hash": hash_,
            "jws": jws,
            "key_version": key_version,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evidence_row_payload import EvidenceRowPayload # noqa: PLC0415
        d = dict(src_dict)
        seq = d.pop("seq")

        event_type = d.pop("event_type")

        subject_id = UUID(d.pop("subject_id"))




        payload = EvidenceRowPayload.from_dict(d.pop("payload"))




        prev_hash = d.pop("prev_hash")

        hash_ = d.pop("hash")

        jws = d.pop("jws")

        key_version = d.pop("key_version")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        evidence_row = cls(
            seq=seq,
            event_type=event_type,
            subject_id=subject_id,
            payload=payload,
            prev_hash=prev_hash,
            hash_=hash_,
            jws=jws,
            key_version=key_version,
            created_at=created_at,
        )


        evidence_row.additional_properties = d
        return evidence_row

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
