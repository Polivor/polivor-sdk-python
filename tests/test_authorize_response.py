import unittest

from polivor.generated.models.authorize_response import AuthorizeResponse

DECISION_ID = "9c1d0000-0000-4000-8000-000000000001"
EVIDENCE = {"id": "9c1d0000-0000-4000-8000-000000000002", "seq": 1}
DENIAL_CODES = {"AGENT_NOT_ENABLED", "OUTSIDE_AUTHORITY", "APPROVAL_REQUIRED", "UNAVAILABLE", "APPROVER_DENIED", "APPROVAL_EXPIRED"}


class AuthorizeResponseTest(unittest.TestCase):
    def test_a_refusal_carries_a_coarse_denial_with_a_retry_flag(self):
        answer = AuthorizeResponse.from_dict({"decision_id": DECISION_ID, "outcome": "DENY", "evidence": EVIDENCE,
                                              "denial": {"code": "UNAVAILABLE", "message": "Try again later.", "retryable": True}})
        self.assertEqual("UNAVAILABLE", answer.denial.code.value)
        self.assertTrue(answer.denial.retryable)

    def test_every_denial_code_of_the_contract_is_known(self):
        for code in DENIAL_CODES:
            answer = AuthorizeResponse.from_dict({"decision_id": DECISION_ID, "outcome": "DENY", "evidence": EVIDENCE,
                                                  "denial": {"code": code, "message": "m", "retryable": False}})
            self.assertEqual(code, answer.denial.code.value)

    def test_an_agent_answer_has_no_reasons_checks_or_policy_version(self):
        answer = AuthorizeResponse.from_dict({"decision_id": DECISION_ID, "outcome": "ALLOW", "evidence": EVIDENCE})
        for field in ("reasons", "checks", "policy_version"):
            self.assertFalse(hasattr(answer, field), field)
