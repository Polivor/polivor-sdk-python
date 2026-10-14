from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TemplateParams")



@_attrs_define
class TemplateParams:
    """ Which rules the generated Cedar contains. The mandate's own limits, scope and threshold are facts in the Cedar
    context;
    the template only chooses which rules apply. Omitted properties take their default.

        Attributes:
            scope (bool | Unset): permit requires debtor account, currency, beneficiary country and payment type inside the
                mandate scope Default: True.
            per_transaction_limit (bool | Unset):  Default: True.
            daily_limit (bool | Unset):  Default: True.
            monthly_limit (bool | Unset):  Default: True.
            approval_threshold (bool | Unset): forbid with approval when the amount exceeds the mandate's threshold Default:
                True.
            beneficiary_allowlist (bool | Unset): forbid with approval when the beneficiary is not on the allowlist Default:
                True.
            blocked_beneficiary (bool | Unset): Hard deny for an explicitly blocked beneficiary; never payable by approval
                Default: True.
            iban_mismatch (bool | Unset): forbid with approval when an allowlisted beneficiary's IBAN differs Default: True.
            risk_signals (list[str] | Unset): Agent-reported risk flags that escalate to approval. Empty turns the rule off.
                Signals only ever tighten.
     """

    scope: bool | Unset = True
    per_transaction_limit: bool | Unset = True
    daily_limit: bool | Unset = True
    monthly_limit: bool | Unset = True
    approval_threshold: bool | Unset = True
    beneficiary_allowlist: bool | Unset = True
    blocked_beneficiary: bool | Unset = True
    iban_mismatch: bool | Unset = True
    risk_signals: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        per_transaction_limit = self.per_transaction_limit

        daily_limit = self.daily_limit

        monthly_limit = self.monthly_limit

        approval_threshold = self.approval_threshold

        beneficiary_allowlist = self.beneficiary_allowlist

        blocked_beneficiary = self.blocked_beneficiary

        iban_mismatch = self.iban_mismatch

        risk_signals: list[str] | Unset = UNSET
        if not isinstance(self.risk_signals, Unset):
            risk_signals = self.risk_signals




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if scope is not UNSET:
            field_dict["scope"] = scope
        if per_transaction_limit is not UNSET:
            field_dict["per_transaction_limit"] = per_transaction_limit
        if daily_limit is not UNSET:
            field_dict["daily_limit"] = daily_limit
        if monthly_limit is not UNSET:
            field_dict["monthly_limit"] = monthly_limit
        if approval_threshold is not UNSET:
            field_dict["approval_threshold"] = approval_threshold
        if beneficiary_allowlist is not UNSET:
            field_dict["beneficiary_allowlist"] = beneficiary_allowlist
        if blocked_beneficiary is not UNSET:
            field_dict["blocked_beneficiary"] = blocked_beneficiary
        if iban_mismatch is not UNSET:
            field_dict["iban_mismatch"] = iban_mismatch
        if risk_signals is not UNSET:
            field_dict["risk_signals"] = risk_signals

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope = d.pop("scope", UNSET)

        per_transaction_limit = d.pop("per_transaction_limit", UNSET)

        daily_limit = d.pop("daily_limit", UNSET)

        monthly_limit = d.pop("monthly_limit", UNSET)

        approval_threshold = d.pop("approval_threshold", UNSET)

        beneficiary_allowlist = d.pop("beneficiary_allowlist", UNSET)

        blocked_beneficiary = d.pop("blocked_beneficiary", UNSET)

        iban_mismatch = d.pop("iban_mismatch", UNSET)

        risk_signals = cast(list[str], d.pop("risk_signals", UNSET))


        template_params = cls(
            scope=scope,
            per_transaction_limit=per_transaction_limit,
            daily_limit=daily_limit,
            monthly_limit=monthly_limit,
            approval_threshold=approval_threshold,
            beneficiary_allowlist=beneficiary_allowlist,
            blocked_beneficiary=blocked_beneficiary,
            iban_mismatch=iban_mismatch,
            risk_signals=risk_signals,
        )

        return template_params

