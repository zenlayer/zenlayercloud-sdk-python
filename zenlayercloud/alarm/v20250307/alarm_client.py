#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.alarm.v20250307 import models
from zenlayercloud.common.abstract_client import AbstractClient


class AlarmClient(AbstractClient):
    _api_version = "2025-03-07"
    _service = "alarm"

    def DescribeIpBlockEvents(self, request):
        response = self._api_call("DescribeIpBlockEvents", request)

        model = models.DescribeIpBlockEventsResponse()
        model._deserialize(response)
        return model

