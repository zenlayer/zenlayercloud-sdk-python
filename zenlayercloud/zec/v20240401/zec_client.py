#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_client import AbstractClient
from zenlayercloud.zec.v20240401 import models


class ZecClient(AbstractClient):
    _api_version = "2024-04-01"
    _service = "zec"

    def DescribeInstanceMonitorData(self, request):
        response = self._api_call("DescribeInstanceMonitorData", request)

        model = models.DescribeInstanceMonitorDataResponse()
        model._deserialize(response)
        return model

