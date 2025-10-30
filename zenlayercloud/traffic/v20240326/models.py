#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeBandwidthClustersRequest(AbstractModel):
    def __init__(self):
        self.bandwidthClusterIds = None
        self.bandwidthClusterName = None
        self.cityName = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.bandwidthClusterIds = params.get("bandwidthClusterIds")
        self.bandwidthClusterName = params.get("bandwidthClusterName")
        self.cityName = params.get("cityName")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


class DescribeBandwidthClustersResponse(AbstractModel):
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
                obj = BandwidthClusterInfo(item)
                self.dataSet.append(obj)


class BandwidthClusterInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.bandwidthClusterId = None
        self.bandwidthClusterName = None
        self.networkType = None
        self.product = None
        self.areaCode = None
        self.internetChargeType = None
        self.commitBandwidthMbps = None
        self.location = None
        self.createTime = None
        self.resourceNumber = None
        self.cities = None

    def _deserialize(self, params):
        self.bandwidthClusterId = params.get("bandwidthClusterId")
        self.bandwidthClusterName = params.get("bandwidthClusterName")
        self.networkType = params.get("networkType")
        self.product = params.get("product")
        self.areaCode = params.get("areaCode")
        self.internetChargeType = params.get("internetChargeType")
        self.commitBandwidthMbps = params.get("commitBandwidthMbps")
        self.location = params.get("location")
        self.createTime = params.get("createTime")
        self.resourceNumber = params.get("resourceNumber")
        if params.get("cities") is not None:
            self.cities = []
            for item in params.get("cities"):
                obj = CityInfo(item)
                self.cities.append(obj)


class CityInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cityName = None
        self.cityCode = None

    def _deserialize(self, params):
        self.cityName = params.get("cityName")
        self.cityCode = params.get("cityCode")


class DescribeBandwidthClusterResourcesRequest(AbstractModel):
    def __init__(self):
        self.bandwidthClusterId = None

    def _deserialize(self, params):
        self.bandwidthClusterId = params.get("bandwidthClusterId")


class DescribeBandwidthClusterResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.resources = None
        self.totalCount = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("resources") is not None:
            self.resources = []
            for item in params.get("resources"):
                obj = BandwidthClusterResource(item)
                self.resources.append(obj)
        self.totalCount = params.get("totalCount")


class BandwidthClusterResource(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceId = None
        self.resourceType = None

    def _deserialize(self, params):
        self.resourceId = params.get("resourceId")
        self.resourceType = params.get("resourceType")


class DescribeBandwidthClusterAreasRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeBandwidthClusterAreasResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.areas = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("areas") is not None:
            self.areas = []
            for item in params.get("areas"):
                obj = BandwidthClusterAreaInfo(item)
                self.areas.append(obj)


class BandwidthClusterAreaInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.areaCode = None
        self.areaName = None
        self.networkTypes = None
        self.products = None

    def _deserialize(self, params):
        self.areaCode = params.get("areaCode")
        self.areaName = params.get("areaName")
        self.networkTypes = params.get("networkTypes")
        self.products = params.get("products")


class DescribeBandwidthClusterTrafficRequest(AbstractModel):
    def __init__(self):
        self.bandwidthClusterId = None
        self.startTime = None
        self.endTime = None
        self.city = None

    def _deserialize(self, params):
        self.bandwidthClusterId = params.get("bandwidthClusterId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.city = params.get("city")


class DescribeBandwidthClusterTrafficResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataList = None
        self.in95 = None
        self.in95Time = None
        self.inAvg = None
        self.inMax = None
        self.inMin = None
        self.inTotal = None
        self.out95 = None
        self.out95Time = None
        self.outAvg = None
        self.outMax = None
        self.outMin = None
        self.outTotal = None
        self.maxBandwidth95ValueMbps = None
        self.totalUnit = None
        self.unit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = BandwidthClusterTrafficData(item)
                self.dataList.append(obj)
        self.in95 = params.get("in95")
        self.in95Time = params.get("in95Time")
        self.inAvg = params.get("inAvg")
        self.inMax = params.get("inMax")
        self.inMin = params.get("inMin")
        self.inTotal = params.get("inTotal")
        self.out95 = params.get("out95")
        self.out95Time = params.get("out95Time")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.outTotal = params.get("outTotal")
        self.maxBandwidth95ValueMbps = params.get("maxBandwidth95ValueMbps")
        self.totalUnit = params.get("totalUnit")
        self.unit = params.get("unit")


class BandwidthClusterTrafficData(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.internetRX = None
        self.internetTX = None
        self.time = None

    def _deserialize(self, params):
        self.internetRX = params.get("internetRX")
        self.internetTX = params.get("internetTX")
        self.time = params.get("time")


class InquiryBandwidthClusterPriceRequest(AbstractModel):
    def __init__(self):
        self.areaCode = None
        self.commitBandwidthMbps = None
        self.networkType = None
        self.internetChargeType = None
        self.product = None

    def _deserialize(self, params):
        self.areaCode = params.get("areaCode")
        self.commitBandwidthMbps = params.get("commitBandwidthMbps")
        self.networkType = params.get("networkType")
        self.internetChargeType = params.get("internetChargeType")
        self.product = params.get("product")


class InquiryBandwidthClusterPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.price = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))


class PriceItem(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.discount = None
        self.discountPrice = None
        self.originalPrice = None
        self.unitPrice = None
        self.discountUnitPrice = None
        self.chargeUnit = None
        self.stepPrices = None
        self.amountUnit = None
        self.excessUnitPrice = None
        self.excessDiscountUnitPrice = None
        self.excessAmountUnit = None

    def _deserialize(self, params):
        self.discount = params.get("discount")
        self.discountPrice = params.get("discountPrice")
        self.originalPrice = params.get("originalPrice")
        self.unitPrice = params.get("unitPrice")
        self.discountUnitPrice = params.get("discountUnitPrice")
        self.chargeUnit = params.get("chargeUnit")
        if params.get("stepPrices") is not None:
            self.stepPrices = []
            for item in params.get("stepPrices"):
                obj = StepPrice(item)
                self.stepPrices.append(obj)
        self.amountUnit = params.get("amountUnit")
        self.excessUnitPrice = params.get("excessUnitPrice")
        self.excessDiscountUnitPrice = params.get("excessDiscountUnitPrice")
        self.excessAmountUnit = params.get("excessAmountUnit")


class StepPrice(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.stepStart = None
        self.stepEnd = None
        self.unitPrice = None
        self.discountUnitPrice = None

    def _deserialize(self, params):
        self.stepStart = params.get("stepStart")
        self.stepEnd = params.get("stepEnd")
        self.unitPrice = params.get("unitPrice")
        self.discountUnitPrice = params.get("discountUnitPrice")


class CreateBandwidthClusterRequest(AbstractModel):
    def __init__(self):
        self.areaCode = None
        self.commitBandwidthMbps = None
        self.networkType = None
        self.internetChargeType = None
        self.name = None
        self.product = None

    def _deserialize(self, params):
        self.areaCode = params.get("areaCode")
        self.commitBandwidthMbps = params.get("commitBandwidthMbps")
        self.networkType = params.get("networkType")
        self.internetChargeType = params.get("internetChargeType")
        self.name = params.get("name")
        self.product = params.get("product")


class CreateBandwidthClusterResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.bandwidthClusterId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.bandwidthClusterId = params.get("bandwidthClusterId")


class ModifyBandwidthClusterAttributeRequest(AbstractModel):
    def __init__(self):
        self.bandwidthClusterId = None
        self.name = None

    def _deserialize(self, params):
        self.bandwidthClusterId = params.get("bandwidthClusterId")
        self.name = params.get("name")


class ModifyBandwidthClusterAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteBandwidthClustersRequest(AbstractModel):
    def __init__(self):
        self.bandwidthClusterIds = None

    def _deserialize(self, params):
        self.bandwidthClusterIds = params.get("bandwidthClusterIds")


class DeleteBandwidthClustersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UpdateBandwidthClusterCommitBandwidthRequest(AbstractModel):
    def __init__(self):
        self.bandwidthClusterId = None
        self.commitBandwidthMbps = None

    def _deserialize(self, params):
        self.bandwidthClusterId = params.get("bandwidthClusterId")
        self.commitBandwidthMbps = params.get("commitBandwidthMbps")


class UpdateBandwidthClusterCommitBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class MigrateBandwidthClusterResourcesRequest(AbstractModel):
    def __init__(self):
        self.targetBandwidthClusterId = None
        self.resourceIdList = None

    def _deserialize(self, params):
        self.targetBandwidthClusterId = params.get("targetBandwidthClusterId")
        self.resourceIdList = params.get("resourceIdList")


class MigrateBandwidthClusterResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


