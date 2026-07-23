#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.ipt.v20240901 import models
from zenlayercloud.common.abstract_client import AbstractClient


class IptClient(AbstractClient):
    _api_version = "2024-09-01"
    _service = "ipt"

    def DescribeIPTransitDatacenters(self, request):
        """
        查询IP Transit可连接数据中心
        """
        response = self._api_call("DescribeIPTransitDatacenters", request)
        model = models.DescribeIPTransitDatacentersResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransitAvailableAsns(self, request):
        """
        查询IP Transit可用 ASN
        """
        response = self._api_call("DescribeIPTransitAvailableAsns", request)
        model = models.DescribeIPTransitAvailableAsnsResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransitAvailableCidrBlocks(self, request):
        """
        查询IP Transit可用公网地址段
        """
        response = self._api_call("DescribeIPTransitAvailableCidrBlocks", request)
        model = models.DescribeIPTransitAvailableCidrBlocksResponse()
        model._deserialize(response)
        return model

    def InquiryCreateIPTransitPrice(self, request):
        """
        iP Transit创建询价
        """
        response = self._api_call("InquiryCreateIPTransitPrice", request)
        model = models.InquiryCreateIPTransitPriceResponse()
        model._deserialize(response)
        return model

    def CreateIPTransit(self, request):
        """
        创建IP Transit
        """
        response = self._api_call("CreateIPTransit", request)
        model = models.CreateIPTransitResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransits(self, request):
        """
        查询IP Transit列表
        """
        response = self._api_call("DescribeIPTransits", request)
        model = models.DescribeIPTransitsResponse()
        model._deserialize(response)
        return model

    def ModifyIPTransitBandwidth(self, request):
        """
        修改IP Transit带宽
        """
        response = self._api_call("ModifyIPTransitBandwidth", request)
        model = models.ModifyIPTransitBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyIPTransitsAttribute(self, request):
        """
        修改IP Transit属性
        """
        response = self._api_call("ModifyIPTransitsAttribute", request)
        model = models.ModifyIPTransitsAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteIPTransit(self, request):
        """
        删除IP Transit
        """
        response = self._api_call("DeleteIPTransit", request)
        model = models.DeleteIPTransitResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransitTraffic(self, request):
        """
        查询IP Transit流量
        """
        response = self._api_call("DescribeIPTransitTraffic", request)
        model = models.DescribeIPTransitTrafficResponse()
        model._deserialize(response)
        return model

    def InquiryModifyIPTransitPrice(self, request):
        """
        IP Transit变配询价
        """
        response = self._api_call("InquiryModifyIPTransitPrice", request)
        model = models.InquiryModifyIPTransitPriceResponse()
        model._deserialize(response)
        return model

    def ModifyIPTransitConfig(self, request):
        """
        修改IP Transit配置
        """
        response = self._api_call("ModifyIPTransitConfig", request)
        model = models.ModifyIPTransitConfigResponse()
        model._deserialize(response)
        return model

