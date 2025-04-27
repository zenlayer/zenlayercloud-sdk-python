#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeIpBlockEventsRequest(AbstractModel):
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.ip = None

    def _deserialize(self, params):
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.ip = params.get("ip")


class DescribeIpBlockEventsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.dataList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = IpBlockEventInfo(item)
                self.dataList.append(obj)


class IpBlockEventInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.ip = None
        self.internalIps = None
        self.region = None
        self.resourceGroup = None
        self.blockTime = None
        self.unblockTime = None
        self.divertMode = None

    def _deserialize(self, params):
        self.ip = params.get("ip")
        self.internalIps = params.get("internalIps")
        self.region = params.get("region")
        self.resourceGroup = params.get("resourceGroup")
        self.blockTime = params.get("blockTime")
        self.unblockTime = params.get("unblockTime")
        self.divertMode = params.get("divertMode")



