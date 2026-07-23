#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel
import warnings

class DescribeIPTransitDatacentersRequest(AbstractModel):
    def __init__(self):
        self.peerPortId = None
        self.peerDcId = None
        self.zbgRegionId = None

    def _deserialize(self, params):
        self.peerPortId = params.get("peerPortId")
        self.peerDcId = params.get("peerDcId")
        self.zbgRegionId = params.get("zbgRegionId")


class DescribeIPTransitDatacentersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.supportSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("supportSet") is not None:
            self.supportSet = []
            for item in params.get("supportSet"):
                obj = IPTransitDatacenter(item)
                self.supportSet.append(obj)


class IPTransitDatacenter(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dataCenter = None
        self.availableRoutingTypes = None

    def _deserialize(self, params):
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        if params.get("availableRoutingTypes") is not None:
            self.availableRoutingTypes = []
            for item in params.get("availableRoutingTypes"):
                obj = RemoteIptAvailableRoutingType(item)
                self.availableRoutingTypes.append(obj)


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


class RemoteIptAvailableRoutingType(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.routingType = None
        self.availableBgpRouteTypes = None
        self.deliveryType = None
        self.publicInterconnectNetmasks = None

    def _deserialize(self, params):
        self.routingType = params.get("routingType")
        self.availableBgpRouteTypes = params.get("availableBgpRouteTypes")
        self.deliveryType = params.get("deliveryType")
        self.publicInterconnectNetmasks = params.get("publicInterconnectNetmasks")


class DescribeIPTransitAvailableAsnsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeIPTransitAvailableAsnsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = AsnInfo(item)
                self.dataSet.append(obj)


class AsnInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.asn = None
        self.asnType = None

    def _deserialize(self, params):
        self.asn = params.get("asn")
        self.asnType = params.get("asnType")


class DescribeIPTransitAvailableCidrBlocksRequest(AbstractModel):
    def __init__(self):
        self.iptDcId = None
        self.routingType = None
        self.zbgRegionId = None
        self.ipUuid = None

    def _deserialize(self, params):
        self.iptDcId = params.get("iptDcId")
        self.routingType = params.get("routingType")
        self.zbgRegionId = params.get("zbgRegionId")
        self.ipUuid = params.get("ipUuid")


class DescribeIPTransitAvailableCidrBlocksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.ipv4CidrBlocks = None
        self.ipv6CidrBlocks = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("ipv4CidrBlocks") is not None:
            self.ipv4CidrBlocks = []
            for item in params.get("ipv4CidrBlocks"):
                obj = CidrBlock(item)
                self.ipv4CidrBlocks.append(obj)
        if params.get("ipv6CidrBlocks") is not None:
            self.ipv6CidrBlocks = []
            for item in params.get("ipv6CidrBlocks"):
                obj = CidrBlock(item)
                self.ipv6CidrBlocks.append(obj)


class CidrBlock(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.netmask = None
        self.ipNetworkType = None

    def _deserialize(self, params):
        self.netmask = params.get("netmask")
        self.ipNetworkType = params.get("ipNetworkType")


class InquiryCreateIPTransitPriceRequest(AbstractModel):
    def __init__(self):
        self.peerPortId = None
        self.iptDcId = None
        self.internetType = None
        self.commitBandwidth = None
        self.bandwidth = None
        self.routingType = None
        self.publicIPv4BlockSize = None
        self.bgpRouteType = None
        self.ipType = None
        self.publicIpList = None
        self.zbgRegionId = None
        self.haConfig = None
        self.publicInterconnectNetmask = None

    def _deserialize(self, params):
        self.peerPortId = params.get("peerPortId")
        self.iptDcId = params.get("iptDcId")
        self.internetType = params.get("internetType")
        self.commitBandwidth = params.get("commitBandwidth")
        self.bandwidth = params.get("bandwidth")
        self.routingType = params.get("routingType")
        self.publicIPv4BlockSize = params.get("publicIPv4BlockSize")
        self.bgpRouteType = params.get("bgpRouteType")
        self.ipType = params.get("ipType")
        if params.get("publicIpList") is not None:
            self.publicIpList = []
            for item in params.get("publicIpList"):
                obj = IPTransitIpRequest(item)
                self.publicIpList.append(obj)
        self.zbgRegionId = params.get("zbgRegionId")
        if params.get("haConfig") is not None:
            self.haConfig = IPTransitHaConfig(params.get("haConfig"))
        self.publicInterconnectNetmask = params.get("publicInterconnectNetmask")


class IPTransitIpRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.netmask = None
        self.ipType = None
        self.ipNetworkType = None
        self.amount = None

    def _deserialize(self, params):
        self.netmask = params.get("netmask")
        self.ipType = params.get("ipType")
        self.ipNetworkType = params.get("ipNetworkType")
        self.amount = params.get("amount")


class IPTransitHaConfig(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.haMode = None
        self.secondaryPortId = None
        self.secondaryPortVlanId = None

    def _deserialize(self, params):
        self.haMode = params.get("haMode")
        self.secondaryPortId = params.get("secondaryPortId")
        self.secondaryPortVlanId = params.get("secondaryPortVlanId")


class InquiryCreateIPTransitPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.privateConnectPrice = None
        self.iptBandwidthPrice = None
        self.publicIpPrices = None
        self.publicInterconnectIpPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("privateConnectPrice") is not None:
            self.privateConnectPrice = PriceItem(params.get("privateConnectPrice"))
        if params.get("iptBandwidthPrice") is not None:
            self.iptBandwidthPrice = PriceItem(params.get("iptBandwidthPrice"))
        if params.get("publicIpPrices") is not None:
            self.publicIpPrices = []
            for item in params.get("publicIpPrices"):
                obj = IPPrice(item)
                self.publicIpPrices.append(obj)
        if params.get("publicInterconnectIpPrice") is not None:
            self.publicInterconnectIpPrice = IPPrice(params.get("publicInterconnectIpPrice"))


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


class IPPrice(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.price = None
        self.netmask = None
        self.qty = None
        self.ipNetworkType = None

    def _deserialize(self, params):
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.netmask = params.get("netmask")
        self.qty = params.get("qty")
        self.ipNetworkType = params.get("ipNetworkType")


class CreateIPTransitRequest(AbstractModel):
    def __init__(self):
        self.iptName = None
        self.iptDescription = None
        self.peerPortId = None
        self.peerPortVlan = None
        self.iptDcId = None
        self.internetType = None
        self.commitBandwidth = None
        self.bandwidth = None
        self.routingType = None
        self.publicIPv4BlockSize = None
        self.bfd = None
        self.resourceGroupId = None
        self.bgp = None
        self.tags = None
        self.publicIpList = None
        self.zbgRegionId = None
        self.haConfig = None
        self.publicInterconnectNetmask = None

    def _deserialize(self, params):
        self.iptName = params.get("iptName")
        self.iptDescription = params.get("iptDescription")
        self.peerPortId = params.get("peerPortId")
        self.peerPortVlan = params.get("peerPortVlan")
        self.iptDcId = params.get("iptDcId")
        self.internetType = params.get("internetType")
        self.commitBandwidth = params.get("commitBandwidth")
        self.bandwidth = params.get("bandwidth")
        self.routingType = params.get("routingType")
        self.publicIPv4BlockSize = params.get("publicIPv4BlockSize")
        if params.get("bfd") is not None:
            self.bfd = BFDConfig(params.get("bfd"))
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("bgp") is not None:
            self.bgp = RiptBgpConfig(params.get("bgp"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))
        if params.get("publicIpList") is not None:
            self.publicIpList = []
            for item in params.get("publicIpList"):
                obj = IPTransitIpRequest(item)
                self.publicIpList.append(obj)
        self.zbgRegionId = params.get("zbgRegionId")
        if params.get("haConfig") is not None:
            self.haConfig = IPTransitHaConfig(params.get("haConfig"))
        self.publicInterconnectNetmask = params.get("publicInterconnectNetmask")


class BFDConfig(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.bfdTxInterval = None
        self.bfdRxInterval = None
        self.bfdMultiplier = None

    def _deserialize(self, params):
        self.bfdTxInterval = params.get("bfdTxInterval")
        self.bfdRxInterval = params.get("bfdRxInterval")
        self.bfdMultiplier = params.get("bfdMultiplier")


class RiptBgpConfig(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.routeType = None
        self.asn = None
        self.password = None
        self.asnList = None
        self.asSetList = None

    def _deserialize(self, params):
        self.routeType = params.get("routeType")
        self.asn = params.get("asn")
        self.password = params.get("password")
        self.asnList = params.get("asnList")
        self.asSetList = params.get("asSetList")


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


class CreateIPTransitResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.iptId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.iptId = params.get("iptId")


class DescribeIPTransitsRequest(AbstractModel):
    def __init__(self):
        self.iptIds = None
        self.iptName = None
        self.resourceGroupId = None
        self.peerPortId = None
        self.iptDcId = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.iptIds = params.get("iptIds")
        self.iptName = params.get("iptName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.peerPortId = params.get("peerPortId")
        self.iptDcId = params.get("iptDcId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeIPTransitsResponse(AbstractModel):
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
                obj = IPTransit(item)
                self.dataSet.append(obj)


class IPTransit(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.iptId = None
        self.iptName = None
        self.iptDescription = None
        self.dataCenter = None
        self.peerPortId = None
        self.peerPortName = None
        self.peerDataCenter = None
        self.deliveryType = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.createTime = None
        self.routingType = None
        self.internetType = None
        self.bandwidth = None
        self.commitBandwidth = None
        self.bfd = None
        self.bgp = None
        self.interconnect = None
        self.privateConnectId = None
        self.privateConnectName = None
        self.publicIpv4Addresses = None
        self.iptStatus = None
        self.connectivityStatus = None
        self.tags = None
        self.publicIpAddresses = None
        self.haMode = None
        self.zbgRegionId = None
        self.peerPortType = None
        self.haLinks = None

    def _deserialize(self, params):
        self.iptId = params.get("iptId")
        self.iptName = params.get("iptName")
        self.iptDescription = params.get("iptDescription")
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        self.peerPortId = params.get("peerPortId")
        self.peerPortName = params.get("peerPortName")
        if params.get("peerDataCenter") is not None:
            self.peerDataCenter = DatacenterInfo(params.get("peerDataCenter"))
        self.deliveryType = params.get("deliveryType")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.createTime = params.get("createTime")
        self.routingType = params.get("routingType")
        self.internetType = params.get("internetType")
        self.bandwidth = params.get("bandwidth")
        self.commitBandwidth = params.get("commitBandwidth")
        if params.get("bfd") is not None:
            self.bfd = BFDConfig(params.get("bfd"))
        if params.get("bgp") is not None:
            self.bgp = RiptBgpConfig(params.get("bgp"))
        if params.get("interconnect") is not None:
            self.interconnect = Interconnect(params.get("interconnect"))
        self.privateConnectId = params.get("privateConnectId")
        self.privateConnectName = params.get("privateConnectName")
        if params.get("publicIpv4Addresses") is not None:
            self.publicIpv4Addresses = []
            for item in params.get("publicIpv4Addresses"):
                obj = IPAddress(item)
                self.publicIpv4Addresses.append(obj)
        self.iptStatus = params.get("iptStatus")
        self.connectivityStatus = params.get("connectivityStatus")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))
        if params.get("publicIpAddresses") is not None:
            self.publicIpAddresses = []
            for item in params.get("publicIpAddresses"):
                obj = IPTransitIpAddress(item)
                self.publicIpAddresses.append(obj)
        self.haMode = params.get("haMode")
        self.zbgRegionId = params.get("zbgRegionId")
        self.peerPortType = params.get("peerPortType")
        if params.get("haLinks") is not None:
            self.haLinks = []
            for item in params.get("haLinks"):
                obj = HaLink(item)
                self.haLinks.append(obj)


class Interconnect(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.vendorIpv4Address = None
        self.customerIpv4Address = None
        self.vendorIpv6Address = None
        self.customerIpv6Address = None

    def _deserialize(self, params):
        self.vendorIpv4Address = params.get("vendorIpv4Address")
        self.customerIpv4Address = params.get("customerIpv4Address")
        self.vendorIpv6Address = params.get("vendorIpv6Address")
        self.customerIpv6Address = params.get("customerIpv6Address")


class IPAddress(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.ipAddress = None
        self.netmask = None
        self.gatewayIpAddress = None

    def _deserialize(self, params):
        self.ipAddress = params.get("ipAddress")
        self.netmask = params.get("netmask")
        self.gatewayIpAddress = params.get("gatewayIpAddress")


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


class IPTransitIpAddress(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.ipUuid = None
        self.ipAddress = None
        self.netmask = None
        self.gatewayIpAddress = None
        self.ipType = None
        self.ipNetworkType = None

    def _deserialize(self, params):
        self.ipUuid = params.get("ipUuid")
        self.ipAddress = params.get("ipAddress")
        self.netmask = params.get("netmask")
        self.gatewayIpAddress = params.get("gatewayIpAddress")
        self.ipType = params.get("ipType")
        self.ipNetworkType = params.get("ipNetworkType")


class HaLink(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.isPrimary = None
        self.iptStatus = None
        self.connectivityStatus = None
        self.privateConnectId = None
        self.privateConnectName = None
        self.peerPortId = None
        self.peerPortName = None
        self.peerDataCenter = None
        self.peerPortVlan = None
        self.interconnect = None

    def _deserialize(self, params):
        self.isPrimary = params.get("isPrimary")
        self.iptStatus = params.get("iptStatus")
        self.connectivityStatus = params.get("connectivityStatus")
        self.privateConnectId = params.get("privateConnectId")
        self.privateConnectName = params.get("privateConnectName")
        self.peerPortId = params.get("peerPortId")
        self.peerPortName = params.get("peerPortName")
        if params.get("peerDataCenter") is not None:
            self.peerDataCenter = DatacenterInfo(params.get("peerDataCenter"))
        self.peerPortVlan = params.get("peerPortVlan")
        if params.get("interconnect") is not None:
            self.interconnect = Interconnect(params.get("interconnect"))


class ModifyIPTransitBandwidthRequest(AbstractModel):
    def __init__(self):
        self.iptId = None
        self.bandwidth = None
        self.commitBandwidth = None

    def _deserialize(self, params):
        self.iptId = params.get("iptId")
        self.bandwidth = params.get("bandwidth")
        self.commitBandwidth = params.get("commitBandwidth")


class ModifyIPTransitBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyIPTransitsAttributeRequest(AbstractModel):
    def __init__(self):
        self.iptIds = None
        self.iptName = None
        self.iptDescription = None

    def _deserialize(self, params):
        self.iptIds = params.get("iptIds")
        self.iptName = params.get("iptName")
        self.iptDescription = params.get("iptDescription")


class ModifyIPTransitsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteIPTransitRequest(AbstractModel):
    def __init__(self):
        self.iptId = None

    def _deserialize(self, params):
        self.iptId = params.get("iptId")


class DeleteIPTransitResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeIPTransitTrafficRequest(AbstractModel):
    def __init__(self):
        self.iptId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.iptId = params.get("iptId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeIPTransitTrafficResponse(AbstractModel):
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


class InquiryModifyIPTransitPriceRequest(AbstractModel):
    def __init__(self):
        self.iptId = None
        self.type = None
        self.bandwidth = None
        self.commitBandwidth = None
        self.publicIPv4BlockSize = None
        self.ipUuid = None
        self.ipNetworkType = None

    def _deserialize(self, params):
        self.iptId = params.get("iptId")
        self.type = params.get("type")
        self.bandwidth = params.get("bandwidth")
        self.commitBandwidth = params.get("commitBandwidth")
        self.publicIPv4BlockSize = params.get("publicIPv4BlockSize")
        self.ipUuid = params.get("ipUuid")
        self.ipNetworkType = params.get("ipNetworkType")


class InquiryModifyIPTransitPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.privateConnectPrice = None
        self.privateConnectBandwidth = None
        self.iptPrice = None
        self.iptIpPrices = None
        self.publicInterconnectIpPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("privateConnectPrice") is not None:
            self.privateConnectPrice = PriceItem(params.get("privateConnectPrice"))
        self.privateConnectBandwidth = params.get("privateConnectBandwidth")
        if params.get("iptPrice") is not None:
            self.iptPrice = PriceItem(params.get("iptPrice"))
        if params.get("iptIpPrices") is not None:
            self.iptIpPrices = []
            for item in params.get("iptIpPrices"):
                obj = IPTransitIpPriceItem(item)
                self.iptIpPrices.append(obj)
        if params.get("publicInterconnectIpPrice") is not None:
            self.publicInterconnectIpPrice = IPTransitIpPriceItem(params.get("publicInterconnectIpPrice"))


class IPTransitIpPriceItem(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.price = None
        self.netmask = None
        self.amount = None
        self.ipNetworkType = None

    def _deserialize(self, params):
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))
        self.netmask = params.get("netmask")
        self.amount = params.get("amount")
        self.ipNetworkType = params.get("ipNetworkType")


class ModifyIPTransitConfigRequest(AbstractModel):
    def __init__(self):
        self.iptId = None
        self.type = None
        self.bandwidth = None
        self.commitBandwidth = None
        self.bfd = None
        self.bgp = None
        self.publicIPv4BlockSize = None
        self.ipUuid = None
        self.ipNetworkType = None

    def _deserialize(self, params):
        self.iptId = params.get("iptId")
        self.type = params.get("type")
        self.bandwidth = params.get("bandwidth")
        self.commitBandwidth = params.get("commitBandwidth")
        if params.get("bfd") is not None:
            self.bfd = BFDConfig(params.get("bfd"))
        if params.get("bgp") is not None:
            self.bgp = BgpConfigParam(params.get("bgp"))
        self.publicIPv4BlockSize = params.get("publicIPv4BlockSize")
        self.ipUuid = params.get("ipUuid")
        self.ipNetworkType = params.get("ipNetworkType")


class BgpConfigParam(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.routeType = None
        self.asnList = None
        self.asSetList = None
        self.password = None

    def _deserialize(self, params):
        self.routeType = params.get("routeType")
        self.asnList = params.get("asnList")
        self.asSetList = params.get("asSetList")
        self.password = params.get("password")


class ModifyIPTransitConfigResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


