#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.traffic.v20240326 import models
from zenlayercloud.common.abstract_client import AbstractClient


class TrafficClient(AbstractClient):
    _api_version = "2024-03-26"
    _service = "traffic"

    def DescribeBandwidthClusterAreas(self, request):
        """
        查询共享带宽包的地区信息。
        """
        response = self._api_call("DescribeBandwidthClusterAreas", request)
        model = models.DescribeBandwidthClusterAreasResponse()
        model._deserialize(response)
        return model

    def InquiryBandwidthClusterPrice(self, request):
        """
        查询共享带宽包价格。
        """
        response = self._api_call("InquiryBandwidthClusterPrice", request)
        model = models.InquiryBandwidthClusterPriceResponse()
        model._deserialize(response)
        return model

    def DescribeBandwidthClusters(self, request):
        """
        查询一个或多个共享带宽包的信息。用户可以根据共享带宽包ID、名称或者城市名称等条件来查询共享带宽包的详细信息。
        """
        response = self._api_call("DescribeBandwidthClusters", request)
        model = models.DescribeBandwidthClustersResponse()
        model._deserialize(response)
        return model

    def CreateBandwidthCluster(self, request):
        """
        创建一个共享带宽包。
        """
        response = self._api_call("CreateBandwidthCluster", request)
        model = models.CreateBandwidthClusterResponse()
        model._deserialize(response)
        return model

    def DescribeBandwidthClusterTraffic(self, request):
        """
        查询带宽组指定时间段内的流量信息。
        """
        response = self._api_call("DescribeBandwidthClusterTraffic", request)
        model = models.DescribeBandwidthClusterTrafficResponse()
        model._deserialize(response)
        return model

    def UpdateBandwidthClusterCommitBandwidth(self, request):
        """
        修改带宽包的保底带宽。
        """
        response = self._api_call("UpdateBandwidthClusterCommitBandwidth", request)
        model = models.UpdateBandwidthClusterCommitBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyBandwidthClusterAttribute(self, request):
        """
        修改共享带宽包的属性。目前只支持名称的修改。
        """
        response = self._api_call("ModifyBandwidthClusterAttribute", request)
        model = models.ModifyBandwidthClusterAttributeResponse()
        model._deserialize(response)
        return model

    def MigrateBandwidthClusterResources(self, request):
        """
        共享带宽包之间的资源迁移。
        """
        response = self._api_call("MigrateBandwidthClusterResources", request)
        model = models.MigrateBandwidthClusterResourcesResponse()
        model._deserialize(response)
        return model

    def DeleteBandwidthClusters(self, request):
        """
        删除一个或多个共享带宽包。
        """
        response = self._api_call("DeleteBandwidthClusters", request)
        model = models.DeleteBandwidthClustersResponse()
        model._deserialize(response)
        return model

    def DescribeBandwidthClusterResources(self, request):
        """
        查询一个共享带宽包里的资源。
        """
        response = self._api_call("DescribeBandwidthClusterResources", request)
        model = models.DescribeBandwidthClusterResourcesResponse()
        model._deserialize(response)
        return model

    def DescribeBandwidthClusterUsage(self, request):
        """
        查询共享带宽包的用量信息。
        """
        response = self._api_call("DescribeBandwidthClusterUsage", request)
        model = models.DescribeBandwidthClusterUsageResponse()
        model._deserialize(response)
        return model

