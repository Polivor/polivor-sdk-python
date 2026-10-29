# polivor

[![PyPI](https://img.shields.io/pypi/v/polivor)](https://pypi.org/project/polivor/) [![ci](https://github.com/Polivor/polivor-sdk-python/actions/workflows/ci.yml/badge.svg)](https://github.com/Polivor/polivor-sdk-python/actions/workflows/ci.yml) [![license](https://img.shields.io/github/license/Polivor/polivor-sdk-python)](LICENSE) [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/Polivor/polivor-sdk-python/badge)](https://scorecard.dev/viewer/?uri=github.com/Polivor/polivor-sdk-python)

Python client for the Polivor API, generated from its OpenAPI file. The package holds no keys or secrets: you bring your own API key.

```python
from polivor import create_client, verify_authorization
from polivor.generated.api.authorize import authorize

client = create_client()  # reads POLIVOR_API_KEY, or pass api_key="..."
result = authorize.sync(client=client, body=body, idempotency_key=key)

# Enforcement point: no API key needed, only Polivor's public keys.
claims = verify_authorization(result.authorization.jws, audience="your-enforcement-point")
```

- Keys have a role: `agent` (ask for authority), `enforcer` (report execution), `admin` (manage). Give each component only its own role, and never put an `admin` key in browser or mobile code.
- Keys starting with `pv_test_` are sandbox keys. Polivor decides and records; it never moves money.
- Base URLs: `PRODUCTION_BASE_URL`, `STAGING_BASE_URL`; pass `base_url` to choose.

## Upgrading from 0.1.0

0.1.0 was generated from an API description that is out of date: it still has agent versions and `mandate_id` in the authorize request. Use 0.2.0 or later against the current API. Main differences:

- `POST /v1/authorize` answers an agent with `denial` (`code`, `message`, `retryable`) when nothing was allowed. The codes are `AGENT_NOT_ENABLED`, `OUTSIDE_AUTHORITY`, `APPROVAL_REQUIRED`, `UNAVAILABLE`, `APPROVER_DENIED` and `APPROVAL_EXPIRED`. An agent's answer has no `reasons`, `checks` or `policy_version`; a person sees them through an admin key, the console or the evidence.
- An agent has no versions and one mandate, so the request names no mandate. Mandate versions are `major.minor` strings. An agent is created with `owner_person_id`.
- New endpoints for people, users and identity providers.

The list of every change is in the pull request that regenerated the client.

## Development

`openapi/polivor.yaml` is a copy of the published API description. A scheduled workflow refreshes it and opens a pull request when it changes. Generated code is never edited by hand.

## License

Apache-2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE).
