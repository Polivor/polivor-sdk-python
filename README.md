# polivor

[![ci](https://github.com/Polivor/polivor-sdk-python/actions/workflows/ci.yml/badge.svg)](https://github.com/Polivor/polivor-sdk-python/actions/workflows/ci.yml) [![license](https://img.shields.io/github/license/Polivor/polivor-sdk-python)](LICENSE)

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

## Development

`openapi/polivor.yaml` is a copy of the published API description. A scheduled workflow refreshes it and opens a pull request when it changes. Generated code is never edited by hand.

## License

Apache-2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE).
