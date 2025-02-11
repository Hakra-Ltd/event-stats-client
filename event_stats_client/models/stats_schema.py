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

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from event_stats_client.models.summary_schema import SummarySchema
from event_stats_client.models.volatility_metrics import VolatilityMetrics
from typing import Optional, Set
from typing_extensions import Self

class StatsSchema(BaseModel):
    """
    StatsSchema
    """ # noqa: E501
    timestamp: datetime
    available: Optional[SummarySchema] = None
    changed: Optional[SummarySchema] = None
    removed: Optional[SummarySchema] = None
    added: Optional[SummarySchema] = None
    volatility_metrics: VolatilityMetrics
    __properties: ClassVar[List[str]] = ["timestamp", "available", "changed", "removed", "added", "volatility_metrics"]

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
        """Create an instance of StatsSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of available
        if self.available:
            _dict['available'] = self.available.to_dict()
        # override the default output from pydantic by calling `to_dict()` of changed
        if self.changed:
            _dict['changed'] = self.changed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of removed
        if self.removed:
            _dict['removed'] = self.removed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of added
        if self.added:
            _dict['added'] = self.added.to_dict()
        # override the default output from pydantic by calling `to_dict()` of volatility_metrics
        if self.volatility_metrics:
            _dict['volatility_metrics'] = self.volatility_metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StatsSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "available": SummarySchema.from_dict(obj["available"]) if obj.get("available") is not None else None,
            "changed": SummarySchema.from_dict(obj["changed"]) if obj.get("changed") is not None else None,
            "removed": SummarySchema.from_dict(obj["removed"]) if obj.get("removed") is not None else None,
            "added": SummarySchema.from_dict(obj["added"]) if obj.get("added") is not None else None,
            "volatility_metrics": VolatilityMetrics.from_dict(obj["volatility_metrics"]) if obj.get("volatility_metrics") is not None else None
        })
        return _obj


