#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.ipt.v20240901 import models
from zenlayercloud.common.abstract_client import AbstractClient


class IptClient(AbstractClient):
    _api_version = "2024-09-01"
    _service = "ipt"

    def DescribeIPTransitDatacenters(self, request):
        """
        本接口用于连接IP Transit 服务支持的数据中心。
        """
        response = self._api_call("DescribeIPTransitDatacenters", request)
        model = models.DescribeIPTransitDatacentersResponse()
        model._deserialize(response)
        return model

    def InquiryCreateIPTransitPrice(self, request):
        """
        创建一条IP Transit 的询价。
        """
        response = self._api_call("InquiryCreateIPTransitPrice", request)
        model = models.InquiryCreateIPTransitPriceResponse()
        model._deserialize(response)
        return model

    def CreateIPTransit(self, request):
        """
        创建一条IP Transit。
        """
        response = self._api_call("CreateIPTransit", request)
        model = models.CreateIPTransitResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransits(self, request):
        """
        本接口用于查询IP Transit资源列表。
        """
        response = self._api_call("DescribeIPTransits", request)
        model = models.DescribeIPTransitsResponse()
        model._deserialize(response)
        return model

    def ModifyIPTransitBandwidth(self, request):
        """
        修改一条IP Transit的带宽限速。
        """
        response = self._api_call("ModifyIPTransitBandwidth", request)
        model = models.ModifyIPTransitBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyIPTransitsAttribute(self, request):
        """
        修改IP Transit的基本信息，包括名称和备注。
        """
        response = self._api_call("ModifyIPTransitsAttribute", request)
        model = models.ModifyIPTransitsAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteIPTransit(self, request):
        """
        删除一条IP Transit。
        """
        response = self._api_call("DeleteIPTransit", request)
        model = models.DeleteIPTransitResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransitTraffic(self, request):
        """
        查询IP Transit在指定时间段内的带宽数据。
        """
        response = self._api_call("DescribeIPTransitTraffic", request)
        model = models.DescribeIPTransitTrafficResponse()
        model._deserialize(response)
        return model

