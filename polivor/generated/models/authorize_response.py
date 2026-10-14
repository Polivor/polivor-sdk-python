from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.authorize_response_outcome import AuthorizeResponseOutcome
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.authorization_artifact import AuthorizationArtifact
  from ..models.authorize_response_evidence import AuthorizeResponseEvidence
  from ..models.authorize_response_mandate import AuthorizeResponseMandate
  from ..models.check import Check





T = TypeVar("T", bound="AuthorizeResponse")



@_attrs_define
class AuthorizeResponse:
    """ 
        Attributes:
            decision_id (UUID):
            outcome (AuthorizeResponseOutcome):
            reasons (list[Any]):
            checks (list[Check]):
            policy_version (int):
            evidence (AuthorizeResponseEvidence): Absent on simulate
            simulated (bool | Unset):
            mandate (AuthorizeResponseMandate | Unset):
            authorization (AuthorizationArtifact | Unset):
     """

    decision_id: UUID
    outcome: AuthorizeResponseOutcome
    reasons: list[Any]
    checks: list[Check]
    policy_version: int
    evidence: AuthorizeResponseEvidence
    simulated: bool | Unset = UNSET
    mandate: AuthorizeResponseMandate | Unset = UNSET
    authorization: AuthorizationArtifact | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.authorization_artifact import AuthorizationArtifact # noqa: PLC0415
        from ..models.authorize_response_evidence import AuthorizeResponseEvidence # noqa: PLC0415
        from ..models.authorize_response_mandate import AuthorizeResponseMandate # noqa: PLC0415
        from ..models.check import Check # noqa: PLC0415
        decision_id = str(self.decision_id)

        outcome = self.outcome.value

        reasons = []
        for reasons_item_data in self.reasons:
            reasons_item: Any
            reasons_item = reasons_item_data
            reasons.append(reasons_item)



        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)



        policy_version = self.policy_version

        evidence = self.evidence.to_dict()

        simulated = self.simulated

        mandate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mandate, Unset):
            mandate = self.mandate.to_dict()

        authorization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorization, Unset):
            authorization = self.authorization.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "decision_id": decision_id,
            "outcome": outcome,
            "reasons": reasons,
            "checks": checks,
            "policy_version": policy_version,
            "evidence": evidence,
        })
        if simulated is not UNSET:
            field_dict["simulated"] = simulated
        if mandate is not UNSET:
            field_dict["mandate"] = mandate
        if authorization is not UNSET:
            field_dict["authorization"] = authorization

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authorization_artifact import AuthorizationArtifact # noqa: PLC0415
        from ..models.authorize_response_evidence import AuthorizeResponseEvidence # noqa: PLC0415
        from ..models.authorize_response_mandate import AuthorizeResponseMandate # noqa: PLC0415
        from ..models.check import Check # noqa: PLC0415
        d = dict(src_dict)
        decision_id = UUID(d.pop("decision_id"))




        outcome = AuthorizeResponseOutcome(d.pop("outcome"))




        reasons = []
        _reasons = d.pop("reasons")
        for reasons_item_data in (_reasons):
            def _parse_reasons_item(data: object) -> Any:
                return cast(Any, data)

            reasons_item = _parse_reasons_item(reasons_item_data)

            reasons.append(reasons_item)


        checks = []
        _checks = d.pop("checks")
        for checks_item_data in (_checks):
            checks_item = Check.from_dict(checks_item_data)



            checks.append(checks_item)


        policy_version = d.pop("policy_version")

        evidence = AuthorizeResponseEvidence.from_dict(d.pop("evidence"))




        simulated = d.pop("simulated", UNSET)

        _mandate = d.pop("mandate", UNSET)
        mandate: AuthorizeResponseMandate | Unset
        if isinstance(_mandate,  Unset):
            mandate = UNSET
        else:
            mandate = AuthorizeResponseMandate.from_dict(_mandate)




        _authorization = d.pop("authorization", UNSET)
        authorization: AuthorizationArtifact | Unset
        if isinstance(_authorization,  Unset):
            authorization = UNSET
        else:
            authorization = AuthorizationArtifact.from_dict(_authorization)




        authorize_response = cls(
            decision_id=decision_id,
            outcome=outcome,
            reasons=reasons,
            checks=checks,
            policy_version=policy_version,
            evidence=evidence,
            simulated=simulated,
            mandate=mandate,
            authorization=authorization,
        )


        authorize_response.additional_properties = d
        return authorize_response

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
