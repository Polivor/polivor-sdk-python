from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem import Problem
from ...models.webhook_configured import WebhookConfigured
from ...models.webhook_set import WebhookSet
from typing import cast



def _get_kwargs(
    *,
    body: WebhookSet,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Problem | WebhookConfigured | None:
    if response.status_code == 200:
        response_200 = WebhookConfigured.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Problem | WebhookConfigured]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookSet,

) -> Response[Problem | WebhookConfigured]:
    """ Set the webhook URL and create a new signing secret, shown once (role admin)

     Events: `decision.resolved` (an approval ended: ALLOWED with the authorization, or DENIED with a
    reason), `authorization.reported`
    (an execution report or an admin release) and `webhook.test`. Each delivery is `POST` with the JSON
    body
    `{id, type, created_at, tenant_id, data}` and the headers `Polivor-Event-Id` and `Polivor-Signature:
    t=<unix seconds>,v1=<hex>`, where
    v1 is HMAC-SHA256 of `<t>.<raw body>` with the secret. Reject deliveries whose `t` is far from your
    clock. Any 2xx is success; other
    results are retried 5 times with backoff (1 min, 5 min, 15 min, 1 h, 6 h) and the same event ID. The
    URL must be HTTPS and public.

    Args:
        body (WebhookSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookConfigured]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookSet,

) -> Problem | WebhookConfigured | None:
    """ Set the webhook URL and create a new signing secret, shown once (role admin)

     Events: `decision.resolved` (an approval ended: ALLOWED with the authorization, or DENIED with a
    reason), `authorization.reported`
    (an execution report or an admin release) and `webhook.test`. Each delivery is `POST` with the JSON
    body
    `{id, type, created_at, tenant_id, data}` and the headers `Polivor-Event-Id` and `Polivor-Signature:
    t=<unix seconds>,v1=<hex>`, where
    v1 is HMAC-SHA256 of `<t>.<raw body>` with the secret. Reject deliveries whose `t` is far from your
    clock. Any 2xx is success; other
    results are retried 5 times with backoff (1 min, 5 min, 15 min, 1 h, 6 h) and the same event ID. The
    URL must be HTTPS and public.

    Args:
        body (WebhookSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookConfigured
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookSet,

) -> Response[Problem | WebhookConfigured]:
    """ Set the webhook URL and create a new signing secret, shown once (role admin)

     Events: `decision.resolved` (an approval ended: ALLOWED with the authorization, or DENIED with a
    reason), `authorization.reported`
    (an execution report or an admin release) and `webhook.test`. Each delivery is `POST` with the JSON
    body
    `{id, type, created_at, tenant_id, data}` and the headers `Polivor-Event-Id` and `Polivor-Signature:
    t=<unix seconds>,v1=<hex>`, where
    v1 is HMAC-SHA256 of `<t>.<raw body>` with the secret. Reject deliveries whose `t` is far from your
    clock. Any 2xx is success; other
    results are retried 5 times with backoff (1 min, 5 min, 15 min, 1 h, 6 h) and the same event ID. The
    URL must be HTTPS and public.

    Args:
        body (WebhookSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookConfigured]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookSet,

) -> Problem | WebhookConfigured | None:
    """ Set the webhook URL and create a new signing secret, shown once (role admin)

     Events: `decision.resolved` (an approval ended: ALLOWED with the authorization, or DENIED with a
    reason), `authorization.reported`
    (an execution report or an admin release) and `webhook.test`. Each delivery is `POST` with the JSON
    body
    `{id, type, created_at, tenant_id, data}` and the headers `Polivor-Event-Id` and `Polivor-Signature:
    t=<unix seconds>,v1=<hex>`, where
    v1 is HMAC-SHA256 of `<t>.<raw body>` with the secret. Reject deliveries whose `t` is far from your
    clock. Any 2xx is success; other
    results are retried 5 times with backoff (1 min, 5 min, 15 min, 1 h, 6 h) and the same event ID. The
    URL must be HTTPS and public.

    Args:
        body (WebhookSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookConfigured
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
