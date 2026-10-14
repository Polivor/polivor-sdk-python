from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.evidence_bundle_authorizations_item import EvidenceBundleAuthorizationsItem
  from ..models.evidence_row import EvidenceRow
  from ..models.jwks import Jwks





T = TypeVar("T", bound="EvidenceBundle")



@_attrs_define
class EvidenceBundle:
    """ Everything needed to verify a range of evidence offline (cli/verify or the console verifier): rows with canonical
    payloads, hashes and
    signatures, all public keys, and the authorization artifacts issued for the decisions in the range. A range that
    does not start at
    row 1 verifies internally; its first row's prev_hash is the anchor to compare with the previous row you hold.

        Attributes:
            format_ (Literal['polivor.evidence-bundle/v1']):
            tenant_id (UUID):
            exported_at (datetime.datetime):
            from_seq (int):
            to_seq (int):
            rows (list[EvidenceRow]):
            jwks (Jwks):
            authorizations (list[EvidenceBundleAuthorizationsItem]):
     """

    format_: Literal['polivor.evidence-bundle/v1']
    tenant_id: UUID
    exported_at: datetime.datetime
    from_seq: int
    to_seq: int
    rows: list[EvidenceRow]
    jwks: Jwks
    authorizations: list[EvidenceBundleAuthorizationsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.evidence_bundle_authorizations_item import EvidenceBundleAuthorizationsItem # noqa: PLC0415
        from ..models.evidence_row import EvidenceRow # noqa: PLC0415
        from ..models.jwks import Jwks # noqa: PLC0415
        format_ = self.format_

        tenant_id = str(self.tenant_id)

        exported_at = self.exported_at.isoformat()

        from_seq = self.from_seq

        to_seq = self.to_seq

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)



        jwks = self.jwks.to_dict()

        authorizations = []
        for authorizations_item_data in self.authorizations:
            authorizations_item = authorizations_item_data.to_dict()
            authorizations.append(authorizations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "format": format_,
            "tenant_id": tenant_id,
            "exported_at": exported_at,
            "from_seq": from_seq,
            "to_seq": to_seq,
            "rows": rows,
            "jwks": jwks,
            "authorizations": authorizations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evidence_bundle_authorizations_item import EvidenceBundleAuthorizationsItem # noqa: PLC0415
        from ..models.evidence_row import EvidenceRow # noqa: PLC0415
        from ..models.jwks import Jwks # noqa: PLC0415
        d = dict(src_dict)
        format_ = cast(Literal['polivor.evidence-bundle/v1'] , d.pop("format"))
        if format_ != 'polivor.evidence-bundle/v1':
            raise ValueError(f"format must match const 'polivor.evidence-bundle/v1', got '{format_}'")

        tenant_id = UUID(d.pop("tenant_id"))




        exported_at = datetime.datetime.fromisoformat(d.pop("exported_at"))




        from_seq = d.pop("from_seq")

        to_seq = d.pop("to_seq")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in (_rows):
            rows_item = EvidenceRow.from_dict(rows_item_data)



            rows.append(rows_item)


        jwks = Jwks.from_dict(d.pop("jwks"))




        authorizations = []
        _authorizations = d.pop("authorizations")
        for authorizations_item_data in (_authorizations):
            authorizations_item = EvidenceBundleAuthorizationsItem.from_dict(authorizations_item_data)



            authorizations.append(authorizations_item)


        evidence_bundle = cls(
            format_=format_,
            tenant_id=tenant_id,
            exported_at=exported_at,
            from_seq=from_seq,
            to_seq=to_seq,
            rows=rows,
            jwks=jwks,
            authorizations=authorizations,
        )


        evidence_bundle.additional_properties = d
        return evidence_bundle

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
