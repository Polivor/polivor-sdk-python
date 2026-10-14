import json
import os
import time
import unittest
from base64 import urlsafe_b64encode

import httpx
import jwt
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from polivor import API_KEY_ENVIRONMENT_VARIABLE, PRODUCTION_BASE_URL, create_client, verify_authorization
from polivor.generated.api.keys import list_api_keys

API_KEY = "pv_test_abc_secret"
AUDIENCE = "hub"
KEY_ID = "authz-1"
TOKEN_TYPE = "polivor-authz+jwt"


def signed_token(token_type=TOKEN_TYPE, audience=AUDIENCE, lifetime_seconds=300):
    private_key = Ed25519PrivateKey.generate()
    raw_public = private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
    jwks = {"keys": [{"kty": "OKP", "crv": "Ed25519", "kid": KEY_ID, "alg": "EdDSA",
                      "x": urlsafe_b64encode(raw_public).rstrip(b"=").decode()}]}
    claims = {"aud": audience, "exp": int(time.time()) + lifetime_seconds, "action_sha256": "abc"}
    token = jwt.encode(claims, private_key, algorithm="EdDSA", headers={"typ": token_type, "kid": KEY_ID})
    return token, jwks


class ClientTest(unittest.TestCase):
    def setUp(self):
        os.environ.pop(API_KEY_ENVIRONMENT_VARIABLE, None)

    def tearDown(self):
        os.environ.pop(API_KEY_ENVIRONMENT_VARIABLE, None)

    def call_list_keys(self, client):
        seen = []

        def handler(request: httpx.Request) -> httpx.Response:
            seen.append(request)
            return httpx.Response(200, json=[])

        client.set_httpx_client(httpx.Client(base_url=PRODUCTION_BASE_URL, transport=httpx.MockTransport(handler),
                                             headers={"Authorization": f"Bearer {client.token}"}))
        list_api_keys.sync_detailed(client=client)
        return seen

    def test_sends_the_api_key_as_a_bearer_token(self):
        seen = self.call_list_keys(create_client(api_key=API_KEY))
        self.assertEqual(seen[0].headers["authorization"], f"Bearer {API_KEY}")
        self.assertEqual(seen[0].url.path, "/v1/keys")

    def test_reads_the_api_key_from_the_environment(self):
        os.environ[API_KEY_ENVIRONMENT_VARIABLE] = "pv_test_env_secret"
        seen = self.call_list_keys(create_client())
        self.assertEqual(seen[0].headers["authorization"], "Bearer pv_test_env_secret")

    def test_refuses_to_build_a_client_without_any_api_key(self):
        with self.assertRaises(ValueError):
            create_client()


class VerifyAuthorizationTest(unittest.TestCase):
    def test_accepts_a_valid_authorization_and_returns_its_claims(self):
        token, jwks = signed_token()
        self.assertEqual(verify_authorization(token, AUDIENCE, jwks=jwks)["action_sha256"], "abc")

    def test_rejects_wrong_audience_type_expiry_and_changed_claims(self):
        for token_type, audience, lifetime in [(TOKEN_TYPE, "other", 300), ("polivor-evidence+jwt", AUDIENCE, 300), (TOKEN_TYPE, AUDIENCE, -60)]:
            token, jwks = signed_token(token_type, audience, lifetime)
            with self.assertRaises(jwt.InvalidTokenError):
                verify_authorization(token, AUDIENCE, jwks=jwks)
        token, jwks = signed_token()
        header, _, signature = token.split(".")
        forged_payload = urlsafe_b64encode(json.dumps({"aud": AUDIENCE, "exp": 9999999999, "action_sha256": "evil"}).encode()).rstrip(b"=").decode()
        with self.assertRaises(jwt.InvalidTokenError):
            verify_authorization(f"{header}.{forged_payload}.{signature}", AUDIENCE, jwks=jwks)


if __name__ == "__main__":
    unittest.main()
