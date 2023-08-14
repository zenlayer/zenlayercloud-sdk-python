#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.zls.v20230804 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZlsClient(AbstractClient):
    _api_version = "2023-08-04"
    _service = "zls"

    def DescribeLogs(self, request):
        response = self._api_call("DescribeLogs", request)

        model = models.DescribeLogsResponse()
        model._deserialize(response)
        return model

