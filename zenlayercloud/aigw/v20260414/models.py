#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel
import warnings

class DescribeAiGatewaysRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuids = None
        self.gatewayName = None
        self.status = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.gatewayUuids = params.get("gatewayUuids")
        self.gatewayName = params.get("gatewayName")
        self.status = params.get("status")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class Tag(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.key = None
        self.value = None

    def _deserialize(self, params):
        self.key = params.get("key")
        self.value = params.get("value")


class DescribeAiGatewaysResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.totalCount = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalCount = params.get("totalCount")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = AiGatewayInfo(item)
                self.dataSet.append(obj)


class AiGatewayInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.gatewayUuid = None
        self.gatewayName = None
        self.enabled = None
        self.createdAt = None
        self.updatedAt = None
        self.resourceGroupId = None
        self.accessLimit = None
        self.expireType = None
        self.expireTime = None
        self.modelAccess = None
        self.tags = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")
        self.gatewayName = params.get("gatewayName")
        self.enabled = params.get("enabled")
        self.createdAt = params.get("createdAt")
        self.updatedAt = params.get("updatedAt")
        self.resourceGroupId = params.get("resourceGroupId")
        self.accessLimit = params.get("accessLimit")
        self.expireType = params.get("expireType")
        self.expireTime = params.get("expireTime")
        self.modelAccess = params.get("modelAccess")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class Tags(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.tags = None

    def _deserialize(self, params):
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class CreateAiGatewayRequest(AbstractModel):
    def __init__(self):
        self.modelUuids = None
        self.gatewayName = None
        self.tokenLimit = None
        self.expireType = None
        self.expireTime = None
        self.resourceGroupId = None
        self.modelAccess = None
        self.tags = None

    def _deserialize(self, params):
        self.modelUuids = params.get("modelUuids")
        self.gatewayName = params.get("gatewayName")
        self.tokenLimit = params.get("tokenLimit")
        self.expireType = params.get("expireType")
        self.expireTime = params.get("expireTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.modelAccess = params.get("modelAccess")
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class TagAssociation(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.tags = None

    def _deserialize(self, params):
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class CreateAiGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.gatewayUuid = None
        self.token = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.gatewayUuid = params.get("gatewayUuid")
        self.token = params.get("token")


class StartAiGatewayRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")


class StartAiGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class StopAiGatewayRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")


class StopAiGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteAiGatewayRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")


class DeleteAiGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAiGatewayModelsRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")


class DescribeAiGatewayModelsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.models = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("models") is not None:
            self.models = []
            for item in params.get("models"):
                obj = AiGatewayModel(item)
                self.models.append(obj)


class AiGatewayModel(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.modelUuid = None
        self.modelName = None

    def _deserialize(self, params):
        self.modelUuid = params.get("modelUuid")
        self.modelName = params.get("modelName")


class ModifyAiGatewayModelsRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None
        self.modelAccess = None
        self.modelUuids = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")
        self.modelAccess = params.get("modelAccess")
        self.modelUuids = params.get("modelUuids")


class ModifyAiGatewayModelsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAiGatewayIpAclRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")


class DescribeAiGatewayIpAclResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.ipAclType = None
        self.ipAddresses = None
        self.enabled = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.ipAclType = params.get("ipAclType")
        self.ipAddresses = params.get("ipAddresses")
        self.enabled = params.get("enabled")


class ModifyAiGatewayIpAclRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None
        self.ipAclType = None
        self.ipAddresses = None
        self.enabled = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")
        self.ipAclType = params.get("ipAclType")
        self.ipAddresses = params.get("ipAddresses")
        self.enabled = params.get("enabled")


class ModifyAiGatewayIpAclResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAiGatewayExpireTimeRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")


class DescribeAiGatewayExpireTimeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.expireType = None
        self.expireTime = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.expireType = params.get("expireType")
        self.expireTime = params.get("expireTime")


class ModifyAiGatewayExpireTimeRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None
        self.expireType = None
        self.expireTime = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")
        self.expireType = params.get("expireType")
        self.expireTime = params.get("expireTime")


class ModifyAiGatewayExpireTimeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAiGatewayTokenLimitRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")


class DescribeAiGatewayTokenLimitResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.tokenLimit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.tokenLimit = params.get("tokenLimit")


class ModifyAiGatewayTokenLimitRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None
        self.tokenLimit = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")
        self.tokenLimit = params.get("tokenLimit")


class ModifyAiGatewayTokenLimitResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyAiGatewayNameRequest(AbstractModel):
    def __init__(self):
        self.gatewayUuid = None
        self.gatewayName = None

    def _deserialize(self, params):
        self.gatewayUuid = params.get("gatewayUuid")
        self.gatewayName = params.get("gatewayName")


class ModifyAiGatewayNameResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAiModelsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeAiModelsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.modelSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("modelSet") is not None:
            self.modelSet = []
            for item in params.get("modelSet"):
                obj = AiModel(item)
                self.modelSet.append(obj)


class AiModel(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.modelUuid = None
        self.modelName = None
        self.modelType = None
        self.providerName = None

    def _deserialize(self, params):
        self.modelUuid = params.get("modelUuid")
        self.modelName = params.get("modelName")
        self.modelType = params.get("modelType")
        self.providerName = params.get("providerName")


class DescribeAiUsageDetailDataRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.resourceGroupId = None
        self.start = None
        self.end = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.resourceGroupId = params.get("resourceGroupId")
        self.start = params.get("start")
        self.end = params.get("end")


class DescribeAiUsageDetailDataResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.request = None
        self.token = None
        self.inputToken = None
        self.outToken = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("request") is not None:
            self.request = []
            for item in params.get("request"):
                obj = UsageDataPoint(item)
                self.request.append(obj)
        if params.get("token") is not None:
            self.token = []
            for item in params.get("token"):
                obj = UsageDataPoint(item)
                self.token.append(obj)
        if params.get("inputToken") is not None:
            self.inputToken = []
            for item in params.get("inputToken"):
                obj = UsageDataPoint(item)
                self.inputToken.append(obj)
        if params.get("outToken") is not None:
            self.outToken = []
            for item in params.get("outToken"):
                obj = UsageDataPoint(item)
                self.outToken.append(obj)


class UsageDataPoint(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.time = None
        self.data = None

    def _deserialize(self, params):
        self.time = params.get("time")
        if params.get("data") is not None:
            self.data = []
            for item in params.get("data"):
                obj = ModelValueItem(item)
                self.data.append(obj)


class ModelValueItem(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.model = None
        self.value = None

    def _deserialize(self, params):
        self.model = params.get("model")
        self.value = params.get("value")


class DescribeAiMonthlyTotalCostRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.resourceGroupId = None
        self.month = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.resourceGroupId = params.get("resourceGroupId")
        self.month = params.get("month")


class DescribeAiMonthlyTotalCostResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.totalCost = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalCost = params.get("totalCost")


class DescribeAiModelDailyCostRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.resourceGroupId = None
        self.month = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.resourceGroupId = params.get("resourceGroupId")
        self.month = params.get("month")


class DescribeAiModelDailyCostResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dates = None
        self.series = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.dates = params.get("dates")
        if params.get("series") is not None:
            self.series = []
            for item in params.get("series"):
                obj = ModelCostSeries(item)
                self.series.append(obj)


class ModelCostSeries(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.modelName = None
        self.data = None

    def _deserialize(self, params):
        self.modelName = params.get("modelName")
        self.data = params.get("data")


class DescribeAiUsageDataRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.resourceGroupId = None
        self.start = None
        self.end = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.resourceGroupId = params.get("resourceGroupId")
        self.start = params.get("start")
        self.end = params.get("end")


class DescribeAiUsageDataResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.totalInputTokens = None
        self.totalOutputTokens = None
        self.instanceModelToken = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalInputTokens = params.get("totalInputTokens")
        self.totalOutputTokens = params.get("totalOutputTokens")
        if params.get("instanceModelToken") is not None:
            self.instanceModelToken = []
            for item in params.get("instanceModelToken"):
                obj = UsageData(item)
                self.instanceModelToken.append(obj)


class UsageData(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.modelUuid = None
        self.modelName = None
        self.totalTokens = None
        self.totalRequests = None

    def _deserialize(self, params):
        self.modelUuid = params.get("modelUuid")
        self.modelName = params.get("modelName")
        self.totalTokens = params.get("totalTokens")
        self.totalRequests = params.get("totalRequests")


class DescribeAiModelDailyCacheHitRateRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.resourceGroupId = None
        self.month = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.resourceGroupId = params.get("resourceGroupId")
        self.month = params.get("month")


class DescribeAiModelDailyCacheHitRateResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dates = None
        self.cacheHit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.dates = params.get("dates")
        if params.get("cacheHit") is not None:
            self.cacheHit = []
            for item in params.get("cacheHit"):
                obj = ModelCacheHitSeries(item)
                self.cacheHit.append(obj)


class ModelCacheHitSeries(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.modelName = None
        self.data = None

    def _deserialize(self, params):
        self.modelName = params.get("modelName")
        self.data = params.get("data")


