#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeDisksRequest(AbstractModel):
    def __init__(self):
        self.diskIds = None
        self.diskName = None
        self.diskStatus = None
        self.diskType = None
        self.diskCategory = None
        self.instanceId = None
        self.zoneId = None
        self.pageNum = None
        self.pageSize = None
        self.regionId = None
        self.snapshotAbility = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")
        self.diskName = params.get("diskName")
        self.diskStatus = params.get("diskStatus")
        self.diskType = params.get("diskType")
        self.diskCategory = params.get("diskCategory")
        self.instanceId = params.get("instanceId")
        self.zoneId = params.get("zoneId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.regionId = params.get("regionId")
        self.snapshotAbility = params.get("snapshotAbility")
        self.resourceGroupId = params.get("resourceGroupId")
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


class DescribeDisksResponse(AbstractModel):
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
                obj = DiskInfo(item)
                self.dataSet.append(obj)


class DiskInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.diskId = None
        self.diskName = None
        self.regionId = None
        self.zoneId = None
        self.diskType = None
        self.portable = None
        self.diskCategory = None
        self.diskSize = None
        self.diskStatus = None
        self.instanceId = None
        self.instanceName = None
        self.createTime = None
        self.expiredTime = None
        self.period = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.serial = None
        self.snapshotAbility = None
        self.autoSnapshotPolicyId = None
        self.tags = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.diskName = params.get("diskName")
        self.regionId = params.get("regionId")
        self.zoneId = params.get("zoneId")
        self.diskType = params.get("diskType")
        self.portable = params.get("portable")
        self.diskCategory = params.get("diskCategory")
        self.diskSize = params.get("diskSize")
        self.diskStatus = params.get("diskStatus")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.period = params.get("period")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.serial = params.get("serial")
        self.snapshotAbility = params.get("snapshotAbility")
        self.autoSnapshotPolicyId = params.get("autoSnapshotPolicyId")
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


class DescribeDiskRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeDiskRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")


class InquiryPriceCreateDisksRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.diskSize = None
        self.diskAmount = None
        self.diskCategory = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.diskSize = params.get("diskSize")
        self.diskAmount = params.get("diskAmount")
        self.diskCategory = params.get("diskCategory")


class InquiryPriceCreateDisksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataDiskPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataDiskPrice") is not None:
            self.dataDiskPrice = PriceItem(params.get("dataDiskPrice"))


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


class CreateDisksRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.diskName = None
        self.diskSize = None
        self.diskAmount = None
        self.instanceId = None
        self.resourceGroupId = None
        self.diskCategory = None
        self.snapshotId = None
        self.marketingOptions = None
        self.tags = None
        self.instanceIds = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.diskName = params.get("diskName")
        self.diskSize = params.get("diskSize")
        self.diskAmount = params.get("diskAmount")
        self.instanceId = params.get("instanceId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.diskCategory = params.get("diskCategory")
        self.snapshotId = params.get("snapshotId")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))
        self.instanceIds = params.get("instanceIds")


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


class CreateDisksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.diskIds = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.diskIds = params.get("diskIds")
        self.orderNumber = params.get("orderNumber")


class AttachDisksRequest(AbstractModel):
    def __init__(self):
        self.diskIds = None
        self.instanceId = None

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")
        self.instanceId = params.get("instanceId")


class AttachDisksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DetachDisksRequest(AbstractModel):
    def __init__(self):
        self.diskIds = None
        self.instanceCheckFlag = None

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")
        self.instanceCheckFlag = params.get("instanceCheckFlag")


class DetachDisksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.failedDiskIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.failedDiskIds = params.get("failedDiskIds")


class ModifyDisksAttributesRequest(AbstractModel):
    def __init__(self):
        self.diskIds = None
        self.diskName = None

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")
        self.diskName = params.get("diskName")


class ModifyDisksAttributesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ResizeDiskRequest(AbstractModel):
    def __init__(self):
        self.diskId = None
        self.diskSize = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.diskSize = params.get("diskSize")


class ResizeDiskResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ReleaseDiskRequest(AbstractModel):
    def __init__(self):
        self.diskId = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")


class ReleaseDiskResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewDiskRequest(AbstractModel):
    def __init__(self):
        self.diskId = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")


class RenewDiskResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyDisksResourceGroupRequest(AbstractModel):
    def __init__(self):
        self.diskIds = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")
        self.resourceGroupId = params.get("resourceGroupId")


class ModifyDisksResourceGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeDiskCategoryRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.diskCategory = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.diskCategory = params.get("diskCategory")


class DescribeDiskCategoryResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.categoryZoneSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("categoryZoneSet") is not None:
            self.categoryZoneSet = []
            for item in params.get("categoryZoneSet"):
                obj = DescribeDiskCategoryItem(item)
                self.categoryZoneSet.append(obj)


class DescribeDiskCategoryItem(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.categorySet = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.categorySet = params.get("categorySet")


class DescribeDiskMonitorDataRequest(AbstractModel):
    def __init__(self):
        self.diskId = None
        self.metricType = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.metricType = params.get("metricType")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeDiskMonitorDataResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.maxValue = None
        self.minValue = None
        self.avgValue = None
        self.metrics = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.maxValue = params.get("maxValue")
        self.minValue = params.get("minValue")
        self.avgValue = params.get("avgValue")
        if params.get("metrics") is not None:
            self.metrics = []
            for item in params.get("metrics"):
                obj = MetricValue(item)
                self.metrics.append(obj)


class MetricValue(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.time = None
        self.value = None

    def _deserialize(self, params):
        self.time = params.get("time")
        self.value = params.get("value")


class CreateVpcRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.cidrBlock = None
        self.mtu = None
        self.enablePriIpv6 = None
        self.resourceGroupId = None
        self.tags = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.mtu = params.get("mtu")
        self.enablePriIpv6 = params.get("enablePriIpv6")
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


class ModifyVpcsAttributeRequest(AbstractModel):
    def __init__(self):
        self.vpcIds = None
        self.name = None

    def _deserialize(self, params):
        self.vpcIds = params.get("vpcIds")
        self.name = params.get("name")


class ModifyVpcsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeSubnetRegionsRequest(AbstractModel):
    def __init__(self):
        self.regionIds = None

    def _deserialize(self, params):
        self.regionIds = params.get("regionIds")


class DescribeSubnetRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regionSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("regionSet") is not None:
            self.regionSet = []
            for item in params.get("regionSet"):
                obj = RegionInfo(item)
                self.regionSet.append(obj)


class RegionInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.regionId = None
        self.regionName = None
        self.regionTitle = None
        self.enablePubIpv6 = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.regionName = params.get("regionName")
        self.regionTitle = params.get("regionTitle")
        self.enablePubIpv6 = params.get("enablePubIpv6")


class CreateSubnetRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None
        self.name = None
        self.regionId = None
        self.stackType = None
        self.cidrBlock = None
        self.ipv6Type = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.name = params.get("name")
        self.regionId = params.get("regionId")
        self.stackType = params.get("stackType")
        self.cidrBlock = params.get("cidrBlock")
        self.ipv6Type = params.get("ipv6Type")


class CreateSubnetResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.subnetId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.subnetId = params.get("subnetId")


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


class ModifySubnetAttributeRequest(AbstractModel):
    def __init__(self):
        self.subnetId = None
        self.subnetName = None
        self.cidrBlock = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.subnetName = params.get("subnetName")
        self.cidrBlock = params.get("cidrBlock")


class ModifySubnetAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifySubnetStackTypeRequest(AbstractModel):
    def __init__(self):
        self.subnetId = None
        self.stackType = None
        self.ipv6Type = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.stackType = params.get("stackType")
        self.ipv6Type = params.get("ipv6Type")


class ModifySubnetStackTypeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.ipv6CidrBlock = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.ipv6CidrBlock = params.get("ipv6CidrBlock")


class DescribeVpcsRequest(AbstractModel):
    def __init__(self):
        self.vpcIds = None
        self.name = None
        self.cidrBlock = None
        self.pageSize = None
        self.pageNum = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.vpcIds = params.get("vpcIds")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.resourceGroupId = params.get("resourceGroupId")
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
        self.name = None
        self.cidrBlock = None
        self.ipv6CidrBlock = None
        self.mtu = None
        self.isDefault = None
        self.createTime = None
        self.usageIpv4Count = None
        self.usageIpv6Count = None
        self.securityGroupId = None
        self.dnsZoneIds = None
        self.resourceGroup = None
        self.tags = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.ipv6CidrBlock = params.get("ipv6CidrBlock")
        self.mtu = params.get("mtu")
        self.isDefault = params.get("isDefault")
        self.createTime = params.get("createTime")
        self.usageIpv4Count = params.get("usageIpv4Count")
        self.usageIpv6Count = params.get("usageIpv6Count")
        self.securityGroupId = params.get("securityGroupId")
        self.dnsZoneIds = params.get("dnsZoneIds")
        if params.get("resourceGroup") is not None:
            self.resourceGroup = ResourceGroupInfo(params.get("resourceGroup"))
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class ResourceGroupInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceGroupId = None
        self.resourceGroupName = None

    def _deserialize(self, params):
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")


class ModifyVpcAttributeRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None
        self.vpcName = None
        self.cidrBlock = None
        self.enableIPv6 = None
        self.securityGroupId = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.vpcName = params.get("vpcName")
        self.cidrBlock = params.get("cidrBlock")
        self.enableIPv6 = params.get("enableIPv6")
        self.securityGroupId = params.get("securityGroupId")


class ModifyVpcAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeSubnetsRequest(AbstractModel):
    def __init__(self):
        self.subnetIds = None
        self.name = None
        self.cidrBlock = None
        self.regionId = None
        self.pageSize = None
        self.pageNum = None
        self.vpcIds = None

    def _deserialize(self, params):
        self.subnetIds = params.get("subnetIds")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.regionId = params.get("regionId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.vpcIds = params.get("vpcIds")


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
        self.regionId = None
        self.name = None
        self.cidrBlock = None
        self.gatewayIpAddress = None
        self.ipv6CidrBlock = None
        self.ipv6GatewayIpAddress = None
        self.stackType = None
        self.ipv6Type = None
        self.vpcId = None
        self.vpcName = None
        self.usageIpv4Count = None
        self.usageIpv6Count = None
        self.createTime = None
        self.isDefault = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.gatewayIpAddress = params.get("gatewayIpAddress")
        self.ipv6CidrBlock = params.get("ipv6CidrBlock")
        self.ipv6GatewayIpAddress = params.get("ipv6GatewayIpAddress")
        self.stackType = params.get("stackType")
        self.ipv6Type = params.get("ipv6Type")
        self.vpcId = params.get("vpcId")
        self.vpcName = params.get("vpcName")
        self.usageIpv4Count = params.get("usageIpv4Count")
        self.usageIpv6Count = params.get("usageIpv6Count")
        self.createTime = params.get("createTime")
        self.isDefault = params.get("isDefault")


class ModifySubnetsAttributeRequest(AbstractModel):
    def __init__(self):
        self.subnetIds = None
        self.name = None

    def _deserialize(self, params):
        self.subnetIds = params.get("subnetIds")
        self.name = params.get("name")


class ModifySubnetsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CreateSnapshotRequest(AbstractModel):
    def __init__(self):
        self.diskId = None
        self.snapshotName = None
        self.retentionTime = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.snapshotName = params.get("snapshotName")
        self.retentionTime = params.get("retentionTime")


class CreateSnapshotResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.snapshotId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.snapshotId = params.get("snapshotId")


class ModifySnapshotsAttributeRequest(AbstractModel):
    def __init__(self):
        self.snapshotIds = None
        self.snapshotName = None
        self.retentionTime = None
        self.isPermanent = None

    def _deserialize(self, params):
        self.snapshotIds = params.get("snapshotIds")
        self.snapshotName = params.get("snapshotName")
        self.retentionTime = params.get("retentionTime")
        self.isPermanent = params.get("isPermanent")


class ModifySnapshotsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteSnapshotsRequest(AbstractModel):
    def __init__(self):
        self.snapshotIds = None

    def _deserialize(self, params):
        self.snapshotIds = params.get("snapshotIds")


class DeleteSnapshotsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.snapshotIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.snapshotIds = params.get("snapshotIds")


class DescribeSnapshotsRequest(AbstractModel):
    def __init__(self):
        self.snapshotIds = None
        self.zoneId = None
        self.status = None
        self.diskIds = None
        self.diskType = None
        self.snapshotType = None
        self.snapshotName = None
        self.pageSize = None
        self.pageNum = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.snapshotIds = params.get("snapshotIds")
        self.zoneId = params.get("zoneId")
        self.status = params.get("status")
        self.diskIds = params.get("diskIds")
        self.diskType = params.get("diskType")
        self.snapshotType = params.get("snapshotType")
        self.snapshotName = params.get("snapshotName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.resourceGroupId = params.get("resourceGroupId")


class DescribeSnapshotsResponse(AbstractModel):
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
                obj = SnapshotInfo(item)
                self.dataSet.append(obj)


class SnapshotInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.snapshotId = None
        self.snapshotName = None
        self.zoneId = None
        self.status = None
        self.snapshotType = None
        self.retentionTime = None
        self.diskId = None
        self.createTime = None
        self.diskAbility = None
        self.resourceGroup = None

    def _deserialize(self, params):
        self.snapshotId = params.get("snapshotId")
        self.snapshotName = params.get("snapshotName")
        self.zoneId = params.get("zoneId")
        self.status = params.get("status")
        self.snapshotType = params.get("snapshotType")
        self.retentionTime = params.get("retentionTime")
        self.diskId = params.get("diskId")
        self.createTime = params.get("createTime")
        self.diskAbility = params.get("diskAbility")
        if params.get("resourceGroup") is not None:
            self.resourceGroup = ResourceGroupInfo(params.get("resourceGroup"))


class ApplySnapshotRequest(AbstractModel):
    def __init__(self):
        self.snapshotId = None
        self.diskId = None

    def _deserialize(self, params):
        self.snapshotId = params.get("snapshotId")
        self.diskId = params.get("diskId")


class ApplySnapshotResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.autoSnapshotPolicyName = None
        self.repeatWeekDays = None
        self.hours = None
        self.retentionDays = None
        self.resourceGroupId = None
        self.tags = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.autoSnapshotPolicyName = params.get("autoSnapshotPolicyName")
        self.repeatWeekDays = params.get("repeatWeekDays")
        self.hours = params.get("hours")
        self.retentionDays = params.get("retentionDays")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateAutoSnapshotPolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.autoSnapshotPolicyId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.autoSnapshotPolicyId = params.get("autoSnapshotPolicyId")


class ApplyAutoSnapshotPolicyRequest(AbstractModel):
    def __init__(self):
        self.autoSnapshotPolicyId = None
        self.diskIds = None

    def _deserialize(self, params):
        self.autoSnapshotPolicyId = params.get("autoSnapshotPolicyId")
        self.diskIds = params.get("diskIds")


class ApplyAutoSnapshotPolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CancelAutoSnapshotPolicyRequest(AbstractModel):
    def __init__(self):
        self.autoSnapshotPolicyId = None
        self.diskIds = None

    def _deserialize(self, params):
        self.autoSnapshotPolicyId = params.get("autoSnapshotPolicyId")
        self.diskIds = params.get("diskIds")


class CancelAutoSnapshotPolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    def __init__(self):
        self.autoSnapshotPolicyIds = None
        self.zoneIds = None
        self.autoSnapshotPolicyName = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.autoSnapshotPolicyIds = params.get("autoSnapshotPolicyIds")
        self.zoneIds = params.get("zoneIds")
        self.autoSnapshotPolicyName = params.get("autoSnapshotPolicyName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeAutoSnapshotPoliciesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataSet = None
        self.totalCount = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = AutoSnapshotPolicy(item)
                self.dataSet.append(obj)
        self.totalCount = params.get("totalCount")


class AutoSnapshotPolicy(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.autoSnapshotPolicyId = None
        self.zoneId = None
        self.autoSnapshotPolicyName = None
        self.repeatWeekDays = None
        self.hours = None
        self.retentionDays = None
        self.diskNum = None
        self.createTime = None
        self.resourceGroup = None
        self.diskIdSet = None
        self.tags = None

    def _deserialize(self, params):
        self.autoSnapshotPolicyId = params.get("autoSnapshotPolicyId")
        self.zoneId = params.get("zoneId")
        self.autoSnapshotPolicyName = params.get("autoSnapshotPolicyName")
        self.repeatWeekDays = params.get("repeatWeekDays")
        self.hours = params.get("hours")
        self.retentionDays = params.get("retentionDays")
        self.diskNum = params.get("diskNum")
        self.createTime = params.get("createTime")
        if params.get("resourceGroup") is not None:
            self.resourceGroup = ResourceGroupInfo(params.get("resourceGroup"))
        self.diskIdSet = params.get("diskIdSet")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class ModifyAutoSnapshotPolicyRequest(AbstractModel):
    def __init__(self):
        self.autoSnapshotPolicyId = None
        self.autoSnapshotPolicyName = None
        self.repeatWeekDays = None
        self.hours = None
        self.retentionDays = None

    def _deserialize(self, params):
        self.autoSnapshotPolicyId = params.get("autoSnapshotPolicyId")
        self.autoSnapshotPolicyName = params.get("autoSnapshotPolicyName")
        self.repeatWeekDays = params.get("repeatWeekDays")
        self.hours = params.get("hours")
        self.retentionDays = params.get("retentionDays")


class ModifyAutoSnapshotPolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteAutoSnapshotPoliciesRequest(AbstractModel):
    def __init__(self):
        self.autoSnapshotPolicyIds = None

    def _deserialize(self, params):
        self.autoSnapshotPolicyIds = params.get("autoSnapshotPolicyIds")


class DeleteAutoSnapshotPoliciesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeNetworkInterfaceRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeNetworkInterfaceRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")


class DescribeNetworkInterfacesRequest(AbstractModel):
    def __init__(self):
        self.nicIds = None
        self.name = None
        self.regionId = None
        self.vpcId = None
        self.subnetId = None
        self.instanceId = None
        self.status = None
        self.pageSize = None
        self.pageNum = None
        self.nicType = None
        self.resourceGroupId = None
        self.securityGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.nicIds = params.get("nicIds")
        self.name = params.get("name")
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.subnetId = params.get("subnetId")
        self.instanceId = params.get("instanceId")
        self.status = params.get("status")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.nicType = params.get("nicType")
        self.resourceGroupId = params.get("resourceGroupId")
        self.securityGroupId = params.get("securityGroupId")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeNetworkInterfacesResponse(AbstractModel):
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
                obj = NicInfo(item)
                self.dataSet.append(obj)


class NicInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.nicId = None
        self.name = None
        self.status = None
        self.nicType = None
        self.regionId = None
        self.nicSubnetType = None
        self.publicIpList = None
        self.privateIpList = None
        self.primaryIpv4 = None
        self.primaryIpv6 = None
        self.ipv6Cidr = None
        self.secondaryIpv4s = None
        self.macAddress = None
        self.instanceId = None
        self.vpcId = None
        self.subnetId = None
        self.createTime = None
        self.updateTime = None
        self.resourceGroup = None
        self.securityGroupId = None
        self.tags = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.name = params.get("name")
        self.status = params.get("status")
        self.nicType = params.get("nicType")
        self.regionId = params.get("regionId")
        self.nicSubnetType = params.get("nicSubnetType")
        self.publicIpList = params.get("publicIpList")
        self.privateIpList = params.get("privateIpList")
        self.primaryIpv4 = params.get("primaryIpv4")
        self.primaryIpv6 = params.get("primaryIpv6")
        self.ipv6Cidr = params.get("ipv6Cidr")
        self.secondaryIpv4s = params.get("secondaryIpv4s")
        self.macAddress = params.get("macAddress")
        self.instanceId = params.get("instanceId")
        self.vpcId = params.get("vpcId")
        self.subnetId = params.get("subnetId")
        self.createTime = params.get("createTime")
        self.updateTime = params.get("updateTime")
        if params.get("resourceGroup") is not None:
            self.resourceGroup = ResourceGroupInfo(params.get("resourceGroup"))
        self.securityGroupId = params.get("securityGroupId")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.name = None
        self.securityGroupId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.name = params.get("name")
        self.securityGroupId = params.get("securityGroupId")


class ModifyNetworkInterfaceAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyNetworkInterfacesAttributeRequest(AbstractModel):
    def __init__(self):
        self.nicIds = None
        self.name = None

    def _deserialize(self, params):
        self.nicIds = params.get("nicIds")
        self.name = params.get("name")


class ModifyNetworkInterfacesAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.subnetId = None
        self.nicStackType = None
        self.resourceGroupId = None
        self.securityGroupId = None
        self.internetChargeType = None
        self.bandwidth = None
        self.packageSize = None
        self.clusterId = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.subnetId = params.get("subnetId")
        self.nicStackType = params.get("nicStackType")
        self.resourceGroupId = params.get("resourceGroupId")
        self.securityGroupId = params.get("securityGroupId")
        self.internetChargeType = params.get("internetChargeType")
        self.bandwidth = params.get("bandwidth")
        self.packageSize = params.get("packageSize")
        self.clusterId = params.get("clusterId")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateNetworkInterfaceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.nicId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.nicId = params.get("nicId")


class DeleteNetworkInterfaceRequest(AbstractModel):
    def __init__(self):
        self.nicId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")


class DeleteNetworkInterfaceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AttachNetworkInterfaceRequest(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.instanceId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.instanceId = params.get("instanceId")


class AttachNetworkInterfaceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    def __init__(self):
        self.nicId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")


class DetachNetworkInterfaceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AssignNetworkInterfaceIpv4Request(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.ipAddress = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.ipAddress = params.get("ipAddress")


class AssignNetworkInterfaceIpv4Response(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class BatchAssignNetworkInterfaceIpv4Request(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.ipAddresses = None
        self.ipAddressCount = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.ipAddresses = params.get("ipAddresses")
        self.ipAddressCount = params.get("ipAddressCount")


class BatchAssignNetworkInterfaceIpv4Response(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.ipAddresses = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.ipAddresses = params.get("ipAddresses")


class UnassignNetworkInterfaceIpv4Request(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.ipAddress = None
        self.ipAddresses = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.ipAddress = params.get("ipAddress")
        self.ipAddresses = params.get("ipAddresses")


class UnassignNetworkInterfaceIpv4Response(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeNetworkInterfacePublicIPv6Request(AbstractModel):
    def __init__(self):
        self.nicId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")


class DescribeNetworkInterfacePublicIPv6Response(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.address = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("address") is not None:
            self.address = PublicIpv6CidrAddress(params.get("address"))


class PublicIpv6CidrAddress(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.ipv6CidrId = None
        self.ipv6Cidr = None
        self.primaryIpv6Address = None
        self.internetChargeType = None
        self.bandwidth = None
        self.trafficPackageSize = None
        self.bandwidthCluster = None

    def _deserialize(self, params):
        self.ipv6CidrId = params.get("ipv6CidrId")
        self.ipv6Cidr = params.get("ipv6Cidr")
        self.primaryIpv6Address = params.get("primaryIpv6Address")
        self.internetChargeType = params.get("internetChargeType")
        self.bandwidth = params.get("bandwidth")
        self.trafficPackageSize = params.get("trafficPackageSize")
        if params.get("bandwidthCluster") is not None:
            self.bandwidthCluster = BandwidthClusterInfo(params.get("bandwidthCluster"))


class BandwidthClusterInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.bandwidthClusterId = None
        self.bandwidthClusterName = None

    def _deserialize(self, params):
        self.bandwidthClusterId = params.get("bandwidthClusterId")
        self.bandwidthClusterName = params.get("bandwidthClusterName")


class InquiryPricePublicIpv6Request(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.packageSize = None
        self.bandwidth = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.packageSize = params.get("packageSize")
        self.bandwidth = params.get("bandwidth")


class InquiryPricePublicIpv6Response(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.bandwidthPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = PriceItem(params.get("bandwidthPrice"))


class AssignNetworkInterfaceIpv6Request(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.internetChargeType = None
        self.bandwidth = None
        self.packageSize = None
        self.clusterId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.internetChargeType = params.get("internetChargeType")
        self.bandwidth = params.get("bandwidth")
        self.packageSize = params.get("packageSize")
        self.clusterId = params.get("clusterId")


class AssignNetworkInterfaceIpv6Response(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeImagesRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.imageIds = None
        self.imageName = None
        self.category = None
        self.imageType = None
        self.imageSource = None
        self.osType = None
        self.imageStatus = None
        self.pageNum = None
        self.pageSize = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.imageIds = params.get("imageIds")
        self.imageName = params.get("imageName")
        self.category = params.get("category")
        self.imageType = params.get("imageType")
        self.imageSource = params.get("imageSource")
        self.osType = params.get("osType")
        self.imageStatus = params.get("imageStatus")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeImagesResponse(AbstractModel):
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
                obj = Image(item)
                self.dataSet.append(obj)


class Image(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.imageId = None
        self.imageName = None
        self.imageType = None
        self.imageSource = None
        self.imageSize = None
        self.imageDescription = None
        self.imageVersion = None
        self.imageStatus = None
        self.nicNetworkType = None
        self.category = None
        self.osType = None
        self.tags = None

    def _deserialize(self, params):
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")
        self.imageType = params.get("imageType")
        self.imageSource = params.get("imageSource")
        self.imageSize = params.get("imageSize")
        self.imageDescription = params.get("imageDescription")
        self.imageVersion = params.get("imageVersion")
        self.imageStatus = params.get("imageStatus")
        self.nicNetworkType = params.get("nicNetworkType")
        self.category = params.get("category")
        self.osType = params.get("osType")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class CreateImageRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.imageName = None
        self.resourceGroupId = None
        self.tags = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.imageName = params.get("imageName")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateImageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.imageId = None
        self.imageName = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")


class ModifyImagesAttributesRequest(AbstractModel):
    def __init__(self):
        self.imageIds = None
        self.imageName = None

    def _deserialize(self, params):
        self.imageIds = params.get("imageIds")
        self.imageName = params.get("imageName")


class ModifyImagesAttributesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteImagesRequest(AbstractModel):
    def __init__(self):
        self.imageIds = None

    def _deserialize(self, params):
        self.imageIds = params.get("imageIds")


class DeleteImagesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.imageIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.imageIds = params.get("imageIds")


class CreatePolicyRequest(AbstractModel):
    def __init__(self):
        self.policyName = None
        self.resourceGroupId = None
        self.blackIpList = None
        self.whiteIpList = None
        self.ipBlackTimeout = None
        self.ports = None
        self.blockProtocol = None
        self.blockRegions = None
        self.finger = None
        self.reflectUdpPort = None
        self.trafficControl = None
        self.tags = None

    def _deserialize(self, params):
        self.policyName = params.get("policyName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.blackIpList = params.get("blackIpList")
        self.whiteIpList = params.get("whiteIpList")
        self.ipBlackTimeout = params.get("ipBlackTimeout")
        if params.get("ports") is not None:
            self.ports = []
            for item in params.get("ports"):
                obj = DdosPolicyPort(item)
                self.ports.append(obj)
        self.blockProtocol = params.get("blockProtocol")
        self.blockRegions = params.get("blockRegions")
        if params.get("finger") is not None:
            self.finger = []
            for item in params.get("finger"):
                obj = DdosFingerprintRule(item)
                self.finger.append(obj)
        if params.get("reflectUdpPort") is not None:
            self.reflectUdpPort = []
            for item in params.get("reflectUdpPort"):
                obj = DdosReflectUdpPort(item)
                self.reflectUdpPort.append(obj)
        if params.get("trafficControl") is not None:
            self.trafficControl = DdosTrafficControl(params.get("trafficControl"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class DdosPolicyPort(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.protocol = None
        self.srcPortStart = None
        self.srcPortEnd = None
        self.dstPortStart = None
        self.dstPortEnd = None
        self.action = None

    def _deserialize(self, params):
        self.protocol = params.get("protocol")
        self.srcPortStart = params.get("srcPortStart")
        self.srcPortEnd = params.get("srcPortEnd")
        self.dstPortStart = params.get("dstPortStart")
        self.dstPortEnd = params.get("dstPortEnd")
        self.action = params.get("action")


class DdosFingerprintRule(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.protocol = None
        self.srcPortStart = None
        self.srcPortEnd = None
        self.dstPortStart = None
        self.dstPortEnd = None
        self.minPktLength = None
        self.maxPktLength = None
        self.offset = None
        self.matchBytes = None
        self.action = None

    def _deserialize(self, params):
        self.protocol = params.get("protocol")
        self.srcPortStart = params.get("srcPortStart")
        self.srcPortEnd = params.get("srcPortEnd")
        self.dstPortStart = params.get("dstPortStart")
        self.dstPortEnd = params.get("dstPortEnd")
        self.minPktLength = params.get("minPktLength")
        self.maxPktLength = params.get("maxPktLength")
        self.offset = params.get("offset")
        self.matchBytes = params.get("matchBytes")
        self.action = params.get("action")


class DdosReflectUdpPort(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.port = None

    def _deserialize(self, params):
        self.port = params.get("port")


class DdosTrafficControl(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.bpsEnabled = None
        self.bps = None
        self.ppsEnabled = None
        self.pps = None
        self.synBPSEnabled = None
        self.synBPS = None
        self.synPPSEnabled = None
        self.synPPS = None

    def _deserialize(self, params):
        self.bpsEnabled = params.get("bpsEnabled")
        self.bps = params.get("bps")
        self.ppsEnabled = params.get("ppsEnabled")
        self.pps = params.get("pps")
        self.synBPSEnabled = params.get("synBPSEnabled")
        self.synBPS = params.get("synBPS")
        self.synPPSEnabled = params.get("synPPSEnabled")
        self.synPPS = params.get("synPPS")


class CreatePolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.policyId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.policyId = params.get("policyId")


class DeletePolicyRequest(AbstractModel):
    def __init__(self):
        self.policyId = None

    def _deserialize(self, params):
        self.policyId = params.get("policyId")


class DeletePolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyPolicyRequest(AbstractModel):
    def __init__(self):
        self.policyId = None
        self.policyName = None
        self.configType = None
        self.blackIpList = None
        self.whiteIpList = None
        self.ipBlackTimeout = None
        self.ports = None
        self.blockProtocol = None
        self.blockRegions = None
        self.finger = None
        self.reflectUdpPort = None
        self.trafficControl = None
        self.tags = None

    def _deserialize(self, params):
        self.policyId = params.get("policyId")
        self.policyName = params.get("policyName")
        self.configType = params.get("configType")
        self.blackIpList = params.get("blackIpList")
        self.whiteIpList = params.get("whiteIpList")
        self.ipBlackTimeout = params.get("ipBlackTimeout")
        if params.get("ports") is not None:
            self.ports = []
            for item in params.get("ports"):
                obj = DdosPolicyPort(item)
                self.ports.append(obj)
        self.blockProtocol = params.get("blockProtocol")
        self.blockRegions = params.get("blockRegions")
        if params.get("finger") is not None:
            self.finger = []
            for item in params.get("finger"):
                obj = DdosFingerprintRule(item)
                self.finger.append(obj)
        if params.get("reflectUdpPort") is not None:
            self.reflectUdpPort = []
            for item in params.get("reflectUdpPort"):
                obj = DdosReflectUdpPort(item)
                self.reflectUdpPort.append(obj)
        if params.get("trafficControl") is not None:
            self.trafficControl = DdosTrafficControl(params.get("trafficControl"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class ModifyPolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribePolicysRequest(AbstractModel):
    def __init__(self):
        self.policyIds = None
        self.policyName = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.policyIds = params.get("policyIds")
        self.policyName = params.get("policyName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribePolicysResponse(AbstractModel):
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
                obj = PolicyInfo(item)
                self.dataSet.append(obj)


class PolicyInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.policyId = None
        self.policyName = None
        self.createTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.tags = None

    def _deserialize(self, params):
        self.policyId = params.get("policyId")
        self.policyName = params.get("policyName")
        self.createTime = params.get("createTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class DescribePolicyDetailRequest(AbstractModel):
    def __init__(self):
        self.policyId = None

    def _deserialize(self, params):
        self.policyId = params.get("policyId")


class DescribePolicyDetailResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.policyId = None
        self.policyName = None
        self.attachmentIps = None
        self.createTime = None
        self.blackIps = None
        self.whiteIps = None
        self.blackIpListExpireAt = None
        self.blockProtocols = None
        self.ports = None
        self.blockRegions = None
        self.reflectUdpPort = None
        self.trafficControl = None
        self.fingerPrintRules = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.policyId = params.get("policyId")
        self.policyName = params.get("policyName")
        self.attachmentIps = params.get("attachmentIps")
        self.createTime = params.get("createTime")
        self.blackIps = params.get("blackIps")
        self.whiteIps = params.get("whiteIps")
        self.blackIpListExpireAt = params.get("blackIpListExpireAt")
        self.blockProtocols = params.get("blockProtocols")
        if params.get("ports") is not None:
            self.ports = []
            for item in params.get("ports"):
                obj = DdosPolicyPort(item)
                self.ports.append(obj)
        self.blockRegions = params.get("blockRegions")
        if params.get("reflectUdpPort") is not None:
            self.reflectUdpPort = []
            for item in params.get("reflectUdpPort"):
                obj = DdosReflectUdpPort(item)
                self.reflectUdpPort.append(obj)
        if params.get("trafficControl") is not None:
            self.trafficControl = DdosTrafficControl(params.get("trafficControl"))
        if params.get("fingerPrintRules") is not None:
            self.fingerPrintRules = []
            for item in params.get("fingerPrintRules"):
                obj = DdosFingerprintRule(item)
                self.fingerPrintRules.append(obj)


class AttachToPolicyRequest(AbstractModel):
    def __init__(self):
        self.policyId = None
        self.ipv4IdList = None

    def _deserialize(self, params):
        self.policyId = params.get("policyId")
        self.ipv4IdList = params.get("ipv4IdList")


class AttachToPolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DetachFromPolicyRequest(AbstractModel):
    def __init__(self):
        self.policyId = None
        self.ipv4IdList = None

    def _deserialize(self, params):
        self.policyId = params.get("policyId")
        self.ipv4IdList = params.get("ipv4IdList")


class DetachFromPolicyResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribePolicyRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribePolicyRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("regions") is not None:
            self.regions = []
            for item in params.get("regions"):
                obj = PolicyRegion(item)
                self.regions.append(obj)


class PolicyRegion(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.regionId = None
        self.regionName = None
        self.areaName = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.regionName = params.get("regionName")
        self.areaName = params.get("areaName")


class DescribeReflectUdpPortOptionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeReflectUdpPortOptionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.reflectUdpPorts = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("reflectUdpPorts") is not None:
            self.reflectUdpPorts = []
            for item in params.get("reflectUdpPorts"):
                obj = ReflectUdpPortPolicy(item)
                self.reflectUdpPorts.append(obj)


class ReflectUdpPortPolicy(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.name = None
        self.port = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.port = params.get("port")


class DescribeSecurityGroupsRequest(AbstractModel):
    def __init__(self):
        self.securityGroupIds = None
        self.securityGroupName = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.securityGroupIds = params.get("securityGroupIds")
        self.securityGroupName = params.get("securityGroupName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeSecurityGroupsResponse(AbstractModel):
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
                obj = SecurityGroupInfo(item)
                self.dataSet.append(obj)


class SecurityGroupInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.securityGroupId = None
        self.securityGroupName = None
        self.scope = None
        self.createTime = None
        self.vpcIds = None
        self.isDefault = None
        self.nicIdList = None
        self.natIdList = None
        self.loadBalancerIdList = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.securityGroupName = params.get("securityGroupName")
        self.scope = params.get("scope")
        self.createTime = params.get("createTime")
        self.vpcIds = params.get("vpcIds")
        self.isDefault = params.get("isDefault")
        self.nicIdList = params.get("nicIdList")
        self.natIdList = params.get("natIdList")
        self.loadBalancerIdList = params.get("loadBalancerIdList")


class ModifySecurityGroupsAttributeRequest(AbstractModel):
    def __init__(self):
        self.securityGroupName = None
        self.securityGroupIds = None

    def _deserialize(self, params):
        self.securityGroupName = params.get("securityGroupName")
        self.securityGroupIds = params.get("securityGroupIds")


class ModifySecurityGroupsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeSecurityGroupRuleRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")


class DescribeSecurityGroupRuleResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.ingressRuleList = None
        self.egressRuleList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("ingressRuleList") is not None:
            self.ingressRuleList = []
            for item in params.get("ingressRuleList"):
                obj = SecurityGroupRuleInfo(item)
                self.ingressRuleList.append(obj)
        if params.get("egressRuleList") is not None:
            self.egressRuleList = []
            for item in params.get("egressRuleList"):
                obj = SecurityGroupRuleInfo(item)
                self.egressRuleList.append(obj)


class SecurityGroupRuleInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.direction = None
        self.policy = None
        self.priority = None
        self.ipProtocol = None
        self.portRange = None
        self.cidrIp = None
        self.desc = None

    def _deserialize(self, params):
        self.direction = params.get("direction")
        self.policy = params.get("policy")
        self.priority = params.get("priority")
        self.ipProtocol = params.get("ipProtocol")
        self.portRange = params.get("portRange")
        self.cidrIp = params.get("cidrIp")
        self.desc = params.get("desc")


class CreateSecurityGroupRequest(AbstractModel):
    def __init__(self):
        self.scope = None
        self.securityGroupName = None
        self.ruleInfos = None

    def _deserialize(self, params):
        self.scope = params.get("scope")
        self.securityGroupName = params.get("securityGroupName")
        if params.get("ruleInfos") is not None:
            self.ruleInfos = []
            for item in params.get("ruleInfos"):
                obj = SecurityGroupRuleInfo(item)
                self.ruleInfos.append(obj)


class CreateSecurityGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.securityGroupId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.securityGroupId = params.get("securityGroupId")


class DeleteSecurityGroupRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")


class DeleteSecurityGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ConfigureSecurityGroupRulesRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None
        self.ruleInfos = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        if params.get("ruleInfos") is not None:
            self.ruleInfos = []
            for item in params.get("ruleInfos"):
                obj = SecurityGroupRuleInfo(item)
                self.ruleInfos.append(obj)


class ConfigureSecurityGroupRulesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AssignSecurityGroupVpcRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None
        self.securityGroupId = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.securityGroupId = params.get("securityGroupId")


class AssignSecurityGroupVpcResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnAssignSecurityGroupVpcRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")


class UnAssignSecurityGroupVpcResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeEipRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeEipRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")


class DescribeEipInternetChargeTypesRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.eipV4Type = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.eipV4Type = params.get("eipV4Type")


class DescribeEipInternetChargeTypesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.internetChargeTypes = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.internetChargeTypes = params.get("internetChargeTypes")


class DescribeEipRemoteRegionsRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.eipV4Type = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.eipV4Type = params.get("eipV4Type")


class DescribeEipRemoteRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.peerRegionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.peerRegionIds = params.get("peerRegionIds")


class DescribeEipsRequest(AbstractModel):
    def __init__(self):
        self.eipIds = None
        self.regionId = None
        self.name = None
        self.status = None
        self.isDefault = None
        self.pageSize = None
        self.pageNum = None
        self.privateIpAddress = None
        self.ipAddress = None
        self.ipAddresses = None
        self.instanceId = None
        self.associatedId = None
        self.cidrIds = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None
        self.internetChargeType = None

    def _deserialize(self, params):
        self.eipIds = params.get("eipIds")
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.status = params.get("status")
        self.isDefault = params.get("isDefault")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.privateIpAddress = params.get("privateIpAddress")
        self.ipAddress = params.get("ipAddress")
        self.ipAddresses = params.get("ipAddresses")
        self.instanceId = params.get("instanceId")
        self.associatedId = params.get("associatedId")
        self.cidrIds = params.get("cidrIds")
        self.resourceGroupId = params.get("resourceGroupId")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)
        self.internetChargeType = params.get("internetChargeType")


class DescribeEipsResponse(AbstractModel):
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
                obj = EipInfo(item)
                self.dataSet.append(obj)


class EipInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.eipId = None
        self.name = None
        self.regionId = None
        self.peerRegionId = None
        self.isDefault = None
        self.status = None
        self.publicIpAddresses = None
        self.privateIpAddress = None
        self.eipV4Type = None
        self.internetChargeType = None
        self.cidrId = None
        self.nicId = None
        self.associatedId = None
        self.associatedType = None
        self.instanceId = None
        self.bindType = None
        self.flowPackage = None
        self.bandwidth = None
        self.eipGeoRefs = None
        self.blockInfoList = None
        self.createTime = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.bandwidthCluster = None
        self.tags = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.name = params.get("name")
        self.regionId = params.get("regionId")
        self.peerRegionId = params.get("peerRegionId")
        self.isDefault = params.get("isDefault")
        self.status = params.get("status")
        self.publicIpAddresses = params.get("publicIpAddresses")
        self.privateIpAddress = params.get("privateIpAddress")
        self.eipV4Type = params.get("eipV4Type")
        self.internetChargeType = params.get("internetChargeType")
        self.cidrId = params.get("cidrId")
        self.nicId = params.get("nicId")
        self.associatedId = params.get("associatedId")
        self.associatedType = params.get("associatedType")
        self.instanceId = params.get("instanceId")
        self.bindType = params.get("bindType")
        self.flowPackage = params.get("flowPackage")
        self.bandwidth = params.get("bandwidth")
        if params.get("eipGeoRefs") is not None:
            self.eipGeoRefs = []
            for item in params.get("eipGeoRefs"):
                obj = EipGeoInfo(item)
                self.eipGeoRefs.append(obj)
        if params.get("blockInfoList") is not None:
            self.blockInfoList = []
            for item in params.get("blockInfoList"):
                obj = BlockInfo(item)
                self.blockInfoList.append(obj)
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        if params.get("bandwidthCluster") is not None:
            self.bandwidthCluster = BandwidthClusterInfo(params.get("bandwidthCluster"))
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class EipGeoInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dbIp = None
        self.ipData = None
        self.ipInfo = None
        self.maxMind = None
        self.standard = None
        self.isConsistent = None

    def _deserialize(self, params):
        self.dbIp = params.get("dbIp")
        self.ipData = params.get("ipData")
        self.ipInfo = params.get("ipInfo")
        self.maxMind = params.get("maxMind")
        self.standard = params.get("standard")
        self.isConsistent = params.get("isConsistent")


class BlockInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.ip = None
        self.bps = None
        self.pps = None
        self.inCps = None
        self.outCps = None

    def _deserialize(self, params):
        self.ip = params.get("ip")
        self.bps = params.get("bps")
        self.pps = params.get("pps")
        self.inCps = params.get("inCps")
        self.outCps = params.get("outCps")


class CreateEipsRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.name = None
        self.internetChargeType = None
        self.amount = None
        self.eipV4Type = None
        self.primaryIsp = None
        self.bandwidth = None
        self.cidrId = None
        self.publicIp = None
        self.resourceGroupId = None
        self.flowPackage = None
        self.clusterId = None
        self.peerRegionId = None
        self.marketingOptions = None
        self.tags = None
        self.instanceIds = None
        self.bindType = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.internetChargeType = params.get("internetChargeType")
        self.amount = params.get("amount")
        self.eipV4Type = params.get("eipV4Type")
        self.primaryIsp = params.get("primaryIsp")
        self.bandwidth = params.get("bandwidth")
        self.cidrId = params.get("cidrId")
        self.publicIp = params.get("publicIp")
        self.resourceGroupId = params.get("resourceGroupId")
        self.flowPackage = params.get("flowPackage")
        self.clusterId = params.get("clusterId")
        self.peerRegionId = params.get("peerRegionId")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))
        self.instanceIds = params.get("instanceIds")
        self.bindType = params.get("bindType")


class CreateEipsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.eipIds = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.eipIds = params.get("eipIds")
        self.orderNumber = params.get("orderNumber")


class DeleteEipRequest(AbstractModel):
    def __init__(self):
        self.eipId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")


class DeleteEipResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewEipRequest(AbstractModel):
    def __init__(self):
        self.eipId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")


class RenewEipResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ConfigEipEgressIpRequest(AbstractModel):
    def __init__(self):
        self.eipId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")


class ConfigEipEgressIpResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeEipPriceRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.internetChargeType = None
        self.amount = None
        self.eipV4Type = None
        self.bandwidth = None
        self.flowPackage = None
        self.cidrId = None
        self.clusterId = None
        self.peerRegionId = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.internetChargeType = params.get("internetChargeType")
        self.amount = params.get("amount")
        self.eipV4Type = params.get("eipV4Type")
        self.bandwidth = params.get("bandwidth")
        self.flowPackage = params.get("flowPackage")
        self.cidrId = params.get("cidrId")
        self.clusterId = params.get("clusterId")
        self.peerRegionId = params.get("peerRegionId")


class DescribeEipPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.eipPrice = None
        self.bandwidthPrice = None
        self.remoteBandwidthPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("eipPrice") is not None:
            self.eipPrice = PriceItem(params.get("eipPrice"))
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = PriceItem(params.get("bandwidthPrice"))
        if params.get("remoteBandwidthPrice") is not None:
            self.remoteBandwidthPrice = PriceItem(params.get("remoteBandwidthPrice"))


class ChangeEipInternetChargeTypeRequest(AbstractModel):
    def __init__(self):
        self.eipId = None
        self.internetChargeType = None
        self.clusterId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.internetChargeType = params.get("internetChargeType")
        self.clusterId = params.get("clusterId")


class ChangeEipInternetChargeTypeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")


class AvailableLanIpRequest(AbstractModel):
    def __init__(self):
        self.eipId = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")


class AvailableLanIpResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.lanIps = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("lanIps") is not None:
            self.lanIps = []
            for item in params.get("lanIps"):
                obj = PrivateIpInfo(item)
                self.lanIps.append(obj)


class PrivateIpInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.lanIp = None
        self.nicId = None
        self.nicName = None
        self.instanceId = None
        self.instanceName = None

    def _deserialize(self, params):
        self.lanIp = params.get("lanIp")
        self.nicId = params.get("nicId")
        self.nicName = params.get("nicName")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")


class DescribeEipTrafficRequest(AbstractModel):
    def __init__(self):
        self.eipId = None
        self.startTime = None
        self.endTime = None
        self.step = None
        self.wanIp = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.step = params.get("step")
        self.wanIp = params.get("wanIp")


class DescribeEipTrafficResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataList = None
        self.in95 = None
        self.inAvg = None
        self.inMax = None
        self.inMin = None
        self.inTotal = None
        self.out95 = None
        self.outAvg = None
        self.outMax = None
        self.outMin = None
        self.outTotal = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = EipTrafficData(item)
                self.dataList.append(obj)
        self.in95 = params.get("in95")
        self.inAvg = params.get("inAvg")
        self.inMax = params.get("inMax")
        self.inMin = params.get("inMin")
        self.inTotal = params.get("inTotal")
        self.out95 = params.get("out95")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.outTotal = params.get("outTotal")


class EipTrafficData(AbstractModel):
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


class AssociateEipAddressRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.nicId = None
        self.lanIp = None
        self.natId = None
        self.eipIds = None
        self.bindType = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.nicId = params.get("nicId")
        self.lanIp = params.get("lanIp")
        self.natId = params.get("natId")
        self.eipIds = params.get("eipIds")
        self.bindType = params.get("bindType")


class AssociateEipAddressResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.failedEipIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.failedEipIds = params.get("failedEipIds")


class UnassociateEipAddressRequest(AbstractModel):
    def __init__(self):
        self.eipIds = None

    def _deserialize(self, params):
        self.eipIds = params.get("eipIds")


class UnassociateEipAddressResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.failedEipIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.failedEipIds = params.get("failedEipIds")


class ReplaceEipAddressRequest(AbstractModel):
    def __init__(self):
        self.replaceIps = None

    def _deserialize(self, params):
        if params.get("replaceIps") is not None:
            self.replaceIps = []
            for item in params.get("replaceIps"):
                obj = ReplaceIp(item)
                self.replaceIps.append(obj)


class ReplaceIp(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.eipId = None
        self.ownIp = None
        self.targetIp = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.ownIp = params.get("ownIp")
        self.targetIp = params.get("targetIp")


class ReplaceEipAddressResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.failedEipIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.failedEipIds = params.get("failedEipIds")


class ModifyEipAttributeRequest(AbstractModel):
    def __init__(self):
        self.eipId = None
        self.name = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.name = params.get("name")


class ModifyEipAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyEipBandwidthRequest(AbstractModel):
    def __init__(self):
        self.eipId = None
        self.bandwidth = None
        self.commitBandwidth = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.bandwidth = params.get("bandwidth")
        self.commitBandwidth = params.get("commitBandwidth")


class ModifyEipBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ChangeEipBindTypeRequest(AbstractModel):
    def __init__(self):
        self.eipId = None
        self.bindType = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.bindType = params.get("bindType")


class ChangeEipBindTypeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeEipMonitorDataRequest(AbstractModel):
    def __init__(self):
        self.eipId = None
        self.metricType = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.metricType = params.get("metricType")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeEipMonitorDataResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.inMaxValue = None
        self.inAvgValue = None
        self.inMinValue = None
        self.inTotalValue = None
        self.outMaxValue = None
        self.outAvgValue = None
        self.outMinValue = None
        self.outTotalValue = None
        self.loseOutMaxValue = None
        self.loseOutMinValue = None
        self.loseOutTotalValue = None
        self.loseInMaxValue = None
        self.loseInMinValue = None
        self.loseInTotalValue = None
        self.dataList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.inMaxValue = params.get("inMaxValue")
        self.inAvgValue = params.get("inAvgValue")
        self.inMinValue = params.get("inMinValue")
        self.inTotalValue = params.get("inTotalValue")
        self.outMaxValue = params.get("outMaxValue")
        self.outAvgValue = params.get("outAvgValue")
        self.outMinValue = params.get("outMinValue")
        self.outTotalValue = params.get("outTotalValue")
        self.loseOutMaxValue = params.get("loseOutMaxValue")
        self.loseOutMinValue = params.get("loseOutMinValue")
        self.loseOutTotalValue = params.get("loseOutTotalValue")
        self.loseInMaxValue = params.get("loseInMaxValue")
        self.loseInMinValue = params.get("loseInMinValue")
        self.loseInTotalValue = params.get("loseInTotalValue")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = EipMetricValue(item)
                self.dataList.append(obj)


class EipMetricValue(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.time = None
        self.inValue = None
        self.outValue = None
        self.loseIn = None
        self.loseOut = None

    def _deserialize(self, params):
        self.time = params.get("time")
        self.inValue = params.get("inValue")
        self.outValue = params.get("outValue")
        self.loseIn = params.get("loseIn")
        self.loseOut = params.get("loseOut")


class DescribeDDosAllEventListRequest(AbstractModel):
    def __init__(self):
        self.status = None
        self.ipAddress = None
        self.startTime = None
        self.endTime = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.status = params.get("status")
        self.ipAddress = params.get("ipAddress")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeDDosAllEventListResponse(AbstractModel):
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
                obj = AttackEventInfo(item)
                self.dataSet.append(obj)


class AttackEventInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.eventId = None
        self.status = None
        self.ipAddress = None
        self.protecting = None
        self.startTime = None
        self.endTime = None
        self.endBlackholeTime = None
        self.attackBandwidthMax = None
        self.attackPackageMax = None
        self.regionId = None

    def _deserialize(self, params):
        self.eventId = params.get("eventId")
        self.status = params.get("status")
        self.ipAddress = params.get("ipAddress")
        self.protecting = params.get("protecting")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.endBlackholeTime = params.get("endBlackholeTime")
        self.attackBandwidthMax = params.get("attackBandwidthMax")
        self.attackPackageMax = params.get("attackPackageMax")
        self.regionId = params.get("regionId")


class DescribeDDosEventDetailRequest(AbstractModel):
    def __init__(self):
        self.eventId = None
        self.regionId = None

    def _deserialize(self, params):
        self.eventId = params.get("eventId")
        self.regionId = params.get("regionId")


class DescribeDDosEventDetailResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.eventId = None
        self.status = None
        self.type = None
        self.ipAddress = None
        self.protecting = None
        self.startTime = None
        self.endTime = None
        self.endBlackholeTime = None
        self.attackBandwidthMax = None
        self.protectedBandwidthMax = None
        self.attackPackageMax = None
        self.protectedPackageMax = None
        self.sourceIp = None
        self.sourcePort = None
        self.desertionPort = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.eventId = params.get("eventId")
        self.status = params.get("status")
        self.type = params.get("type")
        self.ipAddress = params.get("ipAddress")
        self.protecting = params.get("protecting")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.endBlackholeTime = params.get("endBlackholeTime")
        self.attackBandwidthMax = params.get("attackBandwidthMax")
        self.protectedBandwidthMax = params.get("protectedBandwidthMax")
        self.attackPackageMax = params.get("attackPackageMax")
        self.protectedPackageMax = params.get("protectedPackageMax")
        self.sourceIp = params.get("sourceIp")
        if params.get("sourcePort") is not None:
            self.sourcePort = []
            for item in params.get("sourcePort"):
                obj = TopPort(item)
                self.sourcePort.append(obj)
        if params.get("desertionPort") is not None:
            self.desertionPort = []
            for item in params.get("desertionPort"):
                obj = TopPort(item)
                self.desertionPort.append(obj)


class TopPort(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.protocol = None
        self.port = None

    def _deserialize(self, params):
        self.protocol = params.get("protocol")
        self.port = params.get("port")


class DescribeZonesRequest(AbstractModel):
    def __init__(self):
        self.zoneIds = None

    def _deserialize(self, params):
        self.zoneIds = params.get("zoneIds")


class DescribeZonesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.zoneSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("zoneSet") is not None:
            self.zoneSet = []
            for item in params.get("zoneSet"):
                obj = ZoneInfo(item)
                self.zoneSet.append(obj)


class ZoneInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.regionId = None
        self.zoneName = None
        self.supportSecurityGroup = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.regionId = params.get("regionId")
        self.zoneName = params.get("zoneName")
        self.supportSecurityGroup = params.get("supportSecurityGroup")


class DescribePoolsRequest(AbstractModel):
    def __init__(self):
        self.poolIds = None
        self.regionId = None
        self.name = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.poolIds = params.get("poolIds")
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribePoolsResponse(AbstractModel):
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
                obj = PoolInfo(item)
                self.dataSet.append(obj)


class PoolInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.poolId = None
        self.regionId = None
        self.name = None
        self.createTime = None

    def _deserialize(self, params):
        self.poolId = params.get("poolId")
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.createTime = params.get("createTime")


class DescribeCidrRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeCidrRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")


class DescribeCidrPriceRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.eipV4Type = None
        self.netmask = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.eipV4Type = params.get("eipV4Type")
        if params.get("netmask") is not None:
            self.netmask = NetmaskInfo(params.get("netmask"))


class NetmaskInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.netmask = None
        self.amount = None

    def _deserialize(self, params):
        self.netmask = params.get("netmask")
        self.amount = params.get("amount")


class DescribeCidrPriceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cidrPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cidrPrice") is not None:
            self.cidrPrice = PriceItem(params.get("cidrPrice"))


class DescribeCidrsRequest(AbstractModel):
    def __init__(self):
        self.cidrIds = None
        self.regionId = None
        self.name = None
        self.cidrBlock = None
        self.source = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.cidrIds = params.get("cidrIds")
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.source = params.get("source")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeCidrsResponse(AbstractModel):
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
                obj = CidrInfo(item)
                self.dataSet.append(obj)


class CidrInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cidrId = None
        self.regionId = None
        self.name = None
        self.cidrBlock = None
        self.totalCount = None
        self.usedCount = None
        self.source = None
        self.eipV4Type = None
        self.netmask = None
        self.poolId = None
        self.createTime = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.status = None
        self.tags = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.totalCount = params.get("totalCount")
        self.usedCount = params.get("usedCount")
        self.source = params.get("source")
        self.eipV4Type = params.get("eipV4Type")
        self.netmask = params.get("netmask")
        self.poolId = params.get("poolId")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.status = params.get("status")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class CreateCidrRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.eipV4Type = None
        self.netmask = None
        self.name = None
        self.resourceGroupId = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.eipV4Type = params.get("eipV4Type")
        if params.get("netmask") is not None:
            self.netmask = NetmaskInfo(params.get("netmask"))
        self.name = params.get("name")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateCidrResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.cidrIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.cidrIds = params.get("cidrIds")


class ModifyCidrAttributeRequest(AbstractModel):
    def __init__(self):
        self.cidrId = None
        self.name = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")
        self.name = params.get("name")


class ModifyCidrAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteCidrRequest(AbstractModel):
    def __init__(self):
        self.cidrId = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")


class DeleteCidrResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewCidrRequest(AbstractModel):
    def __init__(self):
        self.cidrId = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")


class RenewCidrResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteCidrsRequest(AbstractModel):
    def __init__(self):
        self.cidrIds = None

    def _deserialize(self, params):
        self.cidrIds = params.get("cidrIds")


class DeleteCidrsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.failedCidrIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.failedCidrIds = params.get("failedCidrIds")


class CreateCrossRegionBandwidthRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None
        self.internetChargeType = None
        self.crossRegionBandwidthName = None
        self.marketingInfo = None
        self.regionA = None
        self.regionZ = None
        self.bandwidth = None
        self.bandwidthCap = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.internetChargeType = params.get("internetChargeType")
        self.crossRegionBandwidthName = params.get("crossRegionBandwidthName")
        if params.get("marketingInfo") is not None:
            self.marketingInfo = MarketingInfo(params.get("marketingInfo"))
        self.regionA = params.get("regionA")
        self.regionZ = params.get("regionZ")
        self.bandwidth = params.get("bandwidth")
        self.bandwidthCap = params.get("bandwidthCap")


class CreateCrossRegionBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.crossRegionBandwidthId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.crossRegionBandwidthId = params.get("crossRegionBandwidthId")


class InquiryPriceCreateCrossRegionBandwidthRequest(AbstractModel):
    def __init__(self):
        self.internetChargeType = None
        self.marketingInfo = None
        self.regionA = None
        self.regionZ = None
        self.bandwidth = None

    def _deserialize(self, params):
        self.internetChargeType = params.get("internetChargeType")
        if params.get("marketingInfo") is not None:
            self.marketingInfo = MarketingInfo(params.get("marketingInfo"))
        self.regionA = params.get("regionA")
        self.regionZ = params.get("regionZ")
        self.bandwidth = params.get("bandwidth")


class InquiryPriceCreateCrossRegionBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.crossRegionBandwidthPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("crossRegionBandwidthPrice") is not None:
            self.crossRegionBandwidthPrice = PriceItem(params.get("crossRegionBandwidthPrice"))


class ModifyCrossRegionBandwidthAttributeRequest(AbstractModel):
    def __init__(self):
        self.crossRegionBandwidthIds = None
        self.crossRegionBandwidthName = None

    def _deserialize(self, params):
        self.crossRegionBandwidthIds = params.get("crossRegionBandwidthIds")
        self.crossRegionBandwidthName = params.get("crossRegionBandwidthName")


class ModifyCrossRegionBandwidthAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteCrossRegionBandwidthRequest(AbstractModel):
    def __init__(self):
        self.crossRegionBandwidthId = None

    def _deserialize(self, params):
        self.crossRegionBandwidthId = params.get("crossRegionBandwidthId")


class DeleteCrossRegionBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeCrossRegionBandwidthMonitorDataRequest(AbstractModel):
    def __init__(self):
        self.crossRegionBandwidthId = None
        self.metricType = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.crossRegionBandwidthId = params.get("crossRegionBandwidthId")
        self.metricType = params.get("metricType")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeCrossRegionBandwidthMonitorDataResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.inMaxValue = None
        self.inAvgValue = None
        self.inMinValue = None
        self.inTotalValue = None
        self.outMaxValue = None
        self.outAvgValue = None
        self.outMinValue = None
        self.outTotalValue = None
        self.dataList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.inMaxValue = params.get("inMaxValue")
        self.inAvgValue = params.get("inAvgValue")
        self.inMinValue = params.get("inMinValue")
        self.inTotalValue = params.get("inTotalValue")
        self.outMaxValue = params.get("outMaxValue")
        self.outAvgValue = params.get("outAvgValue")
        self.outMinValue = params.get("outMinValue")
        self.outTotalValue = params.get("outTotalValue")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = CrossRegionBandwidthMetricValue(item)
                self.dataList.append(obj)


class CrossRegionBandwidthMetricValue(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.time = None
        self.inValue = None
        self.outValue = None

    def _deserialize(self, params):
        self.time = params.get("time")
        self.inValue = params.get("inValue")
        self.outValue = params.get("outValue")


class InquiryPriceModifyCrossRegionBandwidthRequest(AbstractModel):
    def __init__(self):
        self.crossRegionBandwidthId = None
        self.bandwidth = None

    def _deserialize(self, params):
        self.crossRegionBandwidthId = params.get("crossRegionBandwidthId")
        self.bandwidth = params.get("bandwidth")


class InquiryPriceModifyCrossRegionBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.crossRegionBandwidthPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("crossRegionBandwidthPrice") is not None:
            self.crossRegionBandwidthPrice = PriceItem(params.get("crossRegionBandwidthPrice"))


class DescribeCrossRegionBandwidthRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeCrossRegionBandwidthRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")


class ModifyCrossRegionBandwidthRequest(AbstractModel):
    def __init__(self):
        self.crossRegionBandwidthId = None
        self.bandwidth = None
        self.bandwidthCap = None

    def _deserialize(self, params):
        self.crossRegionBandwidthId = params.get("crossRegionBandwidthId")
        self.bandwidth = params.get("bandwidth")
        self.bandwidthCap = params.get("bandwidthCap")


class ModifyCrossRegionBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewCrossRegionBandwidthRequest(AbstractModel):
    def __init__(self):
        self.crossRegionBandwidthId = None

    def _deserialize(self, params):
        self.crossRegionBandwidthId = params.get("crossRegionBandwidthId")


class RenewCrossRegionBandwidthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeCrossRegionBandwidthRequest(AbstractModel):
    def __init__(self):
        self.crossRegionBandwidthIds = None
        self.crossRegionBandwidthName = None
        self.vpcId = None
        self.regionA = None
        self.regionZ = None
        self.status = None
        self.pageSize = None
        self.pageNum = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.crossRegionBandwidthIds = params.get("crossRegionBandwidthIds")
        self.crossRegionBandwidthName = params.get("crossRegionBandwidthName")
        self.vpcId = params.get("vpcId")
        self.regionA = params.get("regionA")
        self.regionZ = params.get("regionZ")
        self.status = params.get("status")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.resourceGroupId = params.get("resourceGroupId")


class DescribeCrossRegionBandwidthResponse(AbstractModel):
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
                obj = CrossRegionBandwidthInfo(item)
                self.dataSet.append(obj)


class CrossRegionBandwidthInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.crossRegionBandwidthId = None
        self.crossRegionBandwidthName = None
        self.status = None
        self.vpcId = None
        self.regionA = None
        self.regionZ = None
        self.bandwidth = None
        self.bandwidthCap = None
        self.createTime = None
        self.internetChargeType = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None

    def _deserialize(self, params):
        self.crossRegionBandwidthId = params.get("crossRegionBandwidthId")
        self.crossRegionBandwidthName = params.get("crossRegionBandwidthName")
        self.status = params.get("status")
        self.vpcId = params.get("vpcId")
        self.regionA = params.get("regionA")
        self.regionZ = params.get("regionZ")
        self.bandwidth = params.get("bandwidth")
        self.bandwidthCap = params.get("bandwidthCap")
        self.createTime = params.get("createTime")
        self.internetChargeType = params.get("internetChargeType")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")


class CreateBorderGatewayRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.vpcId = None
        self.label = None
        self.asn = None
        self.routingMode = None
        self.advertisedSubnet = None
        self.advertisedCidrs = None
        self.advertisedRouteIds = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.label = params.get("label")
        self.asn = params.get("asn")
        self.routingMode = params.get("routingMode")
        self.advertisedSubnet = params.get("advertisedSubnet")
        self.advertisedCidrs = params.get("advertisedCidrs")
        self.advertisedRouteIds = params.get("advertisedRouteIds")


class CreateBorderGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.zbgId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.zbgId = params.get("zbgId")


class DescribeBorderGatewaysRequest(AbstractModel):
    def __init__(self):
        self.zbgIds = None
        self.name = None
        self.regionId = None
        self.vpcId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.zbgIds = params.get("zbgIds")
        self.name = params.get("name")
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeBorderGatewaysResponse(AbstractModel):
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
                obj = ZbgInfo(item)
                self.dataSet.append(obj)


class ZbgInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zbgId = None
        self.name = None
        self.vpcId = None
        self.regionId = None
        self.asn = None
        self.interConnectCidr = None
        self.createTime = None
        self.cloudRouterIds = None
        self.routingMode = None
        self.natId = None
        self.advertisedSubnet = None
        self.advertisedCidrs = None
        self.advertisedRouteIds = None

    def _deserialize(self, params):
        self.zbgId = params.get("zbgId")
        self.name = params.get("name")
        self.vpcId = params.get("vpcId")
        self.regionId = params.get("regionId")
        self.asn = params.get("asn")
        self.interConnectCidr = params.get("interConnectCidr")
        self.createTime = params.get("createTime")
        self.cloudRouterIds = params.get("cloudRouterIds")
        self.routingMode = params.get("routingMode")
        self.natId = params.get("natId")
        self.advertisedSubnet = params.get("advertisedSubnet")
        self.advertisedCidrs = params.get("advertisedCidrs")
        self.advertisedRouteIds = params.get("advertisedRouteIds")


class DeleteBorderGatewayRequest(AbstractModel):
    def __init__(self):
        self.zbgId = None

    def _deserialize(self, params):
        self.zbgId = params.get("zbgId")


class DeleteBorderGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyBorderGatewayAsnRequest(AbstractModel):
    def __init__(self):
        self.zbgId = None
        self.asn = None

    def _deserialize(self, params):
        self.zbgId = params.get("zbgId")
        self.asn = params.get("asn")


class ModifyBorderGatewayAsnResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyBorderGatewaysAttributeRequest(AbstractModel):
    def __init__(self):
        self.zbgIds = None
        self.name = None
        self.routingMode = None
        self.advertisedSubnet = None
        self.advertisedCidrs = None
        self.asn = None

    def _deserialize(self, params):
        self.zbgIds = params.get("zbgIds")
        self.name = params.get("name")
        self.routingMode = params.get("routingMode")
        self.advertisedSubnet = params.get("advertisedSubnet")
        self.advertisedCidrs = params.get("advertisedCidrs")
        self.asn = params.get("asn")


class ModifyBorderGatewaysAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAvailableNatsRequest(AbstractModel):
    def __init__(self):
        self.zbgId = None

    def _deserialize(self, params):
        self.zbgId = params.get("zbgId")


class DescribeAvailableNatsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.natIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.natIds = params.get("natIds")


class AssignBorderGatewayRequest(AbstractModel):
    def __init__(self):
        self.zbgId = None
        self.natId = None

    def _deserialize(self, params):
        self.zbgId = params.get("zbgId")
        self.natId = params.get("natId")


class AssignBorderGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnassignBorderGatewayRequest(AbstractModel):
    def __init__(self):
        self.zbgId = None

    def _deserialize(self, params):
        self.zbgId = params.get("zbgId")


class UnassignBorderGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AssignBorderGatewayRouteRequest(AbstractModel):
    def __init__(self):
        self.zbgId = None
        self.advertisedRouteIds = None

    def _deserialize(self, params):
        self.zbgId = params.get("zbgId")
        self.advertisedRouteIds = params.get("advertisedRouteIds")


class AssignBorderGatewayRouteResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnassignBorderGatewayRouteRequest(AbstractModel):
    def __init__(self):
        self.zbgId = None
        self.advertisedRouteIds = None

    def _deserialize(self, params):
        self.zbgId = params.get("zbgId")
        self.advertisedRouteIds = params.get("advertisedRouteIds")


class UnassignBorderGatewayRouteResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeZoneInstanceConfigInfosRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.instanceType = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceType = params.get("instanceType")


class DescribeZoneInstanceConfigInfosResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceTypeQuotaSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("instanceTypeQuotaSet") is not None:
            self.instanceTypeQuotaSet = []
            for item in params.get("instanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem(item)
                self.instanceTypeQuotaSet.append(obj)


class InstanceTypeQuotaItem(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.instanceType = None
        self.instanceTypeName = None
        self.cpuCount = None
        self.memory = None
        self.internetMaxBandwidthOutLimit = None
        self.withStock = None
        self.internetChargeTypes = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceType = params.get("instanceType")
        self.instanceTypeName = params.get("instanceTypeName")
        self.cpuCount = params.get("cpuCount")
        self.memory = params.get("memory")
        self.internetMaxBandwidthOutLimit = params.get("internetMaxBandwidthOutLimit")
        self.withStock = params.get("withStock")
        self.internetChargeTypes = params.get("internetChargeTypes")


class DescribeTimeZonesRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeTimeZonesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.timeZones = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.timeZones = params.get("timeZones")


class InquiryPriceCreateInstanceRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.instanceType = None
        self.eipV4Type = None
        self.internetChargeType = None
        self.trafficPackageSize = None
        self.bandwidth = None
        self.instanceCount = None
        self.systemDisk = None
        self.dataDisk = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceType = params.get("instanceType")
        self.eipV4Type = params.get("eipV4Type")
        self.internetChargeType = params.get("internetChargeType")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.bandwidth = params.get("bandwidth")
        self.instanceCount = params.get("instanceCount")
        if params.get("systemDisk") is not None:
            self.systemDisk = SystemDisk(params.get("systemDisk"))
        if params.get("dataDisk") is not None:
            self.dataDisk = DataDisk(params.get("dataDisk"))


class SystemDisk(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.diskId = None
        self.diskSize = None
        self.diskCategory = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.diskSize = params.get("diskSize")
        self.diskCategory = params.get("diskCategory")


class DataDisk(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.diskId = None
        self.diskName = None
        self.diskSize = None
        self.diskAmount = None
        self.portable = None
        self.diskCategory = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.diskName = params.get("diskName")
        self.diskSize = params.get("diskSize")
        self.diskAmount = params.get("diskAmount")
        self.portable = params.get("portable")
        self.diskCategory = params.get("diskCategory")


class InquiryPriceCreateInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.specPrice = None
        self.gpuPrice = None
        self.ipv4Price = None
        self.ipv4BandwidthPrice = None
        self.ipv6Price = None
        self.ipv6BandwidthPrice = None
        self.systemDiskPrice = None
        self.dataDiskPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("specPrice") is not None:
            self.specPrice = PriceItem(params.get("specPrice"))
        if params.get("gpuPrice") is not None:
            self.gpuPrice = PriceItem(params.get("gpuPrice"))
        if params.get("ipv4Price") is not None:
            self.ipv4Price = PriceItem(params.get("ipv4Price"))
        if params.get("ipv4BandwidthPrice") is not None:
            self.ipv4BandwidthPrice = PriceItem(params.get("ipv4BandwidthPrice"))
        if params.get("ipv6Price") is not None:
            self.ipv6Price = PriceItem(params.get("ipv6Price"))
        if params.get("ipv6BandwidthPrice") is not None:
            self.ipv6BandwidthPrice = PriceItem(params.get("ipv6BandwidthPrice"))
        if params.get("systemDiskPrice") is not None:
            self.systemDiskPrice = PriceItem(params.get("systemDiskPrice"))
        if params.get("dataDiskPrice") is not None:
            self.dataDiskPrice = PriceItem(params.get("dataDiskPrice"))


class CreateZecInstancesRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.imageId = None
        self.timeZone = None
        self.instanceType = None
        self.instanceName = None
        self.password = None
        self.keyId = None
        self.nicNetworkType = None
        self.instanceCount = None
        self.systemDisk = None
        self.dataDisks = None
        self.securityGroupId = None
        self.subnetId = None
        self.lanIp = None
        self.enableAgent = None
        self.enableIpForward = None
        self.internetChargeType = None
        self.trafficPackageSize = None
        self.bandwidth = None
        self.eipBindType = None
        self.eipV4Type = None
        self.clusterId = None
        self.resourceGroupId = None
        self.marketingOptions = None
        self.tags = None
        self.userData = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.imageId = params.get("imageId")
        self.timeZone = params.get("timeZone")
        self.instanceType = params.get("instanceType")
        self.instanceName = params.get("instanceName")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.nicNetworkType = params.get("nicNetworkType")
        self.instanceCount = params.get("instanceCount")
        if params.get("systemDisk") is not None:
            self.systemDisk = SystemDisk(params.get("systemDisk"))
        if params.get("dataDisks") is not None:
            self.dataDisks = []
            for item in params.get("dataDisks"):
                obj = DataDisk(item)
                self.dataDisks.append(obj)
        self.securityGroupId = params.get("securityGroupId")
        self.subnetId = params.get("subnetId")
        self.lanIp = params.get("lanIp")
        self.enableAgent = params.get("enableAgent")
        self.enableIpForward = params.get("enableIpForward")
        self.internetChargeType = params.get("internetChargeType")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.bandwidth = params.get("bandwidth")
        self.eipBindType = params.get("eipBindType")
        self.eipV4Type = params.get("eipV4Type")
        self.clusterId = params.get("clusterId")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))
        self.userData = params.get("userData")


class CreateZecInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.instanceIdSet = None
        self.instances = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.instanceIdSet = params.get("instanceIdSet")
        if params.get("instances") is not None:
            self.instances = []
            for item in params.get("instances"):
                obj = DiskWithInstance(item)
                self.instances.append(obj)


class DiskWithInstance(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.diskIdSet = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.diskIdSet = params.get("diskIdSet")


class DescribeInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.zoneId = None
        self.imageId = None
        self.ipv4Address = None
        self.ipv6Address = None
        self.status = None
        self.name = None
        self.pageSize = None
        self.pageNum = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.zoneId = params.get("zoneId")
        self.imageId = params.get("imageId")
        self.ipv4Address = params.get("ipv4Address")
        self.ipv6Address = params.get("ipv6Address")
        self.status = params.get("status")
        self.name = params.get("name")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.resourceGroupId = params.get("resourceGroupId")
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
        self.instanceName = None
        self.zoneId = None
        self.instanceType = None
        self.cpu = None
        self.memory = None
        self.imageId = None
        self.imageName = None
        self.timeZone = None
        self.nicNetworkType = None
        self.status = None
        self.systemDisk = None
        self.dataDisks = None
        self.publicIpAddresses = None
        self.privateIpAddresses = None
        self.keyId = None
        self.subnetId = None
        self.securityGroupId = None
        self.enableAgent = None
        self.enableAgentMonitor = None
        self.enableIpForward = None
        self.createTime = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.nics = None
        self.tags = None
        self.loadBalancerIds = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.zoneId = params.get("zoneId")
        self.instanceType = params.get("instanceType")
        self.cpu = params.get("cpu")
        self.memory = params.get("memory")
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")
        self.timeZone = params.get("timeZone")
        self.nicNetworkType = params.get("nicNetworkType")
        self.status = params.get("status")
        if params.get("systemDisk") is not None:
            self.systemDisk = SystemDisk(params.get("systemDisk"))
        if params.get("dataDisks") is not None:
            self.dataDisks = []
            for item in params.get("dataDisks"):
                obj = DataDisk(item)
                self.dataDisks.append(obj)
        self.publicIpAddresses = params.get("publicIpAddresses")
        self.privateIpAddresses = params.get("privateIpAddresses")
        self.keyId = params.get("keyId")
        self.subnetId = params.get("subnetId")
        self.securityGroupId = params.get("securityGroupId")
        self.enableAgent = params.get("enableAgent")
        self.enableAgentMonitor = params.get("enableAgentMonitor")
        self.enableIpForward = params.get("enableIpForward")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        if params.get("nics") is not None:
            self.nics = []
            for item in params.get("nics"):
                obj = NicInfo(item)
                self.nics.append(obj)
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))
        self.loadBalancerIds = params.get("loadBalancerIds")


class DescribeInstancesStatusRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.pageSize = None
        self.pageNum = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.resourceGroupId = params.get("resourceGroupId")


class DescribeInstancesStatusResponse(AbstractModel):
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
                obj = InstanceStatus(item)
                self.dataSet.append(obj)


class InstanceStatus(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.instanceStatus = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.instanceStatus = params.get("instanceStatus")


class ModifyInstancesAttributeRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.instanceName = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.instanceName = params.get("instanceName")


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
        self.instanceIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.instanceIds = params.get("instanceIds")


class StopInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.forceShutdown = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.forceShutdown = params.get("forceShutdown")


class StopInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.instanceIds = params.get("instanceIds")


class RebootInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")


class RebootInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.instanceIds = params.get("instanceIds")


class ResetInstancePasswordRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.password = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.password = params.get("password")


class ResetInstancePasswordResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ResetInstanceRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.password = None
        self.keyId = None
        self.imageId = None
        self.timezone = None
        self.enableAgent = None
        self.instanceName = None
        self.userData = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.imageId = params.get("imageId")
        self.timezone = params.get("timezone")
        self.enableAgent = params.get("enableAgent")
        self.instanceName = params.get("instanceName")
        self.userData = params.get("userData")


class ResetInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ResetInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.password = None
        self.keyId = None
        self.imageId = None
        self.timezone = None
        self.enableAgent = None
        self.instanceName = None
        self.userData = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.imageId = params.get("imageId")
        self.timezone = params.get("timezone")
        self.enableAgent = params.get("enableAgent")
        self.instanceName = params.get("instanceName")
        self.userData = params.get("userData")


class ResetInstancesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.instanceIds = params.get("instanceIds")


class StartIpForwardRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class StartIpForwardResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class StopIpForwardRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class StopIpForwardResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class StartAgentMonitorRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class StartAgentMonitorResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class StopAgentMonitorRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class StopAgentMonitorResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyInstanceTypeRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.instanceType = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.instanceType = params.get("instanceType")


class ModifyInstanceTypeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ChangeNicNetworkTypeRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.nicNetworkType = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.nicNetworkType = params.get("nicNetworkType")


class ChangeNicNetworkTypeResponse(AbstractModel):
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
        self.instanceIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.instanceIds = params.get("instanceIds")


class DescribeVncUrlRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class DescribeVncUrlResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.url = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.url = params.get("url")


class DescribeInstanceMonitorDataRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.metricType = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.metricType = params.get("metricType")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeInstanceMonitorDataResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.maxValue = None
        self.minValue = None
        self.avgValue = None
        self.metrics = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.maxValue = params.get("maxValue")
        self.minValue = params.get("minValue")
        self.avgValue = params.get("avgValue")
        if params.get("metrics") is not None:
            self.metrics = []
            for item in params.get("metrics"):
                obj = MetricValue(item)
                self.metrics.append(obj)


class CreateNatGatewayRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.vpcId = None
        self.name = None
        self.subnetIds = None
        self.securityGroupId = None
        self.resourceGroupId = None
        self.tags = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.name = params.get("name")
        self.subnetIds = params.get("subnetIds")
        self.securityGroupId = params.get("securityGroupId")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateNatGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.natGatewayId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.natGatewayId = params.get("natGatewayId")


class ModifyNatGatewayAttributeRequest(AbstractModel):
    def __init__(self):
        self.natGatewayId = None
        self.name = None
        self.subnetIds = None
        self.isAllSubnet = None
        self.icmpReplyEnabled = None
        self.securityGroupId = None

    def _deserialize(self, params):
        self.natGatewayId = params.get("natGatewayId")
        self.name = params.get("name")
        self.subnetIds = params.get("subnetIds")
        self.isAllSubnet = params.get("isAllSubnet")
        self.icmpReplyEnabled = params.get("icmpReplyEnabled")
        self.securityGroupId = params.get("securityGroupId")


class ModifyNatGatewayAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeNatGatewayRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeNatGatewayRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")


class DescribeNatGatewaysRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.vpcId = None
        self.natGatewayIds = None
        self.name = None
        self.status = None
        self.securityGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.natGatewayIds = params.get("natGatewayIds")
        self.name = params.get("name")
        self.status = params.get("status")
        self.securityGroupId = params.get("securityGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.resourceGroupId = params.get("resourceGroupId")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeNatGatewaysResponse(AbstractModel):
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
                obj = NatGateway(item)
                self.dataSet.append(obj)


class NatGateway(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.natGatewayId = None
        self.vpcId = None
        self.regionId = None
        self.status = None
        self.name = None
        self.subnetIds = None
        self.isAllSubnets = None
        self.eipIds = None
        self.zbgId = None
        self.icmpReplyEnabled = None
        self.securityGroupId = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.createTime = None
        self.expiredTime = None
        self.tags = None

    def _deserialize(self, params):
        self.natGatewayId = params.get("natGatewayId")
        self.vpcId = params.get("vpcId")
        self.regionId = params.get("regionId")
        self.status = params.get("status")
        self.name = params.get("name")
        self.subnetIds = params.get("subnetIds")
        self.isAllSubnets = params.get("isAllSubnets")
        self.eipIds = params.get("eipIds")
        self.zbgId = params.get("zbgId")
        self.icmpReplyEnabled = params.get("icmpReplyEnabled")
        self.securityGroupId = params.get("securityGroupId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class DescribeNatGatewayDetailRequest(AbstractModel):
    def __init__(self):
        self.natGatewayId = None

    def _deserialize(self, params):
        self.natGatewayId = params.get("natGatewayId")


class DescribeNatGatewayDetailResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.natGatewayId = None
        self.name = None
        self.snats = None
        self.dnats = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.natGatewayId = params.get("natGatewayId")
        self.name = params.get("name")
        if params.get("snats") is not None:
            self.snats = []
            for item in params.get("snats"):
                obj = SnatEntry(item)
                self.snats.append(obj)
        if params.get("dnats") is not None:
            self.dnats = []
            for item in params.get("dnats"):
                obj = DnatEntry(item)
                self.dnats.append(obj)


class SnatEntry(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.snatEntryId = None
        self.cidrs = None
        self.eipIds = None
        self.isAllEip = None
        self.snatSubnets = None

    def _deserialize(self, params):
        self.snatEntryId = params.get("snatEntryId")
        self.cidrs = params.get("cidrs")
        self.eipIds = params.get("eipIds")
        self.isAllEip = params.get("isAllEip")
        if params.get("snatSubnets") is not None:
            self.snatSubnets = []
            for item in params.get("snatSubnets"):
                obj = SnatSubnet(item)
                self.snatSubnets.append(obj)


class SnatSubnet(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.subnetId = None
        self.cidr = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.cidr = params.get("cidr")


class DnatEntry(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.dnatEntryId = None
        self.status = None
        self.privateIp = None
        self.eipId = None
        self.protocol = None
        self.listenerPort = None
        self.internalPort = None

    def _deserialize(self, params):
        self.dnatEntryId = params.get("dnatEntryId")
        self.status = params.get("status")
        self.privateIp = params.get("privateIp")
        self.eipId = params.get("eipId")
        self.protocol = params.get("protocol")
        self.listenerPort = params.get("listenerPort")
        self.internalPort = params.get("internalPort")


class DeleteNatGatewayRequest(AbstractModel):
    def __init__(self):
        self.natGatewayId = None

    def _deserialize(self, params):
        self.natGatewayId = params.get("natGatewayId")


class DeleteNatGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RenewNatGatewayRequest(AbstractModel):
    def __init__(self):
        self.natGatewayId = None

    def _deserialize(self, params):
        self.natGatewayId = params.get("natGatewayId")


class RenewNatGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class InquiryPriceCreateNatGatewayRequest(AbstractModel):
    def __init__(self):
        self.regionId = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")


class InquiryPriceCreateNatGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.natGatewayPrice = None
        self.cuPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("natGatewayPrice") is not None:
            self.natGatewayPrice = PriceItem(params.get("natGatewayPrice"))
        if params.get("cuPrice") is not None:
            self.cuPrice = PriceItem(params.get("cuPrice"))


class CreateSnatEntryRequest(AbstractModel):
    def __init__(self):
        self.natGatewayId = None
        self.eipIds = None
        self.cidr = None
        self.sourceCidrBlocks = None
        self.subnetIds = None

    def _deserialize(self, params):
        self.natGatewayId = params.get("natGatewayId")
        self.eipIds = params.get("eipIds")
        self.cidr = params.get("cidr")
        self.sourceCidrBlocks = params.get("sourceCidrBlocks")
        self.subnetIds = params.get("subnetIds")


class CreateSnatEntryResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.snatEntryId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.snatEntryId = params.get("snatEntryId")


class ModifySnatEntryRequest(AbstractModel):
    def __init__(self):
        self.snatEntryId = None
        self.eipIds = None
        self.isAllEip = None
        self.cidr = None
        self.sourceCidrBlocks = None
        self.subnetIds = None

    def _deserialize(self, params):
        self.snatEntryId = params.get("snatEntryId")
        self.eipIds = params.get("eipIds")
        self.isAllEip = params.get("isAllEip")
        self.cidr = params.get("cidr")
        self.sourceCidrBlocks = params.get("sourceCidrBlocks")
        self.subnetIds = params.get("subnetIds")


class ModifySnatEntryResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteSnatEntryRequest(AbstractModel):
    def __init__(self):
        self.snatEntryId = None

    def _deserialize(self, params):
        self.snatEntryId = params.get("snatEntryId")


class DeleteSnatEntryResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class CreateDnatEntryRequest(AbstractModel):
    def __init__(self):
        self.natGatewayId = None
        self.eipId = None
        self.privateIp = None
        self.protocol = None
        self.listenerPort = None
        self.internalPort = None

    def _deserialize(self, params):
        self.natGatewayId = params.get("natGatewayId")
        self.eipId = params.get("eipId")
        self.privateIp = params.get("privateIp")
        self.protocol = params.get("protocol")
        self.listenerPort = params.get("listenerPort")
        self.internalPort = params.get("internalPort")


class CreateDnatEntryResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dnatEntryId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.dnatEntryId = params.get("dnatEntryId")


class ModifyDnatEntryRequest(AbstractModel):
    def __init__(self):
        self.dnatEntryId = None
        self.eipId = None
        self.privateIp = None
        self.protocol = None
        self.listenerPort = None
        self.internalPort = None

    def _deserialize(self, params):
        self.dnatEntryId = params.get("dnatEntryId")
        self.eipId = params.get("eipId")
        self.privateIp = params.get("privateIp")
        self.protocol = params.get("protocol")
        self.listenerPort = params.get("listenerPort")
        self.internalPort = params.get("internalPort")


class ModifyDnatEntryResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteDnatEntryRequest(AbstractModel):
    def __init__(self):
        self.dnatEntryId = None

    def _deserialize(self, params):
        self.dnatEntryId = params.get("dnatEntryId")


class DeleteDnatEntryResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAvailableBorderGatewayRequest(AbstractModel):
    def __init__(self):
        self.natGatewayId = None

    def _deserialize(self, params):
        self.natGatewayId = params.get("natGatewayId")


class DescribeAvailableBorderGatewayResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.zbgId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.zbgId = params.get("zbgId")


class CreateRouteRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None
        self.ipVersion = None
        self.routeType = None
        self.sourceCidrBlock = None
        self.destinationCidrBlock = None
        self.cidrBlock = None
        self.priority = None
        self.nextHopId = None
        self.nextHotId = None
        self.name = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.ipVersion = params.get("ipVersion")
        self.routeType = params.get("routeType")
        self.sourceCidrBlock = params.get("sourceCidrBlock")
        self.destinationCidrBlock = params.get("destinationCidrBlock")
        self.cidrBlock = params.get("cidrBlock")
        self.priority = params.get("priority")
        self.nextHopId = params.get("nextHopId")
        self.nextHotId = params.get("nextHotId")
        self.name = params.get("name")


class CreateRouteResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.routeId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.routeId = params.get("routeId")


class ModifyRouteAttributeRequest(AbstractModel):
    def __init__(self):
        self.routeId = None
        self.name = None

    def _deserialize(self, params):
        self.routeId = params.get("routeId")
        self.name = params.get("name")


class ModifyRouteAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteRouteRequest(AbstractModel):
    def __init__(self):
        self.routeId = None

    def _deserialize(self, params):
        self.routeId = params.get("routeId")


class DeleteRouteResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeRoutesRequest(AbstractModel):
    def __init__(self):
        self.routeIds = None
        self.vpcId = None
        self.ipVersion = None
        self.routeType = None
        self.name = None
        self.destinationCidrBlock = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.routeIds = params.get("routeIds")
        self.vpcId = params.get("vpcId")
        self.ipVersion = params.get("ipVersion")
        self.routeType = params.get("routeType")
        self.name = params.get("name")
        self.destinationCidrBlock = params.get("destinationCidrBlock")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeRoutesResponse(AbstractModel):
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
                obj = RouteInfo(item)
                self.dataSet.append(obj)


class RouteInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.routeId = None
        self.name = None
        self.vpcId = None
        self.vpcName = None
        self.ipVersion = None
        self.type = None
        self.sourceCidrBlock = None
        self.destinationCidrBlock = None
        self.cidrBlock = None
        self.priority = None
        self.nextHopId = None
        self.nextHopName = None
        self.nextHopType = None
        self.createTime = None

    def _deserialize(self, params):
        self.routeId = params.get("routeId")
        self.name = params.get("name")
        self.vpcId = params.get("vpcId")
        self.vpcName = params.get("vpcName")
        self.ipVersion = params.get("ipVersion")
        self.type = params.get("type")
        self.sourceCidrBlock = params.get("sourceCidrBlock")
        self.destinationCidrBlock = params.get("destinationCidrBlock")
        self.cidrBlock = params.get("cidrBlock")
        self.priority = params.get("priority")
        self.nextHopId = params.get("nextHopId")
        self.nextHopName = params.get("nextHopName")
        self.nextHopType = params.get("nextHopType")
        self.createTime = params.get("createTime")


