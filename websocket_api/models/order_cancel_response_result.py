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

from .open_orders_cancel_all_response_result_inner_order_reports_inner import (
    OpenOrdersCancelAllResponseResultInnerOrderReportsInner,
)
from .open_orders_cancel_all_response_result_inner_orders_inner import (
    OpenOrdersCancelAllResponseResultInnerOrdersInner,
)


class OrderCancelResponseResult(BaseModel):
    """
    OrderCancelResponseResult
    """  # noqa: E501

    symbol: Optional[StrictStr] = None
    orig_client_order_id: Optional[StrictStr] = Field(
        default=None, alias="origClientOrderId"
    )
    order_id: Optional[StrictInt] = Field(default=None, alias="orderId")
    order_list_id: Optional[StrictInt] = Field(default=None, alias="orderListId")
    client_order_id: Optional[StrictStr] = Field(default=None, alias="clientOrderId")
    transact_time: Optional[StrictInt] = Field(default=None, alias="transactTime")
    price: Optional[StrictStr] = None
    orig_qty: Optional[StrictStr] = Field(default=None, alias="origQty")
    executed_qty: Optional[StrictStr] = Field(default=None, alias="executedQty")
    orig_quote_order_qty: Optional[StrictStr] = Field(
        default=None, alias="origQuoteOrderQty"
    )
    cummulative_quote_qty: Optional[StrictStr] = Field(
        default=None, alias="cummulativeQuoteQty"
    )
    status: Optional[StrictStr] = None
    time_in_force: Optional[StrictStr] = Field(default=None, alias="timeInForce")
    type: Optional[StrictStr] = None
    side: Optional[StrictStr] = None
    stop_price: Optional[StrictStr] = Field(default=None, alias="stopPrice")
    trailing_delta: Optional[StrictInt] = Field(default=None, alias="trailingDelta")
    iceberg_qty: Optional[StrictStr] = Field(default=None, alias="icebergQty")
    strategy_id: Optional[StrictInt] = Field(default=None, alias="strategyId")
    strategy_type: Optional[StrictInt] = Field(default=None, alias="strategyType")
    self_trade_prevention_mode: Optional[StrictStr] = Field(
        default=None, alias="selfTradePreventionMode"
    )
    contingency_type: Optional[StrictStr] = Field(default=None, alias="contingencyType")
    list_status_type: Optional[StrictStr] = Field(default=None, alias="listStatusType")
    list_order_status: Optional[StrictStr] = Field(
        default=None, alias="listOrderStatus"
    )
    list_client_order_id: Optional[StrictStr] = Field(
        default=None, alias="listClientOrderId"
    )
    transaction_time: Optional[StrictInt] = Field(default=None, alias="transactionTime")
    orders: Optional[List[OpenOrdersCancelAllResponseResultInnerOrdersInner]] = Field(
        default=None, alias="orders"
    )

    order_reports: Optional[
        List[OpenOrdersCancelAllResponseResultInnerOrderReportsInner]
    ] = Field(default=None, alias="orderReports")

    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "symbol",
        "origClientOrderId",
        "orderId",
        "orderListId",
        "clientOrderId",
        "transactTime",
        "price",
        "origQty",
        "executedQty",
        "origQuoteOrderQty",
        "cummulativeQuoteQty",
        "status",
        "timeInForce",
        "type",
        "side",
        "stopPrice",
        "trailingDelta",
        "icebergQty",
        "strategyId",
        "strategyType",
        "selfTradePreventionMode",
        "contingencyType",
        "listStatusType",
        "listOrderStatus",
        "listClientOrderId",
        "transactionTime",
        "orders",
        "orderReports",
    ]

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
        """Create an instance of OrderCancelResponseResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in orders (list)
        _items = []
        if self.orders:
            for _item_orders in self.orders:
                if _item_orders:
                    _items.append(_item_orders.to_dict())
            _dict["orders"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in order_reports (list)
        _items = []
        if self.order_reports:
            for _item_order_reports in self.order_reports:
                if _item_order_reports:
                    _items.append(_item_order_reports.to_dict())
            _dict["orderReports"] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCancelResponseResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "symbol": obj.get("symbol"),
                "origClientOrderId": obj.get("origClientOrderId"),
                "orderId": obj.get("orderId"),
                "orderListId": obj.get("orderListId"),
                "clientOrderId": obj.get("clientOrderId"),
                "transactTime": obj.get("transactTime"),
                "price": obj.get("price"),
                "origQty": obj.get("origQty"),
                "executedQty": obj.get("executedQty"),
                "origQuoteOrderQty": obj.get("origQuoteOrderQty"),
                "cummulativeQuoteQty": obj.get("cummulativeQuoteQty"),
                "status": obj.get("status"),
                "timeInForce": obj.get("timeInForce"),
                "type": obj.get("type"),
                "side": obj.get("side"),
                "stopPrice": obj.get("stopPrice"),
                "trailingDelta": obj.get("trailingDelta"),
                "icebergQty": obj.get("icebergQty"),
                "strategyId": obj.get("strategyId"),
                "strategyType": obj.get("strategyType"),
                "selfTradePreventionMode": obj.get("selfTradePreventionMode"),
                "contingencyType": obj.get("contingencyType"),
                "listStatusType": obj.get("listStatusType"),
                "listOrderStatus": obj.get("listOrderStatus"),
                "listClientOrderId": obj.get("listClientOrderId"),
                "transactionTime": obj.get("transactionTime"),
                "orders": (
                    [
                        OpenOrdersCancelAllResponseResultInnerOrdersInner.from_dict(
                            _item
                        )
                        for _item in obj["orders"]
                    ]
                    if obj.get("orders") is not None
                    else None
                ),
                "orderReports": (
                    [
                        OpenOrdersCancelAllResponseResultInnerOrderReportsInner.from_dict(
                            _item
                        )
                        for _item in obj["orderReports"]
                    ]
                    if obj.get("orderReports") is not None
                    else None
                ),
            }
        )
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
