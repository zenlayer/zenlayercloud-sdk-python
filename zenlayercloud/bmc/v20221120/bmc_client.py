#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.bmc.v20221120 import models
from zenlayercloud.common.abstract_client import AbstractClient


class BmcClient(AbstractClient):
    _api_version = "2022-11-20"
    _service = "bmc"

    def CreateInstances(self, request):
        """ 本接口 (CreateInstances) 用于创建一个或多个指定配置的BMC实例。

        :param request: Request instance for CreateInstances.
        :return:
        """

        response = self._api_call("CreateInstances", request)
        model = models.CreateInstancesResponse()
        model._deserialize(response)
        return model
