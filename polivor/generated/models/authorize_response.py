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
  from ..models.denial import Denial





T = TypeVar("T", bound="AuthorizeResponse")



@_attrs_define
class AuthorizeResponse:
    """ The answer to an agent. It has no reasons, no checks and no policy version; a person sees those through the admin
    key, the console or the evidence.

        Attributes:
            decision_id (UUID):
            outcome (AuthorizeResponseOutcome):
            evidence (AuthorizeResponseEvidence):
            denial (Denial | Unset): What an agent is told when nothing was allowed. The list of codes is closed and each
                sentence says what to do, never why.
                `retryable` is true only when sending the same request again later, with nothing else changed, may succeed
                (UNAVAILABLE).
            mandate (AuthorizeResponseMandate | Unset):
            authorization (AuthorizationArtifact | Unset):
     """

    decision_id: UUID
    outcome: AuthorizeResponseOutcome
    evidence: AuthorizeResponseEvidence
    denial: Denial | Unset = UNSET
    mandate: AuthorizeResponseMandate | Unset = UNSET
    authorization: AuthorizationArtifact | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.authorization_artifact import AuthorizationArtifact # noqa: PLC0415
        from ..models.authorize_response_evidence import AuthorizeResponseEvidence # noqa: PLC0415
        from ..models.authorize_response_mandate import AuthorizeResponseMandate # noqa: PLC0415
        from ..models.denial import Denial # noqa: PLC0415
        decision_id = str(self.decision_id)

        outcome = self.outcome.value

        evidence = self.evidence.to_dict()

        denial: dict[str, Any] | Unset = UNSET
        if not isinstance(self.denial, Unset):
            denial = self.denial.to_dict()

        mandate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mandate, Unset):
            mandate = self.mandate.to_dict()

        authorization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorization, Unset):
            authorization = self.authorization.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "decision_id": decision_id,
            "outcome": outcome,
            "evidence": evidence,
        })
        if denial is not UNSET:
            field_dict["denial"] = denial
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
        from ..models.denial import Denial # noqa: PLC0415
        d = dict(src_dict)
        decision_id = UUID(d.pop("decision_id"))




        outcome = AuthorizeResponseOutcome(d.pop("outcome"))




        evidence = AuthorizeResponseEvidence.from_dict(d.pop("evidence"))




        _denial = d.pop("denial", UNSET)
        denial: Denial | Unset
        if isinstance(_denial,  Unset):
            denial = UNSET
        else:
            denial = Denial.from_dict(_denial)




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
            evidence=evidence,
            denial=denial,
            mandate=mandate,
            authorization=authorization,
        )

        return authorize_response

