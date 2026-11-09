#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.ipt.v20240901 import models
from zenlayercloud.common.abstract_client import AbstractClient


class IptClient(AbstractClient):
    _api_version = "2024-09-01"
    _service = "ipt"

    def DescribeIPTransitDatacenters(self, request):
        """
        查询Internet可连接数据中心。本接口已弃用，请改用 **sdn:DescribeInternetDatacenters**。
        """
        response = self._api_call("DescribeIPTransitDatacenters", request)
        model = models.DescribeIPTransitDatacentersResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransitAvailableAsns(self, request):
        """
        查询Internet可用 ASN。本接口已弃用，请改用 **sdn:DescribeInternetAvailableAsns**。
        """
        response = self._api_call("DescribeIPTransitAvailableAsns", request)
        model = models.DescribeIPTransitAvailableAsnsResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransitAvailableCidrBlocks(self, request):
        """
        查询Internet可用公网地址段。本接口已弃用，请改用 **sdn:DescribeInternetAvailableCidrBlocks**。
        """
        response = self._api_call("DescribeIPTransitAvailableCidrBlocks", request)
        model = models.DescribeIPTransitAvailableCidrBlocksResponse()
        model._deserialize(response)
        return model

    def InquiryCreateIPTransitPrice(self, request):
        """
        Internet创建询价。本接口已弃用，请改用 **sdn:InquiryCreateInternetPrice**。
        """
        response = self._api_call("InquiryCreateIPTransitPrice", request)
        model = models.InquiryCreateIPTransitPriceResponse()
        model._deserialize(response)
        return model

    def CreateIPTransit(self, request):
        """
        创建Internet。本接口已弃用，请改用 **sdn:CreateInternet**。
        """
        response = self._api_call("CreateIPTransit", request)
        model = models.CreateIPTransitResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransits(self, request):
        """
        查询Internet列表。本接口已弃用，请改用 **sdn:DescribeInternets**。
        """
        response = self._api_call("DescribeIPTransits", request)
        model = models.DescribeIPTransitsResponse()
        model._deserialize(response)
        return model

    def ModifyIPTransitBandwidth(self, request):
        """
        修改Internet带宽。本接口已弃用，请改用 **sdn:ModifyInternetConfig**（`type=BANDWIDTH`）。
        """
        response = self._api_call("ModifyIPTransitBandwidth", request)
        model = models.ModifyIPTransitBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyIPTransitsAttribute(self, request):
        """
        修改Internet属性。本接口已弃用，请改用 **sdn:ModifyInternetsAttribute**。
        """
        response = self._api_call("ModifyIPTransitsAttribute", request)
        model = models.ModifyIPTransitsAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteIPTransit(self, request):
        """
        删除Internet。本接口已弃用，请改用 **sdn:DeleteInternet**。
        """
        response = self._api_call("DeleteIPTransit", request)
        model = models.DeleteIPTransitResponse()
        model._deserialize(response)
        return model

    def DescribeIPTransitTraffic(self, request):
        """
        查询Internet流量。本接口已弃用，请改用 **sdn:DescribeInternetTraffic**。
        """
        response = self._api_call("DescribeIPTransitTraffic", request)
        model = models.DescribeIPTransitTrafficResponse()
        model._deserialize(response)
        return model

    def InquiryModifyIPTransitPrice(self, request):
        """
        Internet变配询价。本接口已弃用，请改用 **sdn:InquiryModifyInternetPrice**。
        """
        response = self._api_call("InquiryModifyIPTransitPrice", request)
        model = models.InquiryModifyIPTransitPriceResponse()
        model._deserialize(response)
        return model

    def ModifyIPTransitConfig(self, request):
        """
        修改Internet配置。本接口已弃用，请改用 **sdn:ModifyInternetConfig**。
        """
        response = self._api_call("ModifyIPTransitConfig", request)
        model = models.ModifyIPTransitConfigResponse()
        model._deserialize(response)
        return model

