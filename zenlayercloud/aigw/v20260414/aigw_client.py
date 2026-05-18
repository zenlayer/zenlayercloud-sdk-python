#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.aigw.v20260414 import models
from zenlayercloud.common.abstract_client import AbstractClient


class AigwClient(AbstractClient):
    _api_version = "2026-04-14"
    _service = "aigw"

    def DescribeAiGateways(self, request):
        """
        分页查询ai网关列表
        """
        response = self._api_call("DescribeAiGateways", request)
        model = models.DescribeAiGatewaysResponse()
        model._deserialize(response)
        return model

    def CreateAiGateway(self, request):
        """
        创建AI网关
        """
        response = self._api_call("CreateAiGateway", request)
        model = models.CreateAiGatewayResponse()
        model._deserialize(response)
        return model

    def StartAiGateway(self, request):
        """
        启动AI网关
        """
        response = self._api_call("StartAiGateway", request)
        model = models.StartAiGatewayResponse()
        model._deserialize(response)
        return model

    def StopAiGateway(self, request):
        """
        停止AI网关
        """
        response = self._api_call("StopAiGateway", request)
        model = models.StopAiGatewayResponse()
        model._deserialize(response)
        return model

    def DeleteAiGateway(self, request):
        """
        删除AI网关
        """
        response = self._api_call("DeleteAiGateway", request)
        model = models.DeleteAiGatewayResponse()
        model._deserialize(response)
        return model

    def DescribeAiGatewayModels(self, request):
        """
        查询AI网关模型
        """
        response = self._api_call("DescribeAiGatewayModels", request)
        model = models.DescribeAiGatewayModelsResponse()
        model._deserialize(response)
        return model

    def ModifyAiGatewayModels(self, request):
        """
        修改AI网关模型
        """
        response = self._api_call("ModifyAiGatewayModels", request)
        model = models.ModifyAiGatewayModelsResponse()
        model._deserialize(response)
        return model

    def DescribeAiGatewayIpAcl(self, request):
        """
        查询AI网关IP访问控制
        """
        response = self._api_call("DescribeAiGatewayIpAcl", request)
        model = models.DescribeAiGatewayIpAclResponse()
        model._deserialize(response)
        return model

    def ModifyAiGatewayIpAcl(self, request):
        """
        修改AI网关IP访问控制
        """
        response = self._api_call("ModifyAiGatewayIpAcl", request)
        model = models.ModifyAiGatewayIpAclResponse()
        model._deserialize(response)
        return model

    def DescribeAiGatewayExpireTime(self, request):
        """
        查询AI网关过期时间
        """
        response = self._api_call("DescribeAiGatewayExpireTime", request)
        model = models.DescribeAiGatewayExpireTimeResponse()
        model._deserialize(response)
        return model

    def ModifyAiGatewayExpireTime(self, request):
        """
        修改AI网关过期时间
        """
        response = self._api_call("ModifyAiGatewayExpireTime", request)
        model = models.ModifyAiGatewayExpireTimeResponse()
        model._deserialize(response)
        return model

    def DescribeAiGatewayTokenLimit(self, request):
        """
        查询AI网关Token限制
        """
        response = self._api_call("DescribeAiGatewayTokenLimit", request)
        model = models.DescribeAiGatewayTokenLimitResponse()
        model._deserialize(response)
        return model

    def ModifyAiGatewayTokenLimit(self, request):
        """
        修改AI网关Token限制
        """
        response = self._api_call("ModifyAiGatewayTokenLimit", request)
        model = models.ModifyAiGatewayTokenLimitResponse()
        model._deserialize(response)
        return model

    def ModifyAiGatewayName(self, request):
        """
        修改AI网关名称
        """
        response = self._api_call("ModifyAiGatewayName", request)
        model = models.ModifyAiGatewayNameResponse()
        model._deserialize(response)
        return model

    def DescribeAiModels(self, request):
        """
        查询ai模型列表
        """
        response = self._api_call("DescribeAiModels", request)
        model = models.DescribeAiModelsResponse()
        model._deserialize(response)
        return model

    def DescribeAiUsageDetailData(self, request):
        """
        查询AI网关用量明细数据
        """
        response = self._api_call("DescribeAiUsageDetailData", request)
        model = models.DescribeAiUsageDetailDataResponse()
        model._deserialize(response)
        return model

    def DescribeAiMonthlyTotalCost(self, request):
        """
        查询AI网关月总费用
        """
        response = self._api_call("DescribeAiMonthlyTotalCost", request)
        model = models.DescribeAiMonthlyTotalCostResponse()
        model._deserialize(response)
        return model

    def DescribeAiModelDailyCost(self, request):
        """
        查询AI网关月模型日费用
        """
        response = self._api_call("DescribeAiModelDailyCost", request)
        model = models.DescribeAiModelDailyCostResponse()
        model._deserialize(response)
        return model

    def DescribeAiUsageData(self, request):
        """
        查询AI网关用量统计数据
        """
        response = self._api_call("DescribeAiUsageData", request)
        model = models.DescribeAiUsageDataResponse()
        model._deserialize(response)
        return model

    def DescribeAiModelDailyCacheHitRate(self, request):
        """
        查询AI网关日模型缓存命中率
        """
        response = self._api_call("DescribeAiModelDailyCacheHitRate", request)
        model = models.DescribeAiModelDailyCacheHitRateResponse()
        model._deserialize(response)
        return model

