#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel
import warnings

class DescribeMcpMonthlyBillingRequest(AbstractModel):
    def __init__(self):
        self.month = None

    def _deserialize(self, params):
        self.month = params.get("month")


class DescribeMcpMonthlyBillingResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.items = None
        self.totalUsage = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("items") is not None:
            self.items = []
            for item in params.get("items"):
                obj = BillingItem(item)
                self.items.append(obj)
        self.totalUsage = params.get("totalUsage")


class BillingItem(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.gatewayUuid = None
        self.gatewayName = None
        self.date = None
        self.unit = None
        self.usage = None
        self.modelName = None
        self.unitPrice = None
        self.originalPrice = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")
        self.gatewayName = params.get("gatewayName")
        self.date = params.get("date")
        self.unit = params.get("unit")
        self.usage = params.get("usage")
        self.modelName = params.get("modelName")
        self.unitPrice = params.get("unitPrice")
        self.originalPrice = params.get("originalPrice")


