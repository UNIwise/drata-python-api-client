from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exception_response_dto import ExceptionResponseDto
from ...models.exception_response_public_dto import ExceptionResponsePublicDto
from ...models.manual_background_check_request_public_dto import ManualBackgroundCheckRequestPublicDto
from ...models.personnel_details_response_public_dto import PersonnelDetailsResponsePublicDto
from ...types import Response


def _get_kwargs(
    user_id: float,
    *,
    body: ManualBackgroundCheckRequestPublicDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/background-check/{user_id}/manual",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]]:
    if response.status_code == 201:
        response_201 = PersonnelDetailsResponsePublicDto.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ExceptionResponsePublicDto.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ExceptionResponseDto.from_dict(response.json())

        return response_401
    if response.status_code == 402:
        response_402 = ExceptionResponseDto.from_dict(response.json())

        return response_402
    if response.status_code == 403:
        response_403 = ExceptionResponseDto.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ExceptionResponsePublicDto.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = ExceptionResponsePublicDto.from_dict(response.json())

        return response_409
    if response.status_code == 412:
        response_412 = ExceptionResponseDto.from_dict(response.json())

        return response_412
    if response.status_code == 500:
        response_500 = ExceptionResponseDto.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: float,
    *,
    client: AuthenticatedClient,
    body: ManualBackgroundCheckRequestPublicDto,
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]]:
    """Upload a background check evidence to a user

     Manually upload a background check URL for a user

    Args:
        user_id (float):
        body (ManualBackgroundCheckRequestPublicDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: float,
    *,
    client: AuthenticatedClient,
    body: ManualBackgroundCheckRequestPublicDto,
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]]:
    """Upload a background check evidence to a user

     Manually upload a background check URL for a user

    Args:
        user_id (float):
        body (ManualBackgroundCheckRequestPublicDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: float,
    *,
    client: AuthenticatedClient,
    body: ManualBackgroundCheckRequestPublicDto,
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]]:
    """Upload a background check evidence to a user

     Manually upload a background check URL for a user

    Args:
        user_id (float):
        body (ManualBackgroundCheckRequestPublicDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: float,
    *,
    client: AuthenticatedClient,
    body: ManualBackgroundCheckRequestPublicDto,
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]]:
    """Upload a background check evidence to a user

     Manually upload a background check URL for a user

    Args:
        user_id (float):
        body (ManualBackgroundCheckRequestPublicDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponseDto, ExceptionResponsePublicDto, PersonnelDetailsResponsePublicDto]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
