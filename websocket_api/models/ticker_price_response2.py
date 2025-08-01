# coding: utf-8

"""
Binance Spot WebSocket API

OpenAPI Specifications for the Binance Spot WebSocket API

API documents:
  - [Github web-socket-api documentation file](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-api.md)
  - [General API information for web-socket-api on website](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-api/general-api-information)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Self

from .rate_limits_inner import RateLimitsInner
from .ticker_price_response2_result_inner import TickerPriceResponse2ResultInner


class TickerPriceResponse2(BaseModel):
    """
    TickerPriceResponse2
    """  # noqa: E501

    id: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    result: Optional[List[TickerPriceResponse2ResultInner]] = Field(
        default=None, alias="result"
    )

    rate_limits: Optional[List[RateLimitsInner]] = Field(
        default=None, alias="rateLimits"
    )

    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "status", "result", "rateLimits"]

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
    def is_array(cls) -> bool:
        return False

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TickerPriceResponse2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set(
            [
                "additional_properties",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in result (list)
        _items = []
        if self.result:
            for _item_result in self.result:
                if _item_result:
                    _items.append(_item_result.to_dict())
            _dict["result"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rate_limits (list)
        _items = []
        if self.rate_limits:
            for _item_rate_limits in self.rate_limits:
                if _item_rate_limits:
                    _items.append(_item_rate_limits.to_dict())
            _dict["rateLimits"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TickerPriceResponse2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "status": obj.get("status"),
                "result": (
                    [
                        TickerPriceResponse2ResultInner.from_dict(_item)
                        for _item in obj["result"]
                    ]
                    if obj.get("result") is not None
                    else None
                ),
                "rateLimits": (
                    [RateLimitsInner.from_dict(_item) for _item in obj["rateLimits"]]
                    if obj.get("rateLimits") is not None
                    else None
                ),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
