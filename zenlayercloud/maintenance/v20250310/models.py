#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeMaintenanceAlertsRequest(AbstractModel):
    def __init__(self):
        self.product = None

    def _deserialize(self, params):
        self.product = params.get("product")


class DescribeMaintenanceAlertsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.dataList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = MaintenanceAlertInfo(item)
                self.dataList.append(obj)



class MaintenanceAlertInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.location = None
        self.impact = None
        self.startTime = None
        self.endTime = None
        self.status = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.location = params.get("location")
        self.impact = params.get("impact")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.status = params.get("status")



