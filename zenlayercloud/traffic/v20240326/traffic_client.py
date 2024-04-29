#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.traffic.v20240326 import models
from zenlayercloud.common.abstract_client import AbstractClient


class TrafficClient(AbstractClient):
    _api_version = "2024-03-26"
    _service = "traffic"

    def DescribeBandwidthClusters(self, request):
        response = self._api_call("DescribeBandwidthClusters", request)

        model = models.DescribeBandwidthClustersResponse()
        model._deserialize(response)
        return model

    def DescribeBandwidthClusterTraffic(self, request):
        response = self._api_call("DescribeBandwidthClusterTraffic", request)

        model = models.DescribeBandwidthClusterTrafficResponse()
        model._deserialize(response)
        return model