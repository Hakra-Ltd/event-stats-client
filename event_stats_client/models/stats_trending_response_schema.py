# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from event_stats_client.models.trending_event import TrendingEvent
from typing import Optional, Set
from typing_extensions import Self

class StatsTrendingResponseSchema(BaseModel):
    """
    StatsTrendingResponseSchema
    """ # noqa: E501
    added: List[TrendingEvent]
    removed: List[TrendingEvent]
    changed: List[TrendingEvent]
    __properties: ClassVar[List[str]] = ["added", "removed", "changed"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StatsTrendingResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in added (list)
        _items = []
        if self.added:
            for _item_added in self.added:
                if _item_added:
                    _items.append(_item_added.to_dict())
            _dict['added'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in removed (list)
        _items = []
        if self.removed:
            for _item_removed in self.removed:
                if _item_removed:
                    _items.append(_item_removed.to_dict())
            _dict['removed'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in changed (list)
        _items = []
        if self.changed:
            for _item_changed in self.changed:
                if _item_changed:
                    _items.append(_item_changed.to_dict())
            _dict['changed'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StatsTrendingResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "added": [TrendingEvent.from_dict(_item) for _item in obj["added"]] if obj.get("added") is not None else None,
            "removed": [TrendingEvent.from_dict(_item) for _item in obj["removed"]] if obj.get("removed") is not None else None,
            "changed": [TrendingEvent.from_dict(_item) for _item in obj["changed"]] if obj.get("changed") is not None else None
        })
        return _obj


