from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_custom_data_request_public_dto_data import UpdateCustomDataRequestPublicDtoData


T = TypeVar("T", bound="UpdateCustomDataRequestPublicDto")


@_attrs_define
class UpdateCustomDataRequestPublicDto:
    """
    Attributes:
        data (UpdateCustomDataRequestPublicDtoData): The Custom data to be created Example: {'type': 'object',
            'required': ['comment_id', 'user', 'text'], 'properties': {'comment_id': {'type': 'number'}, 'user': {'type':
            'object', 'required': ['id', 'name', 'email', 'has_bought'], 'properties': {'id': {'type': 'number'}, 'name':
            {'type': 'string'}, 'email': {'type': 'string'}, 'has_bought': {'type': 'boolean'}}}, 'text': {'type':
            'string'}}}.
    """

    data: "UpdateCustomDataRequestPublicDtoData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_custom_data_request_public_dto_data import UpdateCustomDataRequestPublicDtoData

        d = dict(src_dict)
        data = UpdateCustomDataRequestPublicDtoData.from_dict(d.pop("data"))

        update_custom_data_request_public_dto = cls(
            data=data,
        )

        update_custom_data_request_public_dto.additional_properties = d
        return update_custom_data_request_public_dto

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
