import jwt

from .client import PRODUCTION_BASE_URL

AUTHORIZATION_TOKEN_TYPE = "polivor-authz+jwt"
AUTHORIZATION_SIGNING_ALGORITHM = "EdDSA"
JWKS_PATH = "/.well-known/jwks.json"


def verify_authorization(token: str, audience: str, base_url: str = PRODUCTION_BASE_URL, jwks: dict | None = None) -> dict:
    """Checks signature, algorithm, token type, audience and expiry of an authorization artifact with Polivor's public keys; needs no API key."""
    header = jwt.get_unverified_header(token)
    if header.get("typ") != AUTHORIZATION_TOKEN_TYPE:
        raise jwt.InvalidTokenError("unexpected token type")
    if jwks is not None:
        signing_key = jwt.PyJWKSet.from_dict(jwks)[header["kid"]].key
    else:
        signing_key = jwt.PyJWKClient(base_url.rstrip("/") + JWKS_PATH).get_signing_key_from_jwt(token).key
    return jwt.decode(token, signing_key, algorithms=[AUTHORIZATION_SIGNING_ALGORITHM], audience=audience,
                      options={"require": ["exp", "aud"]})
