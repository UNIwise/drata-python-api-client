from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient
from ...models.create_control_note_request_public_dto import CreateControlNoteRequestPublicDto
from ...models.exception_response_dto import ExceptionResponseDto
from ...models.exception_response_public_dto import ExceptionResponsePublicDto
from ...models.note_response_public_dto import NoteResponsePublicDto
from ...types import Response


def _get_kwargs(
    workspace_id: float,
    control_id: float,
    *,
    body: CreateControlNoteRequestPublicDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/workspaces/{workspace_id}/controls/{control_id}/notes",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]]:
    if response.status_code == 201:
        response_201 = NoteResponsePublicDto.from_dict(response.json())

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
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: float,
    control_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateControlNoteRequestPublicDto,
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]]:
    """Create a control note

     Create a note for a given control

    Args:
        workspace_id (float):
        control_id (float):
        body (CreateControlNoteRequestPublicDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        control_id=control_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: float,
    control_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateControlNoteRequestPublicDto,
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]]:
    """Create a control note

     Create a note for a given control

    Args:
        workspace_id (float):
        control_id (float):
        body (CreateControlNoteRequestPublicDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        control_id=control_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: float,
    control_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateControlNoteRequestPublicDto,
) -> Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]]:
    """Create a control note

     Create a note for a given control

    Args:
        workspace_id (float):
        control_id (float):
        body (CreateControlNoteRequestPublicDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        control_id=control_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: float,
    control_id: float,
    *,
    client: AuthenticatedClient,
    body: CreateControlNoteRequestPublicDto,
) -> Optional[Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]]:
    """Create a control note

     Create a note for a given control

    Args:
        workspace_id (float):
        control_id (float):
        body (CreateControlNoteRequestPublicDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExceptionResponseDto, ExceptionResponsePublicDto, NoteResponsePublicDto]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            control_id=control_id,
            client=client,
            body=body,
        )
    ).parsed
