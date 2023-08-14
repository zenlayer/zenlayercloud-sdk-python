#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeLogsRequest(AbstractModel):
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.resUid = None
        self.resEvent = None
        self.clientIP = None
        self.size = None
        self.cursor = None

    def _deserialize(self, params):
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.resUid = params.get("resUid")
        self.resEvent = params.get("resEvent")
        self.clientIP = params.get("clientIP")
        self.size = params.get("size")
        if params.get("cursor") is not None:
            self.cursor = []
            for item in params.get("cursor"):
                obj = item
                self.cursor.append(obj)


class DescribeLogsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.cursor = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cursor") is not None:
            self.cursor = []
            for item in params.get("cursor"):
                obj = item
                self.cursor.append(obj)
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = LogInfo(item)
                self.dataSet.append(obj)


class LogInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resUid = None
        self.resType = None
        self.resEvent = None
        self.opsTime = None
        self.eventSource = None
        self.apiVersion = None
        self.opsUser = None
        self.clientIP = None
        self.request = None
        self.response = None

    def _deserialize(self, params):
        self.resUid = params.get("resUid")
        self.resType = params.get("resType")
        self.resEvent = params.get("resEvent")
        self.opsTime = params.get("opsTime")
        self.eventSource = params.get("eventSource")
        self.apiVersion = params.get("apiVersion")
        self.opsUser = params.get("opsUser")
        self.clientIP = params.get("clientIP")
        self.request = params.get("request")
        self.response = params.get("response")



