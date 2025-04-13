from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.requirement_list_response_public_dto import RequirementListResponsePublicDto


T = TypeVar("T", bound="RequirementPaginatedResponsePublicDto")


@_attrs_define
class RequirementPaginatedResponsePublicDto:
    """
    Attributes:
        page (float): Which page of data are you requesting Example: 1.
        limit (float): How many items are you requesting Example: 10.
        total (float): How many items are in the overall set Example: 100.
        data (Union[Unset, list['RequirementListResponsePublicDto']]): Requirements associated to the framework.
    """

    page: float
    limit: float
    total: float
    data: Union[Unset, list["RequirementListResponsePublicDto"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        limit = self.limit

        total = self.total

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "limit": limit,
                "total": total,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.requirement_list_response_public_dto import RequirementListResponsePublicDto

        d = dict(src_dict)
        page = d.pop("page")

        limit = d.pop("limit")

        total = d.pop("total")

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = RequirementListResponsePublicDto.from_dict(data_item_data)

            data.append(data_item)

        requirement_paginated_response_public_dto = cls(
            page=page,
            limit=limit,
            total=total,
            data=data,
        )

        requirement_paginated_response_public_dto.additional_properties = d
        return requirement_paginated_response_public_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
