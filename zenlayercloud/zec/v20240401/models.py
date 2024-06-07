#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeInstanceMonitorDataRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.metricType = None
        self.ipAddress = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.metricType = params.get("metricType")
        self.ipAddress = params.get("ipAddress")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeInstanceMonitorDataResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.maxValue = None
        self.avgValue = None
        self.dataList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.maxValue = params.get("maxValue")
        self.avgValue = params.get("avgValue")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = MetricValue(item)
                self.dataList.append(obj)


class MetricValue(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.value = None
        self.timeInSecond = None

    def _deserialize(self, params):
        self.value = params.get("value")
        self.timeInSecond = params.get("timeInSecond")
