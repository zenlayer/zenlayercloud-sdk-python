#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel
import warnings

class DescribeSubnetAvailableResourcesRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")


class DescribeSubnetAvailableResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.zoneIdSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.zoneIdSet = params.get("zoneIdSet")


class ModifySubnetsAttributeRequest(AbstractModel):
    def __init__(self):
        self.subnetName = None
        self.subnetIds = None

    def _deserialize(self, params):
        self.subnetName = params.get("subnetName")
        self.subnetIds = params.get("subnetIds")


class ModifySubnetsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CreateSubnetRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.cidrBlock = None
        self.subnetName = None
        self.resourceGroupId = None
        self.vpcId = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.cidrBlock = params.get("cidrBlock")
        self.subnetName = params.get("subnetName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.vpcId = params.get("vpcId")


class CreateSubnetResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.subnetId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.subnetId = params.get("subnetId")


class DescribeSubnetsRequest(AbstractModel):
    def __init__(self):
        self.subnetIds = None
        self.subnetName = None
        self.cidrBlock = None
        self.subnetStatus = None
        self.zoneId = None
        self.vpcId = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.subnetIds = params.get("subnetIds")
        self.subnetName = params.get("subnetName")
        self.cidrBlock = params.get("cidrBlock")
        self.subnetStatus = params.get("subnetStatus")
        self.zoneId = params.get("zoneId")
        self.vpcId = params.get("vpcId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeSubnetsResponse(AbstractModel):
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
                obj = SubnetInfo(item)
                self.dataSet.append(obj)


class SubnetInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.subnetId = None
        self.subnetName = None
        self.zoneId = None
        self.availableIpCount = None
        self.cidrBlock = None
        self.subnetStatus = None
        self.createTime = None
        self.vpcSubnetStatus = None
        self.vpcId = None
        self.vpcName = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.subnetInstanceSet = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.subnetName = params.get("subnetName")
        self.zoneId = params.get("zoneId")
        self.availableIpCount = params.get("availableIpCount")
        self.cidrBlock = params.get("cidrBlock")
        self.subnetStatus = params.get("subnetStatus")
        self.createTime = params.get("createTime")
        self.vpcSubnetStatus = params.get("vpcSubnetStatus")
        self.vpcId = params.get("vpcId")
        self.vpcName = params.get("vpcName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        if params.get("subnetInstanceSet") is not None:
            self.subnetInstanceSet = []
            for item in params.get("subnetInstanceSet"):
                obj = SubnetInstance(item)
                self.subnetInstanceSet.append(obj)


class SubnetInstance(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.privateIpAddress = None
        self.privateIpStatus = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.privateIpAddress = params.get("privateIpAddress")
        self.privateIpStatus = params.get("privateIpStatus")


class AssociateSubnetInstancesRequest(AbstractModel):
    def __init__(self):
        self.subnetId = None
        self.subnetInstanceList = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        if params.get("subnetInstanceList") is not None:
            self.subnetInstanceList = []
            for item in params.get("subnetInstanceList"):
                obj = AssociateSubnetInstance(item)
                self.subnetInstanceList.append(obj)


class AssociateSubnetInstance(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.privateIpAddress = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.privateIpAddress = params.get("privateIpAddress")


class AssociateSubnetInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnAssociateSubnetInstanceRequest(AbstractModel):
    def __init__(self):
        self.subnetId = None
        self.instanceId = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.instanceId = params.get("instanceId")


class UnAssociateSubnetInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AssociateVpcSubnetRequest(AbstractModel):
    def __init__(self):
        self.subnetId = None
        self.vpcId = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.vpcId = params.get("vpcId")


class AssociateVpcSubnetResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteSubnetRequest(AbstractModel):
    def __init__(self):
        self.subnetId = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")


class DeleteSubnetResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeZonesRequest(AbstractModel):
    def __init__(self):
        self.acceptLanguage = None
        self.isCloudRouterAvailable = None

    def _deserialize(self, params):
        self.acceptLanguage = params.get("acceptLanguage")
        self.isCloudRouterAvailable = params.get("isCloudRouterAvailable")


class DescribeZonesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.zoneSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("zoneSet") is not None:
            self.zoneSet = []
            for item in params.get("zoneSet"):
                obj = Zone(item)
                self.zoneSet.append(obj)


class Zone(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.zoneName = None
        self.cityName = None
        self.areaName = None
        self.isCloudRouterAvailable = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.zoneName = params.get("zoneName")
        self.cityName = params.get("cityName")
        self.areaName = params.get("areaName")
        self.isCloudRouterAvailable = params.get("isCloudRouterAvailable")


class DescribeInstanceTypesRequest(AbstractModel):
    def __init__(self):
        self.imageId = None
        self.instanceTypeIds = None
        self.minimumCpuCoreCount = None
        self.maximumCpuCoreCount = None
        self.minimumMemorySize = None
        self.maximumMemorySize = None
        self.minimumBandwidth = None
        self.supportRaids = None
        self.supportSubnet = None
        self.minimumDiskSize = None
        self.maximumDiskSize = None
        self.isHA = None

    def _deserialize(self, params):
        self.imageId = params.get("imageId")
        self.instanceTypeIds = params.get("instanceTypeIds")
        self.minimumCpuCoreCount = params.get("minimumCpuCoreCount")
        self.maximumCpuCoreCount = params.get("maximumCpuCoreCount")
        self.minimumMemorySize = params.get("minimumMemorySize")
        self.maximumMemorySize = params.get("maximumMemorySize")
        self.minimumBandwidth = params.get("minimumBandwidth")
        self.supportRaids = params.get("supportRaids")
        self.supportSubnet = params.get("supportSubnet")
        self.minimumDiskSize = params.get("minimumDiskSize")
        self.maximumDiskSize = params.get("maximumDiskSize")
        self.isHA = params.get("isHA")


class DescribeInstanceTypesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceTypes = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("instanceTypes") is not None:
            self.instanceTypes = []
            for item in params.get("instanceTypes"):
                obj = InstanceType(item)
                self.instanceTypes.append(obj)


class InstanceType(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.imageIds = None
        self.instanceTypeId = None
        self.description = None
        self.cpuCoreCount = None
        self.cpuDetail = None
        self.cpuCores = None
        self.cpuThreads = None
        self.baseFrequency = None
        self.memorySize = None
        self.maximumBandwidth = None
        self.supportRaids = None
        self.supportSubnet = None
        self.isHA = None
        self.diskInfo = None

    def _deserialize(self, params):
        self.imageIds = params.get("imageIds")
        self.instanceTypeId = params.get("instanceTypeId")
        self.description = params.get("description")
        self.cpuCoreCount = params.get("cpuCoreCount")
        self.cpuDetail = params.get("cpuDetail")
        self.cpuCores = params.get("cpuCores")
        self.cpuThreads = params.get("cpuThreads")
        self.baseFrequency = params.get("baseFrequency")
        self.memorySize = params.get("memorySize")
        self.maximumBandwidth = params.get("maximumBandwidth")
        self.supportRaids = params.get("supportRaids")
        self.supportSubnet = params.get("supportSubnet")
        self.isHA = params.get("isHA")
        if params.get("diskInfo") is not None:
            self.diskInfo = InstanceDiskInfo(params.get("diskInfo"))


class InstanceDiskInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.totalDiskSize = None
        self.diskDescription = None
        self.disks = None

    def _deserialize(self, params):
        self.totalDiskSize = params.get("totalDiskSize")
        self.diskDescription = params.get("diskDescription")
        if params.get("disks") is not None:
            self.disks = []
            for item in params.get("disks"):
                obj = Disk(item)
                self.disks.append(obj)


class Disk(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.diskSize = None
        self.diskCount = None

    def _deserialize(self, params):
        self.diskSize = params.get("diskSize")
        self.diskCount = params.get("diskCount")


class DescribeAvailableResourcesRequest(AbstractModel):
    def __init__(self):
        self.instanceChargeType = None
        self.instanceTypeId = None
        self.zoneId = None
        self.sellStatus = None

    def _deserialize(self, params):
        self.instanceChargeType = params.get("instanceChargeType")
        self.instanceTypeId = params.get("instanceTypeId")
        self.zoneId = params.get("zoneId")
        self.sellStatus = params.get("sellStatus")


class DescribeAvailableResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.availableResources = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("availableResources") is not None:
            self.availableResources = []
            for item in params.get("availableResources"):
                obj = AvailableResource(item)
                self.availableResources.append(obj)


class AvailableResource(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.sellStatus = None
        self.internetChargeTypes = None
        self.instanceTypeId = None
        self.maximumBandwidthOut = None
        self.defaultBandwidthOut = None
        self.defaultTrafficPackageSize = None
        self.qty = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.sellStatus = params.get("sellStatus")
        self.internetChargeTypes = params.get("internetChargeTypes")
        self.instanceTypeId = params.get("instanceTypeId")
        self.maximumBandwidthOut = params.get("maximumBandwidthOut")
        self.defaultBandwidthOut = params.get("defaultBandwidthOut")
        self.defaultTrafficPackageSize = params.get("defaultTrafficPackageSize")
        self.qty = params.get("qty")


class InquiryPriceCreateInstanceRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.instanceTypeId = None
        self.instanceChargeType = None
        self.instanceChargePrepaid = None
        self.trafficPackageSize = None
        self.internetMaxBandwidthOut = None
        self.internetChargeType = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceTypeId = params.get("instanceTypeId")
        self.instanceChargeType = params.get("instanceChargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")
        self.internetChargeType = params.get("internetChargeType")


class ChargePrepaid(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.period = None

    def _deserialize(self, params):
        self.period = params.get("period")


class InquiryPriceCreateInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instancePrice = None
        self.bandwidthPrice = None
        self.primaryIpPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("instancePrice") is not None:
            self.instancePrice = PriceItem(params.get("instancePrice"))
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = []
            for item in params.get("bandwidthPrice"):
                obj = PriceItem(item)
                self.bandwidthPrice.append(obj)
        if params.get("primaryIpPrice") is not None:
            self.primaryIpPrice = PriceItem(params.get("primaryIpPrice"))


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


class DescribeImagesRequest(AbstractModel):
    def __init__(self):
        self.imageIds = None
        self.imageName = None
        self.catalog = None
        self.imageType = None
        self.osType = None
        self.instanceTypeId = None

    def _deserialize(self, params):
        self.imageIds = params.get("imageIds")
        self.imageName = params.get("imageName")
        self.catalog = params.get("catalog")
        self.imageType = params.get("imageType")
        self.osType = params.get("osType")
        self.instanceTypeId = params.get("instanceTypeId")


class DescribeImagesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.images = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("images") is not None:
            self.images = []
            for item in params.get("images"):
                obj = ImageInfo(item)
                self.images.append(obj)


class ImageInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.imageId = None
        self.imageName = None
        self.catalog = None
        self.imageType = None
        self.osType = None

    def _deserialize(self, params):
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")
        self.catalog = params.get("catalog")
        self.imageType = params.get("imageType")
        self.osType = params.get("osType")


class CreateInstancesRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.instanceChargeType = None
        self.instanceChargePrepaid = None
        self.instanceTypeId = None
        self.imageId = None
        self.resourceGroupId = None
        self.instanceName = None
        self.hostname = None
        self.amount = None
        self.password = None
        self.keyId = None
        self.internetChargeType = None
        self.internetMaxBandwidthOut = None
        self.trafficPackageSize = None
        self.subnetId = None
        self.raidConfig = None
        self.partitions = None
        self.nic = None
        self.ipxeUrl = None
        self.userData = None
        self.enablePrimaryIPv6 = None
        self.clusterId = None
        self.marketingOptions = None
        self.tags = None
        self.enableGatewayMode = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceChargeType = params.get("instanceChargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.instanceTypeId = params.get("instanceTypeId")
        self.imageId = params.get("imageId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.instanceName = params.get("instanceName")
        self.hostname = params.get("hostname")
        self.amount = params.get("amount")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.internetChargeType = params.get("internetChargeType")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.subnetId = params.get("subnetId")
        if params.get("raidConfig") is not None:
            self.raidConfig = RaidConfig(params.get("raidConfig"))
        if params.get("partitions") is not None:
            self.partitions = []
            for item in params.get("partitions"):
                obj = Partition(item)
                self.partitions.append(obj)
        if params.get("nic") is not None:
            self.nic = Nic(params.get("nic"))
        self.ipxeUrl = params.get("ipxeUrl")
        self.userData = params.get("userData")
        self.enablePrimaryIPv6 = params.get("enablePrimaryIPv6")
        self.clusterId = params.get("clusterId")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))
        self.enableGatewayMode = params.get("enableGatewayMode")


class RaidConfig(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.raidType = None
        self.customRaids = None

    def _deserialize(self, params):
        self.raidType = params.get("raidType")
        if params.get("customRaids") is not None:
            self.customRaids = []
            for item in params.get("customRaids"):
                obj = CustomRaid(item)
                self.customRaids.append(obj)


class CustomRaid(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.raidType = None
        self.diskSequence = None

    def _deserialize(self, params):
        self.raidType = params.get("raidType")
        self.diskSequence = params.get("diskSequence")


class Partition(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.fsPath = None
        self.fsType = None
        self.size = None

    def _deserialize(self, params):
        self.fsPath = params.get("fsPath")
        self.fsType = params.get("fsType")
        self.size = params.get("size")


class Nic(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.wanName = None
        self.lanName = None

    def _deserialize(self, params):
        self.wanName = params.get("wanName")
        self.lanName = params.get("lanName")


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


class CreateInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceIdSet = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.instanceIdSet = params.get("instanceIdSet")
        self.orderNumber = params.get("orderNumber")


class DescribeInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.zoneId = None
        self.resourceGroupId = None
        self.instanceTypeId = None
        self.internetChargeType = None
        self.imageId = None
        self.subnetId = None
        self.instanceStatus = None
        self.instanceName = None
        self.hostname = None
        self.publicIpAddresses = None
        self.privateIpAddresses = None
        self.pageNum = None
        self.pageSize = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.zoneId = params.get("zoneId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.instanceTypeId = params.get("instanceTypeId")
        self.internetChargeType = params.get("internetChargeType")
        self.imageId = params.get("imageId")
        self.subnetId = params.get("subnetId")
        self.instanceStatus = params.get("instanceStatus")
        self.instanceName = params.get("instanceName")
        self.hostname = params.get("hostname")
        self.publicIpAddresses = params.get("publicIpAddresses")
        self.privateIpAddresses = params.get("privateIpAddresses")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeInstancesResponse(AbstractModel):
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
                obj = InstanceInfo(item)
                self.dataSet.append(obj)


class InstanceInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.zoneId = None
        self.instanceName = None
        self.hostname = None
        self.instanceTypeId = None
        self.instanceType = None
        self.imageId = None
        self.imageName = None
        self.ipxeUrl = None
        self.instanceChargeType = None
        self.bandwidthOutMbps = None
        self.internetChargeType = None
        self.period = None
        self.primaryPublicIpAddress = None
        self.primaryPublicIPv6Address = None
        self.publicIpAddresses = None
        self.privateIpAddresses = None
        self.ipv6Addresses = None
        self.subnetIds = None
        self.createTime = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.instanceStatus = None
        self.trafficPackageSize = None
        self.raidConfig = None
        self.partitions = None
        self.nic = None
        self.autoRenew = None
        self.keyId = None
        self.tags = None
        self.enableGatewayMode = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.zoneId = params.get("zoneId")
        self.instanceName = params.get("instanceName")
        self.hostname = params.get("hostname")
        self.instanceTypeId = params.get("instanceTypeId")
        if params.get("instanceType") is not None:
            self.instanceType = InstanceType(params.get("instanceType"))
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")
        self.ipxeUrl = params.get("ipxeUrl")
        self.instanceChargeType = params.get("instanceChargeType")
        self.bandwidthOutMbps = params.get("bandwidthOutMbps")
        self.internetChargeType = params.get("internetChargeType")
        self.period = params.get("period")
        self.primaryPublicIpAddress = params.get("primaryPublicIpAddress")
        self.primaryPublicIPv6Address = params.get("primaryPublicIPv6Address")
        self.publicIpAddresses = params.get("publicIpAddresses")
        self.privateIpAddresses = params.get("privateIpAddresses")
        self.ipv6Addresses = params.get("ipv6Addresses")
        self.subnetIds = params.get("subnetIds")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.instanceStatus = params.get("instanceStatus")
        self.trafficPackageSize = params.get("trafficPackageSize")
        if params.get("raidConfig") is not None:
            self.raidConfig = RaidConfig(params.get("raidConfig"))
        if params.get("partitions") is not None:
            self.partitions = []
            for item in params.get("partitions"):
                obj = Partition(item)
                self.partitions.append(obj)
        if params.get("nic") is not None:
            self.nic = Nic(params.get("nic"))
        self.autoRenew = params.get("autoRenew")
        self.keyId = params.get("keyId")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))
        self.enableGatewayMode = params.get("enableGatewayMode")


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


class ModifyInstancesAttributeRequest(AbstractModel):
    def __init__(self):
        self.instanceName = None
        self.instanceIds = None

    def _deserialize(self, params):
        self.instanceName = params.get("instanceName")
        self.instanceIds = params.get("instanceIds")


class ModifyInstancesAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class StartInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")


class StartInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class StopInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")


class StopInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RebootInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")


class RebootInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ReinstallInstanceRequest(AbstractModel):
    def __init__(self):
        self.imageId = None
        self.hostname = None
        self.password = None
        self.keyId = None
        self.raidConfig = None
        self.partitions = None
        self.nic = None
        self.ipxeUrl = None
        self.userData = None
        self.instanceId = None

    def _deserialize(self, params):
        self.imageId = params.get("imageId")
        self.hostname = params.get("hostname")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        if params.get("raidConfig") is not None:
            self.raidConfig = RaidConfig(params.get("raidConfig"))
        if params.get("partitions") is not None:
            self.partitions = []
            for item in params.get("partitions"):
                obj = Partition(item)
                self.partitions.append(obj)
        if params.get("nic") is not None:
            self.nic = Nic(params.get("nic"))
        self.ipxeUrl = params.get("ipxeUrl")
        self.userData = params.get("userData")
        self.instanceId = params.get("instanceId")


class ReinstallInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyInstancesResourceGroupRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.resourceGroupId = params.get("resourceGroupId")


class ModifyInstancesResourceGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class TerminateInstanceRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class TerminateInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewInstanceRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class RenewInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ReleaseInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")


class ReleaseInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class InquiryPriceInstanceBandwidthRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.bandwidthOutMbps = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.bandwidthOutMbps = params.get("bandwidthOutMbps")


class InquiryPriceInstanceBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.bandwidthPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = []
            for item in params.get("bandwidthPrice"):
                obj = PriceItem(item)
                self.bandwidthPrice.append(obj)


class ModifyInstanceBandwidthRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.bandwidthOutMbps = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.bandwidthOutMbps = params.get("bandwidthOutMbps")


class ModifyInstanceBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")


class CancelInstanceBandwidthDowngradeRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class CancelInstanceBandwidthDowngradeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class InquiryPriceInstanceTrafficPackageRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.trafficPackageSize = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.trafficPackageSize = params.get("trafficPackageSize")


class InquiryPriceInstanceTrafficPackageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.trafficPackagePrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("trafficPackagePrice") is not None:
            self.trafficPackagePrice = []
            for item in params.get("trafficPackagePrice"):
                obj = PriceItem(item)
                self.trafficPackagePrice.append(obj)


class ModifyInstanceTrafficPackageRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.trafficPackageSize = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.trafficPackageSize = params.get("trafficPackageSize")


class ModifyInstanceTrafficPackageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")


class CancelInstanceTrafficPackageDowngradeRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class CancelInstanceTrafficPackageDowngradeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeInstanceInternetStatusRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class DescribeInstanceInternetStatusResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceId = None
        self.instanceName = None
        self.internetMaxBandwidthOut = None
        self.modifiedInternetMaxBandwidthOut = None
        self.modifiedBandwidthStatus = None
        self.trafficPackageSize = None
        self.modifiedTrafficPackageSize = None
        self.modifiedTrafficPackageStatus = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")
        self.modifiedInternetMaxBandwidthOut = params.get("modifiedInternetMaxBandwidthOut")
        self.modifiedBandwidthStatus = params.get("modifiedBandwidthStatus")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.modifiedTrafficPackageSize = params.get("modifiedTrafficPackageSize")
        self.modifiedTrafficPackageStatus = params.get("modifiedTrafficPackageStatus")


class DescribeInstanceTrafficRequest(AbstractModel):
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.instanceId = None

    def _deserialize(self, params):
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.instanceId = params.get("instanceId")


class DescribeInstanceTrafficResponse(AbstractModel):
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
                obj = InstanceTrafficData(item)
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


class InstanceTrafficData(AbstractModel):
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


class DescribeInstancesMonitorHealthRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")


class DescribeInstancesMonitorHealthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.monitorHealthList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("monitorHealthList") is not None:
            self.monitorHealthList = []
            for item in params.get("monitorHealthList"):
                obj = InstanceHealth(item)
                self.monitorHealthList.append(obj)


class InstanceHealth(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.cpuStatus = None
        self.diskStatus = None
        self.ipmiPing = None
        self.ipmiStatus = None
        self.memoryStatus = None
        self.psuStatus = None
        self.wanPortStatus = None
        self.fanStatus = None
        self.serverBrand = None
        self.serverModel = None
        self.cpuTemp = None
        self.cpu0Temp = None
        self.cpu1Temp = None
        self.cpu2Temp = None
        self.inletTemp = None
        self.tempUnit = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.cpuStatus = params.get("cpuStatus")
        self.diskStatus = params.get("diskStatus")
        self.ipmiPing = params.get("ipmiPing")
        self.ipmiStatus = params.get("ipmiStatus")
        self.memoryStatus = params.get("memoryStatus")
        self.psuStatus = params.get("psuStatus")
        self.wanPortStatus = params.get("wanPortStatus")
        self.fanStatus = params.get("fanStatus")
        self.serverBrand = params.get("serverBrand")
        self.serverModel = params.get("serverModel")
        self.cpuTemp = params.get("cpuTemp")
        self.cpu0Temp = params.get("cpu0Temp")
        self.cpu1Temp = params.get("cpu1Temp")
        self.cpu2Temp = params.get("cpu2Temp")
        self.inletTemp = params.get("inletTemp")
        self.tempUnit = params.get("tempUnit")


class DescribeAvailableIpv4ResourcesRequest(AbstractModel):
    def __init__(self):
        self.chargeType = None
        self.zoneId = None

    def _deserialize(self, params):
        self.chargeType = params.get("chargeType")
        self.zoneId = params.get("zoneId")


class DescribeAvailableIpv4ResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.availableIpv4Resources = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("availableIpv4Resources") is not None:
            self.availableIpv4Resources = []
            for item in params.get("availableIpv4Resources"):
                obj = AvailableIpv4Resource(item)
                self.availableIpv4Resources.append(obj)


class AvailableIpv4Resource(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.netmask = None
        self.sellStatus = None
        self.cidrType = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.netmask = params.get("netmask")
        self.sellStatus = params.get("sellStatus")
        self.cidrType = params.get("cidrType")


class InquiryPriceCreateIpv4BlockRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.chargeType = None
        self.cidrType = None
        self.chargePrepaid = None
        self.netmask = None
        self.amount = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.chargeType = params.get("chargeType")
        self.cidrType = params.get("cidrType")
        if params.get("chargePrepaid") is not None:
            self.chargePrepaid = ChargePrepaid(params.get("chargePrepaid"))
        self.netmask = params.get("netmask")
        self.amount = params.get("amount")


class InquiryPriceCreateIpv4BlockResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.price = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("price") is not None:
            self.price = PriceItem(params.get("price"))


class CreateIpv4BlockRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.name = None
        self.cidrType = None
        self.chargeType = None
        self.chargePrepaid = None
        self.netmask = None
        self.amount = None
        self.resourceGroupId = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.name = params.get("name")
        self.cidrType = params.get("cidrType")
        self.chargeType = params.get("chargeType")
        if params.get("chargePrepaid") is not None:
            self.chargePrepaid = ChargePrepaid(params.get("chargePrepaid"))
        self.netmask = params.get("netmask")
        self.amount = params.get("amount")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateIpv4BlockResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.cidrBlockIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.cidrBlockIds = params.get("cidrBlockIds")


class DescribeAvailableIpv6ResourcesRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")


class DescribeAvailableIpv6ResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.availableIpv6Resources = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("availableIpv6Resources") is not None:
            self.availableIpv6Resources = []
            for item in params.get("availableIpv6Resources"):
                obj = AvailableIpv6Resource(item)
                self.availableIpv6Resources.append(obj)


class AvailableIpv6Resource(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.sellStatus = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.sellStatus = params.get("sellStatus")


class CreateIpv6BlockRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.name = None
        self.amount = None
        self.resourceGroupId = None
        self.tags = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.name = params.get("name")
        self.amount = params.get("amount")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateIpv6BlockResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cidrBlockIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.cidrBlockIds = params.get("cidrBlockIds")


class DescribeCidrBlocksRequest(AbstractModel):
    def __init__(self):
        self.cidrBlockIds = None
        self.cidrBlock = None
        self.cidrBlockName = None
        self.zoneId = None
        self.cidrBlockType = None
        self.gateway = None
        self.chargeType = None
        self.resourceGroupId = None
        self.pageNum = None
        self.pageSize = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.cidrBlockIds = params.get("cidrBlockIds")
        self.cidrBlock = params.get("cidrBlock")
        self.cidrBlockName = params.get("cidrBlockName")
        self.zoneId = params.get("zoneId")
        self.cidrBlockType = params.get("cidrBlockType")
        self.gateway = params.get("gateway")
        self.chargeType = params.get("chargeType")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeCidrBlocksResponse(AbstractModel):
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
                obj = CidrBlockInfo(item)
                self.dataSet.append(obj)


class CidrBlockInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cidrBlockId = None
        self.cidrBlockType = None
        self.cidrType = None
        self.cidrBlockName = None
        self.zoneId = None
        self.cidrBlock = None
        self.gateway = None
        self.availableIpStart = None
        self.availableIpEnd = None
        self.availableIpCount = None
        self.instanceIds = None
        self.status = None
        self.chargeType = None
        self.createTime = None
        self.expireTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.tags = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")
        self.cidrBlockType = params.get("cidrBlockType")
        self.cidrType = params.get("cidrType")
        self.cidrBlockName = params.get("cidrBlockName")
        self.zoneId = params.get("zoneId")
        self.cidrBlock = params.get("cidrBlock")
        self.gateway = params.get("gateway")
        self.availableIpStart = params.get("availableIpStart")
        self.availableIpEnd = params.get("availableIpEnd")
        self.availableIpCount = params.get("availableIpCount")
        self.instanceIds = params.get("instanceIds")
        self.status = params.get("status")
        self.chargeType = params.get("chargeType")
        self.createTime = params.get("createTime")
        self.expireTime = params.get("expireTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class ModifyCidrBlocksAttributeRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.cidrBlockIds = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.cidrBlockIds = params.get("cidrBlockIds")


class ModifyCidrBlocksAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewCidrBlockRequest(AbstractModel):
    def __init__(self):
        self.cidrBlockId = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")


class RenewCidrBlockResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class TerminateCidrBlockRequest(AbstractModel):
    def __init__(self):
        self.cidrBlockId = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")


class TerminateCidrBlockResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ReleaseCidrBlocksRequest(AbstractModel):
    def __init__(self):
        self.cidrBlockIds = None

    def _deserialize(self, params):
        self.cidrBlockIds = params.get("cidrBlockIds")


class ReleaseCidrBlocksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeInstanceAvailableCidrBlockRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.cidrBlockType = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.cidrBlockType = params.get("cidrBlockType")


class DescribeInstanceAvailableCidrBlockResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceAvailableCidrBlocks = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("instanceAvailableCidrBlocks") is not None:
            self.instanceAvailableCidrBlocks = []
            for item in params.get("instanceAvailableCidrBlocks"):
                obj = InstanceAvailableCidrBlock(item)
                self.instanceAvailableCidrBlocks.append(obj)


class InstanceAvailableCidrBlock(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cidrBlockId = None
        self.zoneId = None
        self.cidrBlockType = None
        self.cidrType = None
        self.cidrBlock = None
        self.availableIps = None
        self.availableIpCount = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")
        self.zoneId = params.get("zoneId")
        self.cidrBlockType = params.get("cidrBlockType")
        self.cidrType = params.get("cidrType")
        self.cidrBlock = params.get("cidrBlock")
        self.availableIps = params.get("availableIps")
        self.availableIpCount = params.get("availableIpCount")


class DescribeCidrBlockIpsRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.ip = None
        self.cidrBlockId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.ip = params.get("ip")
        self.cidrBlockId = params.get("cidrBlockId")


class DescribeCidrBlockIpsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cidrBlockIps = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cidrBlockIps") is not None:
            self.cidrBlockIps = []
            for item in params.get("cidrBlockIps"):
                obj = CidrBlockIp(item)
                self.cidrBlockIps.append(obj)


class CidrBlockIp(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cidrBlockId = None
        self.cidrBlockType = None
        self.ip = None
        self.instanceId = None
        self.status = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")
        self.cidrBlockType = params.get("cidrBlockType")
        self.ip = params.get("ip")
        self.instanceId = params.get("instanceId")
        self.status = params.get("status")


class BindCidrBlockIpsRequest(AbstractModel):
    def __init__(self):
        self.ipBindList = None
        self.cidrBlockId = None

    def _deserialize(self, params):
        if params.get("ipBindList") is not None:
            self.ipBindList = []
            for item in params.get("ipBindList"):
                obj = IpBindParam(item)
                self.ipBindList.append(obj)
        self.cidrBlockId = params.get("cidrBlockId")


class IpBindParam(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.ip = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.ip = params.get("ip")


class BindCidrBlockIpsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnbindCidrBlockIpsRequest(AbstractModel):
    def __init__(self):
        self.ipList = None
        self.cidrBlockId = None

    def _deserialize(self, params):
        self.ipList = params.get("ipList")
        self.cidrBlockId = params.get("cidrBlockId")


class UnbindCidrBlockIpsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class InquiryPriceCreateEipAddressRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.eipChargeType = None
        self.eipChargePrepaid = None
        self.amount = None
        self.netmask = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.eipChargeType = params.get("eipChargeType")
        if params.get("eipChargePrepaid") is not None:
            self.eipChargePrepaid = ChargePrepaid(params.get("eipChargePrepaid"))
        self.amount = params.get("amount")
        self.netmask = params.get("netmask")


class InquiryPriceCreateEipAddressResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.eipPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("eipPrice") is not None:
            self.eipPrice = PriceItem(params.get("eipPrice"))


class DescribeEipAddressesRequest(AbstractModel):
    def __init__(self):
        self.eipIds = None
        self.eipChargeType = None
        self.ipAddress = None
        self.zoneId = None
        self.resourceGroupId = None
        self.eipStatus = None
        self.instanceId = None
        self.instanceName = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.eipIds = params.get("eipIds")
        self.eipChargeType = params.get("eipChargeType")
        self.ipAddress = params.get("ipAddress")
        self.zoneId = params.get("zoneId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.eipStatus = params.get("eipStatus")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeEipAddressesResponse(AbstractModel):
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
                obj = EipAddress(item)
                self.dataSet.append(obj)


class EipAddress(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.eipId = None
        self.zoneId = None
        self.ipAddress = None
        self.netmask = None
        self.instanceId = None
        self.instanceName = None
        self.eipChargeType = None
        self.period = None
        self.createTime = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.eipStatus = None
        self.tags = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.zoneId = params.get("zoneId")
        self.ipAddress = params.get("ipAddress")
        self.netmask = params.get("netmask")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.eipChargeType = params.get("eipChargeType")
        self.period = params.get("period")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.eipStatus = params.get("eipStatus")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class AllocateEipAddressesRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.eipChargeType = None
        self.eipChargePrepaid = None
        self.resourceGroupId = None
        self.amount = None
        self.netmask = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.eipChargeType = params.get("eipChargeType")
        if params.get("eipChargePrepaid") is not None:
            self.eipChargePrepaid = ChargePrepaid(params.get("eipChargePrepaid"))
        self.resourceGroupId = params.get("resourceGroupId")
        self.amount = params.get("amount")
        self.netmask = params.get("netmask")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class AllocateEipAddressesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.eipIdSet = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.eipIdSet = params.get("eipIdSet")
        self.orderNumber = params.get("orderNumber")


class ModifyEipAddressesResourceGroupRequest(AbstractModel):
    def __init__(self):
        self.eipIds = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.eipIds = params.get("eipIds")
        self.resourceGroupId = params.get("resourceGroupId")


class ModifyEipAddressesResourceGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeInstanceAvailableEipResourcesRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class DescribeInstanceAvailableEipResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceEipResources = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("instanceEipResources") is not None:
            self.instanceEipResources = []
            for item in params.get("instanceEipResources"):
                obj = InstanceAvailableEip(item)
                self.instanceEipResources.append(obj)


class InstanceAvailableEip(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.eipId = None
        self.ipAddress = None
        self.netmask = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.ipAddress = params.get("ipAddress")
        self.netmask = params.get("netmask")


class AssociateEipAddressRequest(AbstractModel):
    def __init__(self):
        self.eipId = None
        self.instanceId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.instanceId = params.get("instanceId")


class AssociateEipAddressResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnAssociateEipAddressRequest(AbstractModel):
    def __init__(self):
        self.eipId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")


class UnAssociateEipAddressResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeEipAvailableResourcesRequest(AbstractModel):
    def __init__(self):
        self.eipChargeType = None
        self.zoneId = None

    def _deserialize(self, params):
        self.eipChargeType = params.get("eipChargeType")
        self.zoneId = params.get("zoneId")


class DescribeEipAvailableResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.eipResources = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("eipResources") is not None:
            self.eipResources = []
            for item in params.get("eipResources"):
                obj = EipAvailable(item)
                self.eipResources.append(obj)


class EipAvailable(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.status = None
        self.netmask = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.status = params.get("status")
        self.netmask = params.get("netmask")


class TerminateEipAddressRequest(AbstractModel):
    def __init__(self):
        self.eipId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")


class TerminateEipAddressResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewEipAddressRequest(AbstractModel):
    def __init__(self):
        self.eipId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")


class RenewEipAddressResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ReleaseEipAddressesRequest(AbstractModel):
    def __init__(self):
        self.eipIds = None

    def _deserialize(self, params):
        self.eipIds = params.get("eipIds")


class ReleaseEipAddressesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeVpcAvailableRegionsRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.vpcRegionId = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.vpcRegionId = params.get("vpcRegionId")


class DescribeVpcAvailableRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.vpcRegionSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("vpcRegionSet") is not None:
            self.vpcRegionSet = []
            for item in params.get("vpcRegionSet"):
                obj = VpcRegionInfo(item)
                self.vpcRegionSet.append(obj)


class VpcRegionInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.vpcRegionId = None
        self.vpcRegionName = None
        self.zoneIds = None

    def _deserialize(self, params):
        self.vpcRegionId = params.get("vpcRegionId")
        self.vpcRegionName = params.get("vpcRegionName")
        self.zoneIds = params.get("zoneIds")


class CreateVpcRequest(AbstractModel):
    def __init__(self):
        self.vpcRegionId = None
        self.cidrBlock = None
        self.vpcName = None
        self.resourceGroupId = None
        self.tags = None

    def _deserialize(self, params):
        self.vpcRegionId = params.get("vpcRegionId")
        self.cidrBlock = params.get("cidrBlock")
        self.vpcName = params.get("vpcName")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateVpcResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.vpcId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.vpcId = params.get("vpcId")


class DescribeVpcsRequest(AbstractModel):
    def __init__(self):
        self.vpcIds = None
        self.vpcName = None
        self.cidrBlock = None
        self.vpcStatus = None
        self.vpcRegionId = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.vpcIds = params.get("vpcIds")
        self.vpcName = params.get("vpcName")
        self.cidrBlock = params.get("cidrBlock")
        self.vpcStatus = params.get("vpcStatus")
        self.vpcRegionId = params.get("vpcRegionId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeVpcsResponse(AbstractModel):
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
                obj = VpcInfo(item)
                self.dataSet.append(obj)


class VpcInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.vpcId = None
        self.vpcRegionId = None
        self.vpcRegionName = None
        self.vpcName = None
        self.cidrBlock = None
        self.createTime = None
        self.vpcStatus = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.tags = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.vpcRegionId = params.get("vpcRegionId")
        self.vpcRegionName = params.get("vpcRegionName")
        self.vpcName = params.get("vpcName")
        self.cidrBlock = params.get("cidrBlock")
        self.createTime = params.get("createTime")
        self.vpcStatus = params.get("vpcStatus")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class ModifyVpcsAttributeRequest(AbstractModel):
    def __init__(self):
        self.vpcName = None
        self.vpcIds = None

    def _deserialize(self, params):
        self.vpcName = params.get("vpcName")
        self.vpcIds = params.get("vpcIds")


class ModifyVpcsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteVpcRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")


class DeleteVpcResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeLoadBalancerZonesRequest(AbstractModel):
    def __init__(self):
        self.chargeType = None

    def _deserialize(self, params):
        self.chargeType = params.get("chargeType")


class DescribeLoadBalancerZonesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.zoneIdSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.zoneIdSet = params.get("zoneIdSet")


class DescribeLoadBalancerSpecsRequest(AbstractModel):
    def __init__(self):
        self.chargeType = None
        self.zoneId = None

    def _deserialize(self, params):
        self.chargeType = params.get("chargeType")
        self.zoneId = params.get("zoneId")


class DescribeLoadBalancerSpecsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.specSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("specSet") is not None:
            self.specSet = []
            for item in params.get("specSet"):
                obj = LoadBalancerSpec(item)
                self.specSet.append(obj)


class LoadBalancerSpec(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.specName = None
        self.maxConnection = None
        self.cps = None
        self.qps = None

    def _deserialize(self, params):
        self.specName = params.get("specName")
        self.maxConnection = params.get("maxConnection")
        self.cps = params.get("cps")
        self.qps = params.get("qps")


class CreateLoadBalancerRequest(AbstractModel):
    def __init__(self):
        self.clientToken = None
        self.zoneId = None
        self.loadBalancerName = None
        self.chargeType = None
        self.instanceChargePrepaid = None
        self.bandwidth = None
        self.ipType = None
        self.vipCount = None
        self.subnetId = None
        self.cidrBlockId = None
        self.masterIp = None
        self.backupIp = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.clientToken = params.get("clientToken")
        self.zoneId = params.get("zoneId")
        self.loadBalancerName = params.get("loadBalancerName")
        self.chargeType = params.get("chargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.bandwidth = params.get("bandwidth")
        self.ipType = params.get("ipType")
        self.vipCount = params.get("vipCount")
        self.subnetId = params.get("subnetId")
        self.cidrBlockId = params.get("cidrBlockId")
        self.masterIp = params.get("masterIp")
        self.backupIp = params.get("backupIp")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateLoadBalancerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.loadBalancerId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.loadBalancerId = params.get("loadBalancerId")


class DescribeLoadBalancersRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerIds = None
        self.zoneId = None
        self.loadBalancerName = None
        self.pageNum = None
        self.pageSize = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.loadBalancerIds = params.get("loadBalancerIds")
        self.zoneId = params.get("zoneId")
        self.loadBalancerName = params.get("loadBalancerName")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.resourceGroupId = params.get("resourceGroupId")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeLoadBalancersResponse(AbstractModel):
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
                obj = LoadBalancerInfo(item)
                self.dataSet.append(obj)


class LoadBalancerInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.loadBalancerId = None
        self.zoneId = None
        self.loadBalancerName = None
        self.specName = None
        self.vipList = None
        self.chargeType = None
        self.period = None
        self.createTime = None
        self.expiredTime = None
        self.status = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.masterIp = None
        self.backupIp = None
        self.ipType = None
        self.bandwidth = None
        self.isWorking = None
        self.listenerList = None
        self.backendList = None
        self.tags = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.zoneId = params.get("zoneId")
        self.loadBalancerName = params.get("loadBalancerName")
        self.specName = params.get("specName")
        if params.get("vipList") is not None:
            self.vipList = []
            for item in params.get("vipList"):
                obj = LoadBalancerIp(item)
                self.vipList.append(obj)
        self.chargeType = params.get("chargeType")
        self.period = params.get("period")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.status = params.get("status")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.masterIp = params.get("masterIp")
        self.backupIp = params.get("backupIp")
        self.ipType = params.get("ipType")
        self.bandwidth = params.get("bandwidth")
        self.isWorking = params.get("isWorking")
        if params.get("listenerList") is not None:
            self.listenerList = []
            for item in params.get("listenerList"):
                obj = ListenerInfo(item)
                self.listenerList.append(obj)
        if params.get("backendList") is not None:
            self.backendList = []
            for item in params.get("backendList"):
                obj = BackendInfo(item)
                self.backendList.append(obj)
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class LoadBalancerIp(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.vipId = None
        self.ipAddress = None
        self.type = None
        self.status = None

    def _deserialize(self, params):
        self.vipId = params.get("vipId")
        self.ipAddress = params.get("ipAddress")
        self.type = params.get("type")
        self.status = params.get("status")


class ListenerInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.loadBalancerId = None
        self.listenerId = None
        self.listenerName = None
        self.status = None
        self.port = None
        self.protocol = None
        self.backendProtocol = None
        self.scheduler = None
        self.kind = None
        self.healthCheck = None
        self.notify = None
        self.createTime = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")
        self.listenerName = params.get("listenerName")
        self.status = params.get("status")
        self.port = params.get("port")
        self.protocol = params.get("protocol")
        self.backendProtocol = params.get("backendProtocol")
        self.scheduler = params.get("scheduler")
        self.kind = params.get("kind")
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))
        if params.get("notify") is not None:
            self.notify = Notify(params.get("notify"))
        self.createTime = params.get("createTime")


class HealthCheck(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.checkEnabled = None
        self.checkType = None
        self.checkConnectTimeout = None
        self.checkRetry = None
        self.checkDelayBeforeRetry = None
        self.checkIntervalTime = None
        self.checkPort = None
        self.httpVersion = None
        self.httpCheckPath = None
        self.httpCheckDigest = None
        self.httpCode = None
        self.miscCheckPath = None
        self.miscTimeout = None

    def _deserialize(self, params):
        self.checkEnabled = params.get("checkEnabled")
        self.checkType = params.get("checkType")
        self.checkConnectTimeout = params.get("checkConnectTimeout")
        self.checkRetry = params.get("checkRetry")
        self.checkDelayBeforeRetry = params.get("checkDelayBeforeRetry")
        self.checkIntervalTime = params.get("checkIntervalTime")
        self.checkPort = params.get("checkPort")
        self.httpVersion = params.get("httpVersion")
        self.httpCheckPath = params.get("httpCheckPath")
        self.httpCheckDigest = params.get("httpCheckDigest")
        self.httpCode = params.get("httpCode")
        self.miscCheckPath = params.get("miscCheckPath")
        self.miscTimeout = params.get("miscTimeout")


class Notify(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.enable = None
        self.apiAddress = None

    def _deserialize(self, params):
        self.enable = params.get("enable")
        self.apiAddress = params.get("apiAddress")


class BackendInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.listenerId = None
        self.backendId = None
        self.backendName = None
        self.status = None
        self.port = None
        self.weight = None
        self.instanceId = None
        self.instanceName = None
        self.createTime = None

    def _deserialize(self, params):
        self.listenerId = params.get("listenerId")
        self.backendId = params.get("backendId")
        self.backendName = params.get("backendName")
        self.status = params.get("status")
        self.port = params.get("port")
        self.weight = params.get("weight")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.createTime = params.get("createTime")


class ModifyLoadBalancersNameRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerName = None
        self.loadBalancerIds = None

    def _deserialize(self, params):
        self.loadBalancerName = params.get("loadBalancerName")
        self.loadBalancerIds = params.get("loadBalancerIds")


class ModifyLoadBalancersNameResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class TerminateLoadBalancerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")


class TerminateLoadBalancerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RestoreLoadBalancerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")


class RestoreLoadBalancerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")


class ReleaseLoadBalancerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")


class ReleaseLoadBalancerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CreateListenerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerName = None
        self.portList = None
        self.clientToken = None
        self.protocol = None
        self.backendProtocol = None
        self.scheduler = None
        self.kind = None
        self.healthCheck = None
        self.notify = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerName = params.get("listenerName")
        self.portList = params.get("portList")
        self.clientToken = params.get("clientToken")
        self.protocol = params.get("protocol")
        self.backendProtocol = params.get("backendProtocol")
        self.scheduler = params.get("scheduler")
        self.kind = params.get("kind")
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))
        if params.get("notify") is not None:
            self.notify = Notify(params.get("notify"))


class CreateListenerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.listenerId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.listenerId = params.get("listenerId")


class DescribeListenersRequest(AbstractModel):
    def __init__(self):
        self.listenerIds = None
        self.loadBalancerIds = None
        self.listenerName = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.listenerIds = params.get("listenerIds")
        self.loadBalancerIds = params.get("loadBalancerIds")
        self.listenerName = params.get("listenerName")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


class DescribeListenersResponse(AbstractModel):
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
                obj = ListenerInfo(item)
                self.dataSet.append(obj)


class ModifyListenerAttributeRequest(AbstractModel):
    def __init__(self):
        self.listenerId = None
        self.listenerName = None
        self.protocol = None
        self.backendProtocol = None
        self.scheduler = None
        self.kind = None
        self.healthCheck = None
        self.notify = None

    def _deserialize(self, params):
        self.listenerId = params.get("listenerId")
        self.listenerName = params.get("listenerName")
        self.protocol = params.get("protocol")
        self.backendProtocol = params.get("backendProtocol")
        self.scheduler = params.get("scheduler")
        self.kind = params.get("kind")
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))
        if params.get("notify") is not None:
            self.notify = Notify(params.get("notify"))


class ModifyListenerAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteListenerRequest(AbstractModel):
    def __init__(self):
        self.listenerId = None

    def _deserialize(self, params):
        self.listenerId = params.get("listenerId")


class DeleteListenerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CreateLoadBalancerVIPsRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.count = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.count = params.get("count")


class CreateLoadBalancerVIPsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.vipIdSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.vipIdSet = params.get("vipIdSet")


class DeleteLoadBalancerVIPRequest(AbstractModel):
    def __init__(self):
        self.vipId = None

    def _deserialize(self, params):
        self.vipId = params.get("vipId")


class DeleteLoadBalancerVIPResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeBackendsRequest(AbstractModel):
    def __init__(self):
        self.listenerId = None
        self.backendIds = None
        self.backendName = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.listenerId = params.get("listenerId")
        self.backendIds = params.get("backendIds")
        self.backendName = params.get("backendName")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


class DescribeBackendsResponse(AbstractModel):
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
                obj = BackendInfo(item)
                self.dataSet.append(obj)


class RegisterBackendRequest(AbstractModel):
    def __init__(self):
        self.listenerId = None
        self.backendName = None
        self.instanceId = None
        self.clientToken = None
        self.portList = None
        self.weight = None

    def _deserialize(self, params):
        self.listenerId = params.get("listenerId")
        self.backendName = params.get("backendName")
        self.instanceId = params.get("instanceId")
        self.clientToken = params.get("clientToken")
        self.portList = params.get("portList")
        self.weight = params.get("weight")


class RegisterBackendResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.backendId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.backendId = params.get("backendId")


class DeregisterBackendRequest(AbstractModel):
    def __init__(self):
        self.backendId = None

    def _deserialize(self, params):
        self.backendId = params.get("backendId")


class DeregisterBackendResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeManagedInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.instanceName = None
        self.ip = None
        self.lanIp = None
        self.facName = None
        self.cityCode = None
        self.pageNum = None
        self.pageSize = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.instanceName = params.get("instanceName")
        self.ip = params.get("ip")
        self.lanIp = params.get("lanIp")
        self.facName = params.get("facName")
        self.cityCode = params.get("cityCode")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.resourceGroupId = params.get("resourceGroupId")


class DescribeManagedInstancesResponse(AbstractModel):
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
                obj = ManagedInstanceInfo(item)
                self.dataSet.append(obj)


class ManagedInstanceInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.instanceName = None
        self.facName = None
        self.ips = None
        self.lanIps = None
        self.createTime = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.facName = params.get("facName")
        self.ips = params.get("ips")
        self.lanIps = params.get("lanIps")
        self.createTime = params.get("createTime")


class DescribeManagedInstanceTrafficRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeManagedInstanceTrafficResponse(AbstractModel):
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
                obj = InstanceTrafficData(item)
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


