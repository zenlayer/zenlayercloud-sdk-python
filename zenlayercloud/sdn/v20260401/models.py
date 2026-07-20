#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel
import warnings

class CreatePortRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.portName = None
        self.portRemarks = None
        self.portType = None
        self.businessEntityName = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.portName = params.get("portName")
        self.portRemarks = params.get("portRemarks")
        self.portType = params.get("portType")
        self.businessEntityName = params.get("businessEntityName")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class MarketingInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.discountCode = None
        self.usePocVoucher = None

    def _deserialize(self, params):
        self.discountCode = params.get("discountCode")
        self.usePocVoucher = params.get("usePocVoucher")


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


class CreatePortResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.portId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.portId = params.get("portId")


class DestroyPortRequest(AbstractModel):
    def __init__(self):
        self.portId = None

    def _deserialize(self, params):
        self.portId = params.get("portId")


class DestroyPortResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class TerminatePortRequest(AbstractModel):
    def __init__(self):
        self.portId = None

    def _deserialize(self, params):
        self.portId = params.get("portId")


class TerminatePortResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewPortRequest(AbstractModel):
    def __init__(self):
        self.portId = None

    def _deserialize(self, params):
        self.portId = params.get("portId")


class RenewPortResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyPortAttributeRequest(AbstractModel):
    def __init__(self):
        self.portId = None
        self.portName = None
        self.portRemarks = None
        self.businessEntityName = None

    def _deserialize(self, params):
        self.portId = params.get("portId")
        self.portName = params.get("portName")
        self.portRemarks = params.get("portRemarks")
        self.businessEntityName = params.get("businessEntityName")


class ModifyPortAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribePortsRequest(AbstractModel):
    def __init__(self):
        self.pageSize = None
        self.pageNum = None
        self.portIds = None
        self.portName = None
        self.dcId = None
        self.cityName = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.portIds = params.get("portIds")
        self.portName = params.get("portName")
        self.dcId = params.get("dcId")
        self.cityName = params.get("cityName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribePortsResponse(AbstractModel):
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
                obj = PortInfo(item)
                self.dataSet.append(obj)


class PortInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.portId = None
        self.portName = None
        self.portRemarks = None
        self.portType = None
        self.dcId = None
        self.dcName = None
        self.cityName = None
        self.areaName = None
        self.businessEntityName = None
        self.connectionStatus = None
        self.portStatus = None
        self.loaStatus = None
        self.loaDownloadUrl = None
        self.createdTime = None
        self.expiredTime = None
        self.period = None
        self.isCreateBusinessAllowed = None
        self.tags = None

    def _deserialize(self, params):
        self.portId = params.get("portId")
        self.portName = params.get("portName")
        self.portRemarks = params.get("portRemarks")
        self.portType = params.get("portType")
        self.dcId = params.get("dcId")
        self.dcName = params.get("dcName")
        self.cityName = params.get("cityName")
        self.areaName = params.get("areaName")
        self.businessEntityName = params.get("businessEntityName")
        self.connectionStatus = params.get("connectionStatus")
        self.portStatus = params.get("portStatus")
        self.loaStatus = params.get("loaStatus")
        self.loaDownloadUrl = params.get("loaDownloadUrl")
        self.createdTime = params.get("createdTime")
        self.expiredTime = params.get("expiredTime")
        self.period = params.get("period")
        self.isCreateBusinessAllowed = params.get("isCreateBusinessAllowed")
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


class DescribeDataCenterPortPriceRequest(AbstractModel):
    def __init__(self):
        self.dcId = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")


class DescribeDataCenterPortPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.portPriceSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("portPriceSet") is not None:
            self.portPriceSet = []
            for item in params.get("portPriceSet"):
                obj = PortPrice(item)
                self.portPriceSet.append(obj)


class PortPrice(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dcId = None
        self.portType = None
        self.portCategory = None
        self.portPrice = None
        self.stock = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.portType = params.get("portType")
        self.portCategory = params.get("portCategory")
        if params.get("portPrice") is not None:
            self.portPrice = PriceItem(params.get("portPrice"))
        self.stock = params.get("stock")


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
        self.category = None

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
        self.category = params.get("category")


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


class DescribePortTrafficRequest(AbstractModel):
    def __init__(self):
        self.portId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.portId = params.get("portId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribePortTrafficResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataList = None
        self.in95 = None
        self.inAvg = None
        self.inMax = None
        self.inMin = None
        self.out95 = None
        self.outAvg = None
        self.outMax = None
        self.outMin = None
        self.unit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = TrafficData(item)
                self.dataList.append(obj)
        self.in95 = params.get("in95")
        self.inAvg = params.get("inAvg")
        self.inMax = params.get("inMax")
        self.inMin = params.get("inMin")
        self.out95 = params.get("out95")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.unit = params.get("unit")


class TrafficData(AbstractModel):
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


class DescribePortUsableVlanRequest(AbstractModel):
    def __init__(self):
        self.portId = None
        self.dcId = None

    def _deserialize(self, params):
        self.portId = params.get("portId")
        self.dcId = params.get("dcId")


class DescribePortUsableVlanResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.inuseVlanList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.inuseVlanList = params.get("inuseVlanList")


class QueryCloudOnrampPriceRequest(AbstractModel):
    def __init__(self):
        self.cloudType = None
        self.dcId = None
        self.bandwidthMbps = None
        self.vlanId = None
        self.cloudRegionId = None

    def _deserialize(self, params):
        self.cloudType = params.get("cloudType")
        self.dcId = params.get("dcId")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.vlanId = params.get("vlanId")
        self.cloudRegionId = params.get("cloudRegionId")


class QueryCloudOnrampPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.price = None
        self.stock = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.stock = params.get("stock")


class QueryDataCenterPortPriceRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.portType = None
        self.buildCrossConnectWithAssisted = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.portType = params.get("portType")
        self.buildCrossConnectWithAssisted = params.get("buildCrossConnectWithAssisted")


class QueryDataCenterPortPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.crossConnectPrice = None
        self.crossConnectOneTimeConstructionPrice = None
        self.dcId = None
        self.price = None
        self.stock = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("crossConnectPrice") is not None:
            self.crossConnectPrice = PriceItem(params.get("crossConnectPrice"))
        if params.get("crossConnectOneTimeConstructionPrice") is not None:
            self.crossConnectOneTimeConstructionPrice = PriceItem(params.get("crossConnectOneTimeConstructionPrice"))
        self.dcId = params.get("dcId")
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.stock = params.get("stock")


class QueryDataCenterPortPricesRequest(AbstractModel):
    def __init__(self):
        self.dcIds = None
        self.portType = None
        self.buildCrossConnectWithAssisted = None

    def _deserialize(self, params):
        self.dcIds = params.get("dcIds")
        self.portType = params.get("portType")
        self.buildCrossConnectWithAssisted = params.get("buildCrossConnectWithAssisted")


class QueryDataCenterPortPricesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.prices = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("prices") is not None:
            self.prices = []
            for item in params.get("prices"):
                obj = DatacenterPortPrice(item)
                self.prices.append(obj)


class DatacenterPortPrice(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.crossConnectPrice = None
        self.crossConnectOneTimeConstructionPrice = None
        self.dcId = None
        self.price = None
        self.stock = None

    def _deserialize(self, params):
        if params.get("crossConnectPrice") is not None:
            self.crossConnectPrice = PriceItem(params.get("crossConnectPrice"))
        if params.get("crossConnectOneTimeConstructionPrice") is not None:
            self.crossConnectOneTimeConstructionPrice = PriceItem(params.get("crossConnectOneTimeConstructionPrice"))
        self.dcId = params.get("dcId")
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.stock = params.get("stock")


class QueryPrivateConnectPriceRequest(AbstractModel):
    def __init__(self):
        self.internetType = None
        self.bandwidthMbps = None
        self.endpointA = None
        self.endpointZ = None

    def _deserialize(self, params):
        self.internetType = params.get("internetType")
        self.bandwidthMbps = params.get("bandwidthMbps")
        if params.get("endpointA") is not None:
            self.endpointA = PrivateConnectEndpointInfo(params.get("endpointA"))
        if params.get("endpointZ") is not None:
            self.endpointZ = PrivateConnectEndpointInfo(params.get("endpointZ"))


class PrivateConnectEndpointInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dcId = None
        self.cloudType = None
        self.bandwidthMbps = None
        self.vlanId = None
        self.cloudRegionId = None
        self.portType = None
        self.buildCrossConnectWithAssisted = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.cloudType = params.get("cloudType")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.vlanId = params.get("vlanId")
        self.cloudRegionId = params.get("cloudRegionId")
        self.portType = params.get("portType")
        self.buildCrossConnectWithAssisted = params.get("buildCrossConnectWithAssisted")


class QueryPrivateConnectPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.endpointAPrice = None
        self.endpointZPrice = None
        self.price = None
        self.stock = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("endpointAPrice") is not None:
            self.endpointAPrice = PrivateConnectEndpointPrice(params.get("endpointAPrice"))
        if params.get("endpointZPrice") is not None:
            self.endpointZPrice = PrivateConnectEndpointPrice(params.get("endpointZPrice"))
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.stock = params.get("stock")


class PrivateConnectEndpointPrice(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.crossConnectPrice = None
        self.crossConnectOneTimeConstructionPrice = None
        self.price = None
        self.stock = None

    def _deserialize(self, params):
        if params.get("crossConnectPrice") is not None:
            self.crossConnectPrice = PriceItem(params.get("crossConnectPrice"))
        if params.get("crossConnectOneTimeConstructionPrice") is not None:
            self.crossConnectOneTimeConstructionPrice = PriceItem(params.get("crossConnectOneTimeConstructionPrice"))
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.stock = params.get("stock")


class QueryPrivateConnectBandwidthPriceRequest(AbstractModel):
    def __init__(self):
        self.sourceDcId = None
        self.destinationDcId = None
        self.internetType = None
        self.bandwidthMbps = None
        self.serviceLevel = None

    def _deserialize(self, params):
        self.sourceDcId = params.get("sourceDcId")
        self.destinationDcId = params.get("destinationDcId")
        self.internetType = params.get("internetType")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.serviceLevel = params.get("serviceLevel")


class QueryPrivateConnectBandwidthPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.price = None
        self.stock = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.stock = params.get("stock")


class QueryCloudRouterBandwidthPriceRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.bandwidthMbps = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.bandwidthMbps = params.get("bandwidthMbps")


class QueryCloudRouterBandwidthPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.price = None
        self.stock = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.stock = params.get("stock")


class DescribeGoogleVlanUsageRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pairingKey = params.get("pairingKey")


class DescribeGoogleVlanUsageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.usedVlans = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.usedVlans = params.get("usedVlans")


class DescribeTencentVlanUsageRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pairingKey = params.get("pairingKey")


class DescribeTencentVlanUsageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.usedVlans = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.usedVlans = params.get("usedVlans")


class DescribeAliCloudVlanUsageRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pairingKey = params.get("pairingKey")


class DescribeAliCloudVlanUsageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.usedVlans = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.usedVlans = params.get("usedVlans")


class DescribeHuaweiCloudVlanUsageRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pairingKey = params.get("pairingKey")


class DescribeHuaweiCloudVlanUsageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.usedVlans = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.usedVlans = params.get("usedVlans")


class DescribeAzureVlanUsageRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pairingKey = params.get("pairingKey")


class DescribeAzureVlanUsageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.usedVlans = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.usedVlans = params.get("usedVlans")


class DescribeOracleVlanUsageRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pairingKey = params.get("pairingKey")


class DescribeOracleVlanUsageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.usedVlans = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.usedVlans = params.get("usedVlans")


class DescribeBytePlusVlanUsageRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pairingKey = params.get("pairingKey")


class DescribeBytePlusVlanUsageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.usedVlans = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.usedVlans = params.get("usedVlans")


class ModifyCloudBandwidthRequest(AbstractModel):
    def __init__(self):
        self.cloudPortId = None
        self.bandwidthMbps = None

    def _deserialize(self, params):
        self.cloudPortId = params.get("cloudPortId")
        self.bandwidthMbps = params.get("bandwidthMbps")


class ModifyCloudBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeCloudAvailableBandwidthTiersRequest(AbstractModel):
    def __init__(self):
        self.cloudType = None
        self.cloudRegionId = None
        self.dcId = None
        self.vlanId = None
        self.cloudPortId = None
        self.cloudAccountId = None
        self.zoneColor = None

    def _deserialize(self, params):
        self.cloudType = params.get("cloudType")
        self.cloudRegionId = params.get("cloudRegionId")
        self.dcId = params.get("dcId")
        self.vlanId = params.get("vlanId")
        self.cloudPortId = params.get("cloudPortId")
        self.cloudAccountId = params.get("cloudAccountId")
        self.zoneColor = params.get("zoneColor")


class DescribeCloudAvailableBandwidthTiersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.availableBandwidthTiers = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.availableBandwidthTiers = params.get("availableBandwidthTiers")


class DescribeAWSRegionsRequest(AbstractModel):
    def __init__(self):
        self.product = None

    def _deserialize(self, params):
        self.product = params.get("product")


class DescribeAWSRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRegions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cloudRegions") is not None:
            self.cloudRegions = []
            for item in params.get("cloudRegions"):
                obj = CloudRegion(item)
                self.cloudRegions.append(obj)


class CloudRegion(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cloudRegionId = None
        self.dataCenter = None
        self.products = None
        self.haTypes = None

    def _deserialize(self, params):
        self.cloudRegionId = params.get("cloudRegionId")
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        self.products = params.get("products")
        if params.get("haTypes") is not None:
            self.haTypes = []
            for item in params.get("haTypes"):
                obj = HaTypeInfo(item)
                self.haTypes.append(obj)


class DatacenterInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dcId = None
        self.dcName = None
        self.dcAddress = None
        self.cityName = None
        self.countryName = None
        self.areaName = None
        self.latitude = None
        self.longitude = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.dcName = params.get("dcName")
        self.dcAddress = params.get("dcAddress")
        self.cityName = params.get("cityName")
        self.countryName = params.get("countryName")
        self.areaName = params.get("areaName")
        self.latitude = params.get("latitude")
        self.longitude = params.get("longitude")


class HaTypeInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.haType = None
        self.isUsed = None

    def _deserialize(self, params):
        self.haType = params.get("haType")
        self.isUsed = params.get("isUsed")


class DescribeTencentRegionsRequest(AbstractModel):
    def __init__(self):
        self.product = None

    def _deserialize(self, params):
        self.product = params.get("product")


class DescribeTencentRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRegions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cloudRegions") is not None:
            self.cloudRegions = []
            for item in params.get("cloudRegions"):
                obj = CloudRegion(item)
                self.cloudRegions.append(obj)


class DescribeGoogleRegionsRequest(AbstractModel):
    def __init__(self):
        self.product = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.product = params.get("product")
        self.pairingKey = params.get("pairingKey")


class DescribeGoogleRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRegions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cloudRegions") is not None:
            self.cloudRegions = []
            for item in params.get("cloudRegions"):
                obj = CloudRegion(item)
                self.cloudRegions.append(obj)


class DescribeAzureRegionsRequest(AbstractModel):
    def __init__(self):
        self.product = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.product = params.get("product")
        self.pairingKey = params.get("pairingKey")


class DescribeAzureRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRegions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cloudRegions") is not None:
            self.cloudRegions = []
            for item in params.get("cloudRegions"):
                obj = CloudRegion(item)
                self.cloudRegions.append(obj)


class DescribeOracleRegionsRequest(AbstractModel):
    def __init__(self):
        self.product = None
        self.ocId = None

    def _deserialize(self, params):
        self.product = params.get("product")
        self.ocId = params.get("ocId")


class DescribeOracleRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRegions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cloudRegions") is not None:
            self.cloudRegions = []
            for item in params.get("cloudRegions"):
                obj = CloudRegion(item)
                self.cloudRegions.append(obj)


class DescribeAliCloudRegionsRequest(AbstractModel):
    def __init__(self):
        self.product = None

    def _deserialize(self, params):
        self.product = params.get("product")


class DescribeAliCloudRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRegions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cloudRegions") is not None:
            self.cloudRegions = []
            for item in params.get("cloudRegions"):
                obj = CloudRegion(item)
                self.cloudRegions.append(obj)


class DescribeHuaweiCloudRegionsRequest(AbstractModel):
    def __init__(self):
        self.product = None

    def _deserialize(self, params):
        self.product = params.get("product")


class DescribeHuaweiCloudRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRegions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cloudRegions") is not None:
            self.cloudRegions = []
            for item in params.get("cloudRegions"):
                obj = CloudRegion(item)
                self.cloudRegions.append(obj)


class DescribeBytePlusRegionsRequest(AbstractModel):
    def __init__(self):
        self.product = None

    def _deserialize(self, params):
        self.product = params.get("product")


class DescribeBytePlusRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRegions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cloudRegions") is not None:
            self.cloudRegions = []
            for item in params.get("cloudRegions"):
                obj = CloudRegion(item)
                self.cloudRegions.append(obj)


class DescribeAWSVlanUsageRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pairingKey = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pairingKey = params.get("pairingKey")


class DescribeAWSVlanUsageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.start = None
        self.end = None
        self.usedVlans = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.start = params.get("start")
        self.end = params.get("end")
        self.usedVlans = params.get("usedVlans")


class CreateCloudRouterRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterName = None
        self.cloudRouterDescription = None
        self.edgePoints = None
        self.resourceGroupId = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.cloudRouterName = params.get("cloudRouterName")
        self.cloudRouterDescription = params.get("cloudRouterDescription")
        if params.get("edgePoints") is not None:
            self.edgePoints = []
            for item in params.get("edgePoints"):
                obj = CreateCloudRouterEdgePoint(item)
                self.edgePoints.append(obj)
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateCloudRouterEdgePoint(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.edgePointName = None
        self.vpcId = None
        self.zbgId = None
        self.portId = None
        self.cloudType = None
        self.cloudAccountId = None
        self.dcId = None
        self.cloudRegionId = None
        self.haType = None
        self.vlanId = None
        self.bandwidthMbps = None
        self.cloudBandwidthMbps = None
        self.ipAddress = None
        self.bgpConnection = None
        self.staticRoutes = None
        self.ipSecTunnel = None
        self.customerPublicIP = None
        self.customerPrivateIP = None
        self.virtualEdgePrivateIP = None
        self.psk = None
        self.enableHealthCheck = None
        self.backupIpSec = None
        self.ipSecBgpConnection = None
        self.ipSecStaticRoutes = None

    def _deserialize(self, params):
        self.edgePointName = params.get("edgePointName")
        self.vpcId = params.get("vpcId")
        self.zbgId = params.get("zbgId")
        self.portId = params.get("portId")
        self.cloudType = params.get("cloudType")
        self.cloudAccountId = params.get("cloudAccountId")
        self.dcId = params.get("dcId")
        self.cloudRegionId = params.get("cloudRegionId")
        self.haType = params.get("haType")
        self.vlanId = params.get("vlanId")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.cloudBandwidthMbps = params.get("cloudBandwidthMbps")
        self.ipAddress = params.get("ipAddress")
        if params.get("bgpConnection") is not None:
            self.bgpConnection = BGPConnection(params.get("bgpConnection"))
        if params.get("staticRoutes") is not None:
            self.staticRoutes = []
            for item in params.get("staticRoutes"):
                obj = IPRoute(item)
                self.staticRoutes.append(obj)
        self.ipSecTunnel = params.get("ipSecTunnel")
        self.customerPublicIP = params.get("customerPublicIP")
        self.customerPrivateIP = params.get("customerPrivateIP")
        self.virtualEdgePrivateIP = params.get("virtualEdgePrivateIP")
        self.psk = params.get("psk")
        self.enableHealthCheck = params.get("enableHealthCheck")
        if params.get("backupIpSec") is not None:
            self.backupIpSec = BackupIPSecConfig(params.get("backupIpSec"))
        if params.get("ipSecBgpConnection") is not None:
            self.ipSecBgpConnection = IPSecBGPConnection(params.get("ipSecBgpConnection"))
        if params.get("ipSecStaticRoutes") is not None:
            self.ipSecStaticRoutes = []
            for item in params.get("ipSecStaticRoutes"):
                obj = IPSecStaticRoute(item)
                self.ipSecStaticRoutes.append(obj)


class BGPConnection(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.peerIpAddress = None
        self.peerAsn = None
        self.password = None
        self.localAsn = None

    def _deserialize(self, params):
        self.peerIpAddress = params.get("peerIpAddress")
        self.peerAsn = params.get("peerAsn")
        self.password = params.get("password")
        self.localAsn = params.get("localAsn")


class IPRoute(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.prefix = None
        self.nextHop = None

    def _deserialize(self, params):
        self.prefix = params.get("prefix")
        self.nextHop = params.get("nextHop")


class BackupIPSecConfig(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dcId = None
        self.password = None
        self.customerPrivateIP = None
        self.virtualEdgePrivateIP = None
        self.psk = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.password = params.get("password")
        self.customerPrivateIP = params.get("customerPrivateIP")
        self.virtualEdgePrivateIP = params.get("virtualEdgePrivateIP")
        self.psk = params.get("psk")


class IPSecBGPConnection(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.customerAsn = None
        self.virtualEdgeAsn = None
        self.password = None

    def _deserialize(self, params):
        self.customerAsn = params.get("customerAsn")
        self.virtualEdgeAsn = params.get("virtualEdgeAsn")
        self.password = params.get("password")


class IPSecStaticRoute(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cidr = None

    def _deserialize(self, params):
        self.cidr = params.get("cidr")


class CreateCloudRouterResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cloudRouterId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.cloudRouterId = params.get("cloudRouterId")


class DeleteCloudRouterEdgePointRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None
        self.edgePointId = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")
        self.edgePointId = params.get("edgePointId")


class DeleteCloudRouterEdgePointResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AddCloudRouterEdgePointsRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None
        self.edgePoints = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")
        if params.get("edgePoints") is not None:
            self.edgePoints = []
            for item in params.get("edgePoints"):
                obj = CreateCloudRouterEdgePoint(item)
                self.edgePoints.append(obj)


class AddCloudRouterEdgePointsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.edgePointIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.edgePointIds = params.get("edgePointIds")


class ModifyCloudRoutersAttributeRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterIds = None
        self.cloudRouterName = None
        self.cloudRouterDescription = None

    def _deserialize(self, params):
        self.cloudRouterIds = params.get("cloudRouterIds")
        self.cloudRouterName = params.get("cloudRouterName")
        self.cloudRouterDescription = params.get("cloudRouterDescription")


class ModifyCloudRoutersAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeCloudRouterAvailableVpcsRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeCloudRouterAvailableVpcsResponse(AbstractModel):
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
                obj = CloudRouterAvailableVpc(item)
                self.dataSet.append(obj)


class CloudRouterAvailableVpc(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.vpcId = None
        self.vpcName = None
        self.dataCenter = None
        self.cidrBlock = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.vpcName = params.get("vpcName")
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        self.cidrBlock = params.get("cidrBlock")


class DescribeCloudRouterEdgePointTrafficRequest(AbstractModel):
    def __init__(self):
        self.edgePointId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.edgePointId = params.get("edgePointId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeCloudRouterEdgePointTrafficResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataList = None
        self.in95 = None
        self.inAvg = None
        self.inMax = None
        self.inMin = None
        self.out95 = None
        self.outAvg = None
        self.outMax = None
        self.outMin = None
        self.unit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = TrafficData(item)
                self.dataList.append(obj)
        self.in95 = params.get("in95")
        self.inAvg = params.get("inAvg")
        self.inMax = params.get("inMax")
        self.inMin = params.get("inMin")
        self.out95 = params.get("out95")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.unit = params.get("unit")


class DescribeCloudRouterDCToDCTrafficRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None
        self.sourceDcId = None
        self.destinationDcId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")
        self.sourceDcId = params.get("sourceDcId")
        self.destinationDcId = params.get("destinationDcId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeCloudRouterDCToDCTrafficResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataList = None
        self.in95 = None
        self.inAvg = None
        self.inMax = None
        self.inMin = None
        self.out95 = None
        self.outAvg = None
        self.outMax = None
        self.outMin = None
        self.unit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = TrafficData(item)
                self.dataList.append(obj)
        self.in95 = params.get("in95")
        self.inAvg = params.get("inAvg")
        self.inMax = params.get("inMax")
        self.inMin = params.get("inMin")
        self.out95 = params.get("out95")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.unit = params.get("unit")


class ModifyCloudRouterEdgePointBandwidthRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None
        self.edgePointId = None
        self.bandwidthMbps = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")
        self.edgePointId = params.get("edgePointId")
        self.bandwidthMbps = params.get("bandwidthMbps")


class ModifyCloudRouterEdgePointBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyCloudRouterEdgePointRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None
        self.edgePointId = None
        self.bandwidthMbps = None
        self.ipAddress = None
        self.bgpConnection = None
        self.staticRoutes = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")
        self.edgePointId = params.get("edgePointId")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.ipAddress = params.get("ipAddress")
        if params.get("bgpConnection") is not None:
            self.bgpConnection = BGPConnection(params.get("bgpConnection"))
        if params.get("staticRoutes") is not None:
            self.staticRoutes = []
            for item in params.get("staticRoutes"):
                obj = IPRoute(item)
                self.staticRoutes.append(obj)


class ModifyCloudRouterEdgePointResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteCloudRouterRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")


class DeleteCloudRouterResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DestroyCloudRouterRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")


class DestroyCloudRouterResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewCloudRouterRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")


class RenewCloudRouterResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeCloudRouterAvailablePortsRequest(AbstractModel):
    def __init__(self):
        self.portIds = None
        self.dcId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.portIds = params.get("portIds")
        self.dcId = params.get("dcId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeCloudRouterAvailablePortsResponse(AbstractModel):
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
                obj = PortInfo(item)
                self.dataSet.append(obj)


class DescribeCloudRoutersRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterIds = None
        self.cloudRouterName = None
        self.cloudRouterStatus = None
        self.edgePointId = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.cloudRouterIds = params.get("cloudRouterIds")
        self.cloudRouterName = params.get("cloudRouterName")
        self.cloudRouterStatus = params.get("cloudRouterStatus")
        self.edgePointId = params.get("edgePointId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeCloudRoutersResponse(AbstractModel):
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
                obj = CloudRouter(item)
                self.dataSet.append(obj)


class CloudRouter(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cloudRouterId = None
        self.cloudRouterName = None
        self.cloudRouterDescription = None
        self.createTime = None
        self.expiredTime = None
        self.recycledTime = None
        self.edgePoints = None
        self.cloudRouterStatus = None
        self.connectivityStatus = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.period = None
        self.source = None
        self.tags = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")
        self.cloudRouterName = params.get("cloudRouterName")
        self.cloudRouterDescription = params.get("cloudRouterDescription")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.recycledTime = params.get("recycledTime")
        if params.get("edgePoints") is not None:
            self.edgePoints = []
            for item in params.get("edgePoints"):
                obj = CloudRouterEdgePoint(item)
                self.edgePoints.append(obj)
        self.cloudRouterStatus = params.get("cloudRouterStatus")
        self.connectivityStatus = params.get("connectivityStatus")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.period = params.get("period")
        self.source = params.get("source")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class CloudRouterEdgePoint(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.edgePointId = None
        self.edgePointName = None
        self.connectivityStatus = None
        self.dataCenter = None
        self.edgePointType = None
        self.cloudType = None
        self.cloudAccountId = None
        self.cloudRegionId = None
        self.vpcId = None
        self.zbgId = None
        self.zbgRegionId = None
        self.portId = None
        self.sharedChannelId = None
        self.vlanId = None
        self.bandwidthMbps = None
        self.bgpConnection = None
        self.staticRoutes = None
        self.createTime = None
        self.ipAddress = None

    def _deserialize(self, params):
        self.edgePointId = params.get("edgePointId")
        self.edgePointName = params.get("edgePointName")
        self.connectivityStatus = params.get("connectivityStatus")
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        self.edgePointType = params.get("edgePointType")
        self.cloudType = params.get("cloudType")
        self.cloudAccountId = params.get("cloudAccountId")
        self.cloudRegionId = params.get("cloudRegionId")
        self.vpcId = params.get("vpcId")
        self.zbgId = params.get("zbgId")
        self.zbgRegionId = params.get("zbgRegionId")
        self.portId = params.get("portId")
        self.sharedChannelId = params.get("sharedChannelId")
        self.vlanId = params.get("vlanId")
        self.bandwidthMbps = params.get("bandwidthMbps")
        if params.get("bgpConnection") is not None:
            self.bgpConnection = BGPConnection(params.get("bgpConnection"))
        if params.get("staticRoutes") is not None:
            self.staticRoutes = []
            for item in params.get("staticRoutes"):
                obj = IPRoute(item)
                self.staticRoutes.append(obj)
        self.createTime = params.get("createTime")
        self.ipAddress = params.get("ipAddress")


class DescribeDatacentersRequest(AbstractModel):
    def __init__(self):
        self.dcIds = None
        self.isPortAvailable = None

    def _deserialize(self, params):
        self.dcIds = params.get("dcIds")
        self.isPortAvailable = params.get("isPortAvailable")


class DescribeDatacentersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dcSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dcSet") is not None:
            self.dcSet = []
            for item in params.get("dcSet"):
                obj = DataCenterAssemble(item)
                self.dcSet.append(obj)


class DataCenterAssemble(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dcId = None
        self.dcName = None
        self.dcAddress = None
        self.cityName = None
        self.countryName = None
        self.areaName = None
        self.latitude = None
        self.longitude = None
        self.isPortAvailable = None
        self.availableBandwidth = None
        self.regionId = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.dcName = params.get("dcName")
        self.dcAddress = params.get("dcAddress")
        self.cityName = params.get("cityName")
        self.countryName = params.get("countryName")
        self.areaName = params.get("areaName")
        self.latitude = params.get("latitude")
        self.longitude = params.get("longitude")
        self.isPortAvailable = params.get("isPortAvailable")
        self.availableBandwidth = params.get("availableBandwidth")
        self.regionId = params.get("regionId")


class DescribeVirtualEdgeDatacentersRequest(AbstractModel):
    def __init__(self):
        self.primaryDcId = None

    def _deserialize(self, params):
        self.primaryDcId = params.get("primaryDcId")


class DescribeVirtualEdgeDatacentersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dcSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dcSet") is not None:
            self.dcSet = []
            for item in params.get("dcSet"):
                obj = DataCenterAssemble(item)
                self.dcSet.append(obj)


class DescribeBorderGatewayDatacentersRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.regionId = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.regionId = params.get("regionId")


class DescribeBorderGatewayDatacentersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dcSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dcSet") is not None:
            self.dcSet = []
            for item in params.get("dcSet"):
                obj = DataCenterAssemble(item)
                self.dcSet.append(obj)


class DescribeVPCDatacentersRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.regionId = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.regionId = params.get("regionId")


class DescribeVPCDatacentersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dcSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dcSet") is not None:
            self.dcSet = []
            for item in params.get("dcSet"):
                obj = DataCenterAssemble(item)
                self.dcSet.append(obj)


class DescribeDatacentersWithServiceRequest(AbstractModel):
    def __init__(self):
        self.cloudRegionId = None
        self.dcId = None
        self.serviceType = None

    def _deserialize(self, params):
        self.cloudRegionId = params.get("cloudRegionId")
        self.dcId = params.get("dcId")
        self.serviceType = params.get("serviceType")


class DescribeDatacentersWithServiceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dcSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dcSet") is not None:
            self.dcSet = []
            for item in params.get("dcSet"):
                obj = DataCenterWithServiceResponse(item)
                self.dcSet.append(obj)


class DataCenterWithServiceResponse(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dcId = None
        self.dcName = None
        self.dcAddress = None
        self.cityName = None
        self.countryName = None
        self.areaName = None
        self.latitude = None
        self.longitude = None
        self.cloudRegionId = None
        self.serviceTypes = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.dcName = params.get("dcName")
        self.dcAddress = params.get("dcAddress")
        self.cityName = params.get("cityName")
        self.countryName = params.get("countryName")
        self.areaName = params.get("areaName")
        self.latitude = params.get("latitude")
        self.longitude = params.get("longitude")
        self.cloudRegionId = params.get("cloudRegionId")
        self.serviceTypes = params.get("serviceTypes")


class DescribePrivateConnectsRequest(AbstractModel):
    def __init__(self):
        self.privateConnectIds = None
        self.privateConnectName = None
        self.connectivityStatus = None
        self.privateConnectStatus = None
        self.endpointTypes = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.privateConnectIds = params.get("privateConnectIds")
        self.privateConnectName = params.get("privateConnectName")
        self.connectivityStatus = params.get("connectivityStatus")
        self.privateConnectStatus = params.get("privateConnectStatus")
        self.endpointTypes = params.get("endpointTypes")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribePrivateConnectsResponse(AbstractModel):
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
                obj = PrivateConnect(item)
                self.dataSet.append(obj)


class PrivateConnect(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.privateConnectId = None
        self.privateConnectName = None
        self.connectivityStatus = None
        self.privateConnectStatus = None
        self.bandwidthMbps = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.createTime = None
        self.expiredTime = None
        self.recycledTime = None
        self.endpointA = None
        self.endpointZ = None
        self.source = None
        self.tags = None

    def _deserialize(self, params):
        self.privateConnectId = params.get("privateConnectId")
        self.privateConnectName = params.get("privateConnectName")
        self.connectivityStatus = params.get("connectivityStatus")
        self.privateConnectStatus = params.get("privateConnectStatus")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.recycledTime = params.get("recycledTime")
        if params.get("endpointA") is not None:
            self.endpointA = PrivateConnectEndpoint(params.get("endpointA"))
        if params.get("endpointZ") is not None:
            self.endpointZ = PrivateConnectEndpoint(params.get("endpointZ"))
        self.source = params.get("source")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class PrivateConnectEndpoint(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.endpointId = None
        self.endpointName = None
        self.endpointType = None
        self.connectivityStatus = None
        self.vlanId = None
        self.dataCenter = None
        self.cloudRegionId = None
        self.cloudAccountId = None
        self.sharedChannelId = None

    def _deserialize(self, params):
        self.endpointId = params.get("endpointId")
        self.endpointName = params.get("endpointName")
        self.endpointType = params.get("endpointType")
        self.connectivityStatus = params.get("connectivityStatus")
        self.vlanId = params.get("vlanId")
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        self.cloudRegionId = params.get("cloudRegionId")
        self.cloudAccountId = params.get("cloudAccountId")
        self.sharedChannelId = params.get("sharedChannelId")


class CreatePrivateConnectRequest(AbstractModel):
    def __init__(self):
        self.privateConnectName = None
        self.bandwidthMbps = None
        self.resourceGroupId = None
        self.endpointA = None
        self.endpointZ = None
        self.tags = None
        self.marketingOptions = None

    def _deserialize(self, params):
        self.privateConnectName = params.get("privateConnectName")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("endpointA") is not None:
            self.endpointA = CreateEndpointParam(params.get("endpointA"))
        if params.get("endpointZ") is not None:
            self.endpointZ = CreateEndpointParam(params.get("endpointZ"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))


class CreateEndpointParam(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.portId = None
        self.vlanId = None
        self.cloudRegionId = None
        self.cloudAccountId = None
        self.haType = None
        self.cloudBandwidthMbps = None
        self.dcId = None
        self.cloudType = None
        self.endpointName = None

    def _deserialize(self, params):
        self.portId = params.get("portId")
        self.vlanId = params.get("vlanId")
        self.cloudRegionId = params.get("cloudRegionId")
        self.cloudAccountId = params.get("cloudAccountId")
        self.haType = params.get("haType")
        self.cloudBandwidthMbps = params.get("cloudBandwidthMbps")
        self.dcId = params.get("dcId")
        self.cloudType = params.get("cloudType")
        self.endpointName = params.get("endpointName")


class CreatePrivateConnectResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.privateConnectId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.privateConnectId = params.get("privateConnectId")


class ModifyPrivateConnectBandwidthRequest(AbstractModel):
    def __init__(self):
        self.privateConnectId = None
        self.bandwidthMbps = None

    def _deserialize(self, params):
        self.privateConnectId = params.get("privateConnectId")
        self.bandwidthMbps = params.get("bandwidthMbps")


class ModifyPrivateConnectBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribePrivateConnectTrafficRequest(AbstractModel):
    def __init__(self):
        self.privateConnectId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.privateConnectId = params.get("privateConnectId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribePrivateConnectTrafficResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataList = None
        self.in95 = None
        self.inAvg = None
        self.inMax = None
        self.inMin = None
        self.out95 = None
        self.outAvg = None
        self.outMax = None
        self.outMin = None
        self.unit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = TrafficData(item)
                self.dataList.append(obj)
        self.in95 = params.get("in95")
        self.inAvg = params.get("inAvg")
        self.inMax = params.get("inMax")
        self.inMin = params.get("inMin")
        self.out95 = params.get("out95")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.unit = params.get("unit")


class DeletePrivateConnectRequest(AbstractModel):
    def __init__(self):
        self.privateConnectId = None

    def _deserialize(self, params):
        self.privateConnectId = params.get("privateConnectId")


class DeletePrivateConnectResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DestroyPrivateConnectRequest(AbstractModel):
    def __init__(self):
        self.privateConnectId = None

    def _deserialize(self, params):
        self.privateConnectId = params.get("privateConnectId")


class DestroyPrivateConnectResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribePrivateConnectAvailablePortsRequest(AbstractModel):
    def __init__(self):
        self.portIds = None
        self.dcId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.portIds = params.get("portIds")
        self.dcId = params.get("dcId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribePrivateConnectAvailablePortsResponse(AbstractModel):
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
                obj = PortInfo(item)
                self.dataSet.append(obj)


class ModifyPrivateConnectsAttributeRequest(AbstractModel):
    def __init__(self):
        self.privateConnectIds = None
        self.privateConnectName = None

    def _deserialize(self, params):
        self.privateConnectIds = params.get("privateConnectIds")
        self.privateConnectName = params.get("privateConnectName")


class ModifyPrivateConnectsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewPrivateConnectRequest(AbstractModel):
    def __init__(self):
        self.privateConnectId = None

    def _deserialize(self, params):
        self.privateConnectId = params.get("privateConnectId")


class RenewPrivateConnectResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class InquiryCreatePrivateConnectPriceRequest(AbstractModel):
    def __init__(self):
        self.bandwidthMbps = None
        self.internetType = None
        self.commitBandwidth = None
        self.endpointA = None
        self.endpointZ = None

    def _deserialize(self, params):
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.internetType = params.get("internetType")
        self.commitBandwidth = params.get("commitBandwidth")
        if params.get("endpointA") is not None:
            self.endpointA = CreateEndpointParam(params.get("endpointA"))
        if params.get("endpointZ") is not None:
            self.endpointZ = CreateEndpointParam(params.get("endpointZ"))


class InquiryCreatePrivateConnectPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.privateConnectPrice = None
        self.privateConnectBandwidth = None
        self.endpointAPrice = None
        self.endpointABandwidth = None
        self.endpointZPrice = None
        self.endpointZBandwidth = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("privateConnectPrice") is not None:
            self.privateConnectPrice = PriceItem(params.get("privateConnectPrice"))
        self.privateConnectBandwidth = params.get("privateConnectBandwidth")
        if params.get("endpointAPrice") is not None:
            self.endpointAPrice = PriceItem(params.get("endpointAPrice"))
        self.endpointABandwidth = params.get("endpointABandwidth")
        if params.get("endpointZPrice") is not None:
            self.endpointZPrice = PriceItem(params.get("endpointZPrice"))
        self.endpointZBandwidth = params.get("endpointZBandwidth")


