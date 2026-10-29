import httpx
import jwt

from .client import PRODUCTION_BASE_URL

AUTHORIZATION_TOKEN_TYPE = "polivor-authz+jwt"
AUTHORIZATION_SIGNING_ALGORITHM = "EdDSA"
JWKS_PATH = "/.well-known/jwks.json"
AUTHORIZATION_KEY_USE = "authz"
AUTHORIZATION_KEY_CURVE = "Ed25519"
KEY_SET_TIMEOUT_SECONDS = 10


def fetch_key_set(base_url: str) -> dict:
    response = httpx.get(base_url.rstrip("/") + JWKS_PATH, timeout=KEY_SET_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def authorization_key(key_set: dict, key_id: str | None):
    """Polivor labels its keys use "authz" and use "evidence", not the standard "sig", so PyJWKClient skips every one of them; the key is picked by its id and by that use."""
    for entry in key_set.get("keys", []):
        if entry.get("kid") == key_id and entry.get("use") == AUTHORIZATION_KEY_USE and entry.get("crv") == AUTHORIZATION_KEY_CURVE:
            return jwt.PyJWK.from_dict({name: entry[name] for name in ("kty", "crv", "x")}).key
    raise jwt.InvalidKeyError(f"no authorization key with id {key_id}")


def verify_authorization(token: str, audience: str, base_url: str = PRODUCTION_BASE_URL, jwks: dict | None = None) -> dict:
    """Checks signature, algorithm, token type, audience and expiry of an authorization artifact with Polivor's public keys; needs no API key."""
    header = jwt.get_unverified_header(token)
    if header.get("typ") != AUTHORIZATION_TOKEN_TYPE:
        raise jwt.InvalidTokenError("unexpected token type")
    signing_key = authorization_key(jwks if jwks is not None else fetch_key_set(base_url), header.get("kid"))
    return jwt.decode(token, signing_key, algorithms=[AUTHORIZATION_SIGNING_ALGORITHM], audience=audience,
                      options={"require": ["exp", "aud"]})
