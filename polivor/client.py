import os

from .generated import AuthenticatedClient

PRODUCTION_BASE_URL = "https://api.polivor.com"
STAGING_BASE_URL = "https://api.staging.polivor.com"
API_KEY_ENVIRONMENT_VARIABLE = "POLIVOR_API_KEY"


def create_client(api_key: str | None = None, base_url: str = PRODUCTION_BASE_URL) -> AuthenticatedClient:
    resolved_key = api_key or os.environ.get(API_KEY_ENVIRONMENT_VARIABLE)
    if not resolved_key:
        raise ValueError(f"Polivor API key missing: pass api_key or set {API_KEY_ENVIRONMENT_VARIABLE}")
    return AuthenticatedClient(base_url=base_url, token=resolved_key)
