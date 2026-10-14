from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.decision_status_outcome import DecisionStatusOutcome
from ..models.decision_status_status import DecisionStatusStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.authorization_artifact import AuthorizationArtifact





T = TypeVar("T", bound="DecisionStatus")



@_attrs_define
class DecisionStatus:
    """ 
        Attributes:
            decision_id (UUID):
            outcome (DecisionStatusOutcome):
            status (DecisionStatusStatus):
            reasons (list[Any] | Unset):
            authorization (AuthorizationArtifact | Unset):
     """

    decision_id: UUID
    outcome: DecisionStatusOutcome
    status: DecisionStatusStatus
    reasons: list[Any] | Unset = UNSET
    authorization: AuthorizationArtifact | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.authorization_artifact import AuthorizationArtifact # noqa: PLC0415
        decision_id = str(self.decision_id)

        outcome = self.outcome.value

        status = self.status.value

        reasons: list[Any] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = []
            for reasons_item_data in self.reasons:
                reasons_item: Any
                reasons_item = reasons_item_data
                reasons.append(reasons_item)



        authorization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorization, Unset):
            authorization = self.authorization.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "decision_id": decision_id,
            "outcome": outcome,
            "status": status,
        })
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if authorization is not UNSET:
            field_dict["authorization"] = authorization

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authorization_artifact import AuthorizationArtifact # noqa: PLC0415
        d = dict(src_dict)
        decision_id = UUID(d.pop("decision_id"))




        outcome = DecisionStatusOutcome(d.pop("outcome"))




        status = DecisionStatusStatus(d.pop("status"))




        _reasons = d.pop("reasons", UNSET)
        reasons: list[Any] | Unset = UNSET
        if _reasons is not UNSET:
            reasons = []
            for reasons_item_data in _reasons:
                def _parse_reasons_item(data: object) -> Any:
                    return cast(Any, data)

                reasons_item = _parse_reasons_item(reasons_item_data)

                reasons.append(reasons_item)


        _authorization = d.pop("authorization", UNSET)
        authorization: AuthorizationArtifact | Unset
        if isinstance(_authorization,  Unset):
            authorization = UNSET
        else:
            authorization = AuthorizationArtifact.from_dict(_authorization)




        decision_status = cls(
            decision_id=decision_id,
            outcome=outcome,
            status=status,
            reasons=reasons,
            authorization=authorization,
        )


        decision_status.additional_properties = d
        return decision_status

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
