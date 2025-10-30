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

    def DescribeBandwidthClusterResources(self, request):
        response = self._api_call("DescribeBandwidthClusterResources", request)
        model = models.DescribeBandwidthClusterResourcesResponse()
        model._deserialize(response)
        return model

    def DescribeBandwidthClusterAreas(self, request):
        response = self._api_call("DescribeBandwidthClusterAreas", request)
        model = models.DescribeBandwidthClusterAreasResponse()
        model._deserialize(response)
        return model

    def DescribeBandwidthClusterTraffic(self, request):
        response = self._api_call("DescribeBandwidthClusterTraffic", request)
        model = models.DescribeBandwidthClusterTrafficResponse()
        model._deserialize(response)
        return model

    def InquiryBandwidthClusterPrice(self, request):
        response = self._api_call("InquiryBandwidthClusterPrice", request)
        model = models.InquiryBandwidthClusterPriceResponse()
        model._deserialize(response)
        return model

    def CreateBandwidthCluster(self, request):
        response = self._api_call("CreateBandwidthCluster", request)
        model = models.CreateBandwidthClusterResponse()
        model._deserialize(response)
        return model

    def ModifyBandwidthClusterAttribute(self, request):
        response = self._api_call("ModifyBandwidthClusterAttribute", request)
        model = models.ModifyBandwidthClusterAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteBandwidthClusters(self, request):
        response = self._api_call("DeleteBandwidthClusters", request)
        model = models.DeleteBandwidthClustersResponse()
        model._deserialize(response)
        return model

    def UpdateBandwidthClusterCommitBandwidth(self, request):
        response = self._api_call("UpdateBandwidthClusterCommitBandwidth", request)
        model = models.UpdateBandwidthClusterCommitBandwidthResponse()
        model._deserialize(response)
        return model

    def MigrateBandwidthClusterResources(self, request):
        response = self._api_call("MigrateBandwidthClusterResources", request)
        model = models.MigrateBandwidthClusterResourcesResponse()
        model._deserialize(response)
        return model

