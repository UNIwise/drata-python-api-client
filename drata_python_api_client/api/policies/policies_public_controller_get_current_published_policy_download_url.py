from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...models.exception_response_dto import ExceptionResponseDto
from ...models.exception_response_public_dto import ExceptionResponsePublicDto
from ...models.user_signed_url_response_public_dto import UserSignedUrlResponsePublicDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: float,
    *,
    with_appendix: Union[None, Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_with_appendix: Union[None, Unset, bool]
    if isinstance(with_appendix, Unset):
        json_with_appendix = UNSET
    else:
        json_with_appendix = with_appendix
    params["withAppendix"] = json_with_appendix

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/policies/{id}/current-published/download",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]]:
    if response.status_code == 200:
        response_200 = UserSignedUrlResponsePublicDto.from_dict(response.json())

        return response_200
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
    *, client: AuthenticatedClient, response: httpx.Response
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: float,
    *,
    client: AuthenticatedClient,
    with_appendix: Union[None, Unset, bool] = False,
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]]:
    """Get signed URL of a policy's current published version

     Returns the signed URL of a policy's current published version, used to download the document

    Args:
        id (float):
        with_appendix (Union[None, Unset, bool]):  Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]]
    """

    kwargs = _get_kwargs(
        id=id,
        with_appendix=with_appendix,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: float,
    *,
    client: AuthenticatedClient,
    with_appendix: Union[None, Unset, bool] = False,
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]]:
    """Get signed URL of a policy's current published version

     Returns the signed URL of a policy's current published version, used to download the document

    Args:
        id (float):
        with_appendix (Union[None, Unset, bool]):  Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]
    """

    return sync_detailed(
        id=id,
        client=client,
        with_appendix=with_appendix,
    ).parsed


async def asyncio_detailed(
    id: float,
    *,
    client: AuthenticatedClient,
    with_appendix: Union[None, Unset, bool] = False,
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]]:
    """Get signed URL of a policy's current published version

     Returns the signed URL of a policy's current published version, used to download the document

    Args:
        id (float):
        with_appendix (Union[None, Unset, bool]):  Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]]
    """

    kwargs = _get_kwargs(
        id=id,
        with_appendix=with_appendix,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: float,
    *,
    client: AuthenticatedClient,
    with_appendix: Union[None, Unset, bool] = False,
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]]:
    """Get signed URL of a policy's current published version

     Returns the signed URL of a policy's current published version, used to download the document

    Args:
        id (float):
        with_appendix (Union[None, Unset, bool]):  Default: False. Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponseDto, ExceptionResponsePublicDto, UserSignedUrlResponsePublicDto]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            with_appendix=with_appendix,
        )
    ).parsed
