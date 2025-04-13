from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateDeviceRequestPublicDtoPasswordManagerExplanation")


@_attrs_define
class CreateDeviceRequestPublicDtoPasswordManagerExplanation:
    """Any additional information to explain the hasPasswordManager value

    Example:
        {'passwordManagerApps': ['1password']}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_device_request_public_dto_password_manager_explanation = cls()

        create_device_request_public_dto_password_manager_explanation.additional_properties = d
        return create_device_request_public_dto_password_manager_explanation

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
