#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel
import warnings

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
        self.zoneName = None
        self.supportSecurityGroup = None
        self.supportNetworkType = None
        self.supportIpv6 = None
        self.supportCpuPassThrough = None
        self.networkLineType = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.zoneName = params.get("zoneName")
        self.supportSecurityGroup = params.get("supportSecurityGroup")
        self.supportNetworkType = params.get("supportNetworkType")
        self.supportIpv6 = params.get("supportIpv6")
        self.supportCpuPassThrough = params.get("supportCpuPassThrough")
        self.networkLineType = params.get("networkLineType")


class InquiryPriceCreateInstanceRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.imageId = None
        self.instanceType = None
        self.instanceChargeType = None
        self.instanceChargePrepaid = None
        self.instanceChargePostpaid = None
        self.internetChargeType = None
        self.trafficPackageSize = None
        self.internetMaxBandwidthOut = None
        self.instanceCount = None
        self.systemDisk = None
        self.dataDisks = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.imageId = params.get("imageId")
        self.instanceType = params.get("instanceType")
        self.instanceChargeType = params.get("instanceChargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        if params.get("instanceChargePostpaid") is not None:
            self.instanceChargePostpaid = ChargePostpaid(params.get("instanceChargePostpaid"))
        self.internetChargeType = params.get("internetChargeType")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")
        self.instanceCount = params.get("instanceCount")
        if params.get("systemDisk") is not None:
            self.systemDisk = SystemDisk(params.get("systemDisk"))
        if params.get("dataDisks") is not None:
            self.dataDisks = []
            for item in params.get("dataDisks"):
                obj = DataDisk(item)
                self.dataDisks.append(obj)


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


class ChargePostpaid(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.period = None

    def _deserialize(self, params):
        self.period = params.get("period")


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
        self.diskPrice = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.diskName = params.get("diskName")
        self.diskSize = params.get("diskSize")
        self.diskAmount = params.get("diskAmount")
        self.portable = params.get("portable")
        self.diskCategory = params.get("diskCategory")
        if params.get("diskPrice") is not None:
            self.diskPrice = PriceItem(params.get("diskPrice"))


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


class InquiryPriceCreateInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instancePrice = None
        self.bandwidthPrice = None
        self.eipPrice = None
        self.systemDiskPrice = None
        self.dataDiskPrice = None
        self.dataDiskPrices = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("instancePrice") is not None:
            self.instancePrice = PriceItem(params.get("instancePrice"))
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = []
            for item in params.get("bandwidthPrice"):
                obj = PriceItem(item)
                self.bandwidthPrice.append(obj)
        if params.get("eipPrice") is not None:
            self.eipPrice = PriceItem(params.get("eipPrice"))
        if params.get("systemDiskPrice") is not None:
            self.systemDiskPrice = PriceItem(params.get("systemDiskPrice"))
        if params.get("dataDiskPrice") is not None:
            self.dataDiskPrice = PriceItem(params.get("dataDiskPrice"))
        if params.get("dataDiskPrices") is not None:
            self.dataDiskPrices = []
            for item in params.get("dataDiskPrices"):
                obj = DataDisk(item)
                self.dataDiskPrices.append(obj)


class DescribeZoneInstanceConfigInfosRequest(AbstractModel):
    def __init__(self):
        self.instanceChargeType = None
        self.zoneId = None
        self.instanceType = None

    def _deserialize(self, params):
        self.instanceChargeType = params.get("instanceChargeType")
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
        self.frequency = None
        self.internetChargeTypes = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceType = params.get("instanceType")
        self.instanceTypeName = params.get("instanceTypeName")
        self.cpuCount = params.get("cpuCount")
        self.memory = params.get("memory")
        self.internetMaxBandwidthOutLimit = params.get("internetMaxBandwidthOutLimit")
        self.frequency = params.get("frequency")
        self.internetChargeTypes = params.get("internetChargeTypes")


class CreateInstancesRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.imageId = None
        self.instanceType = None
        self.instanceName = None
        self.password = None
        self.keyId = None
        self.resourceGroupId = None
        self.instanceChargeType = None
        self.instanceChargePrepaid = None
        self.instanceChargePostpaid = None
        self.internetChargeType = None
        self.trafficPackageSize = None
        self.internetMaxBandwidthOut = None
        self.instanceCount = None
        self.systemDisk = None
        self.dataDisks = None
        self.subnetId = None
        self.enableIpv6 = None
        self.enableIpv4 = None
        self.cpuPassThrough = None
        self.initScript = None
        self.networkMode = None
        self.diskPreAllocated = None
        self.nic = None
        self.securityGroupId = None
        self.clusterId = None
        self.cidrBlockId = None
        self.startCidrIpv4 = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.imageId = params.get("imageId")
        self.instanceType = params.get("instanceType")
        self.instanceName = params.get("instanceName")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.instanceChargeType = params.get("instanceChargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        if params.get("instanceChargePostpaid") is not None:
            self.instanceChargePostpaid = ChargePostpaid(params.get("instanceChargePostpaid"))
        self.internetChargeType = params.get("internetChargeType")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")
        self.instanceCount = params.get("instanceCount")
        if params.get("systemDisk") is not None:
            self.systemDisk = SystemDisk(params.get("systemDisk"))
        if params.get("dataDisks") is not None:
            self.dataDisks = []
            for item in params.get("dataDisks"):
                obj = DataDisk(item)
                self.dataDisks.append(obj)
        self.subnetId = params.get("subnetId")
        self.enableIpv6 = params.get("enableIpv6")
        self.enableIpv4 = params.get("enableIpv4")
        self.cpuPassThrough = params.get("cpuPassThrough")
        self.initScript = params.get("initScript")
        self.networkMode = params.get("networkMode")
        self.diskPreAllocated = params.get("diskPreAllocated")
        if params.get("nic") is not None:
            self.nic = Nic(params.get("nic"))
        self.securityGroupId = params.get("securityGroupId")
        self.clusterId = params.get("clusterId")
        self.cidrBlockId = params.get("cidrBlockId")
        self.startCidrIpv4 = params.get("startCidrIpv4")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


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


class ResetInstancesPasswordRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.password = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.password = params.get("password")


class ResetInstancesPasswordResponse(AbstractModel):
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
        self.instanceName = None
        self.wanName = None
        self.lanName = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.imageId = params.get("imageId")
        self.instanceName = params.get("instanceName")
        self.wanName = params.get("wanName")
        self.lanName = params.get("lanName")


class ResetInstanceResponse(AbstractModel):
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


class DescribeInstancesRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.zoneId = None
        self.internetChargeType = None
        self.imageId = None
        self.instanceType = None
        self.keyId = None
        self.publicIpAddresses = None
        self.privateIpAddresses = None
        self.instanceStatus = None
        self.instanceName = None
        self.subnetId = None
        self.securityGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.zoneId = params.get("zoneId")
        self.internetChargeType = params.get("internetChargeType")
        self.imageId = params.get("imageId")
        self.instanceType = params.get("instanceType")
        self.keyId = params.get("keyId")
        self.publicIpAddresses = params.get("publicIpAddresses")
        self.privateIpAddresses = params.get("privateIpAddresses")
        self.instanceStatus = params.get("instanceStatus")
        self.instanceName = params.get("instanceName")
        self.subnetId = params.get("subnetId")
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
        self.instanceType = None
        self.cpuCount = None
        self.memory = None
        self.imageId = None
        self.imageName = None
        self.instanceChargeType = None
        self.internetMaxBandwidthOut = None
        self.internetChargeType = None
        self.period = None
        self.publicIpAddresses = None
        self.publicIpv6Addresses = None
        self.privateIpAddresses = None
        self.subnetId = None
        self.createTime = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.instanceStatus = None
        self.trafficPackageSize = None
        self.securityGroupIds = None
        self.systemDisk = None
        self.dataDisks = None
        self.autoRenew = None
        self.keyId = None
        self.nic = None
        self.tags = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.zoneId = params.get("zoneId")
        self.instanceName = params.get("instanceName")
        self.instanceType = params.get("instanceType")
        self.cpuCount = params.get("cpuCount")
        self.memory = params.get("memory")
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")
        self.instanceChargeType = params.get("instanceChargeType")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")
        self.internetChargeType = params.get("internetChargeType")
        self.period = params.get("period")
        self.publicIpAddresses = params.get("publicIpAddresses")
        self.publicIpv6Addresses = params.get("publicIpv6Addresses")
        self.privateIpAddresses = params.get("privateIpAddresses")
        self.subnetId = params.get("subnetId")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.instanceStatus = params.get("instanceStatus")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.securityGroupIds = params.get("securityGroupIds")
        if params.get("systemDisk") is not None:
            self.systemDisk = SystemDisk(params.get("systemDisk"))
        if params.get("dataDisks") is not None:
            self.dataDisks = []
            for item in params.get("dataDisks"):
                obj = DataDisk(item)
                self.dataDisks.append(obj)
        self.autoRenew = params.get("autoRenew")
        self.keyId = params.get("keyId")
        if params.get("nic") is not None:
            self.nic = Nic(params.get("nic"))
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


class DescribeInstancesStatusRequest(AbstractModel):
    def __init__(self):
        self.instanceIds = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


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
        self.PENDING = None
        self.DEPLOYING = None
        self.REBUILDING = None
        self.REBOOT = None
        self.RUNNING = None
        self.STOPPED = None
        self.BOOTING = None
        self.RELEASING = None
        self.STOPPING = None
        self.RECYCLE = None
        self.RECYCLING = None
        self.CREATE_FAILED = None
        self.IMAGING = None

    def _deserialize(self, params):
        self.PENDING = params.get("PENDING")
        self.DEPLOYING = params.get("DEPLOYING")
        self.REBUILDING = params.get("REBUILDING")
        self.REBOOT = params.get("REBOOT")
        self.RUNNING = params.get("RUNNING")
        self.STOPPED = params.get("STOPPED")
        self.BOOTING = params.get("BOOTING")
        self.RELEASING = params.get("RELEASING")
        self.STOPPING = params.get("STOPPING")
        self.RECYCLE = params.get("RECYCLE")
        self.RECYCLING = params.get("RECYCLING")
        self.CREATE_FAILED = params.get("CREATE_FAILED")
        self.IMAGING = params.get("IMAGING")


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


class ModifyInstanceTypeRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.instanceTypeId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.instanceTypeId = params.get("instanceTypeId")


class ModifyInstanceTypeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")


class DescribeInstanceTypeStatusRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class DescribeInstanceTypeStatusResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceId = None
        self.instanceName = None
        self.instanceType = None
        self.modifiedInstanceType = None
        self.modifiedInstanceTypeStatus = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.instanceType = params.get("instanceType")
        self.modifiedInstanceType = params.get("modifiedInstanceType")
        self.modifiedInstanceTypeStatus = params.get("modifiedInstanceTypeStatus")


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


class ModifyInstanceBandwidthRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.internetMaxBandwidthOut = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")


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


class CancelInstanceDowngradeRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class CancelInstanceDowngradeResponse(AbstractModel):
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
        self.internetMaxBandwidthOut = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")


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


class DescribeInstanceTrafficRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


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


class DescribeInstanceCpuMonitorRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeInstanceCpuMonitorResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = DescribeInstanceCpuMonitorData(item)
                self.dataList.append(obj)


class DescribeInstanceCpuMonitorData(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cpu = None
        self.time = None

    def _deserialize(self, params):
        self.cpu = params.get("cpu")
        self.time = params.get("time")


class DescribeDiskCategoryRequest(AbstractModel):
    def __init__(self):
        self.instanceChargeType = None
        self.zoneId = None
        self.diskCategory = None

    def _deserialize(self, params):
        self.instanceChargeType = params.get("instanceChargeType")
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
                obj = DiskCategory(item)
                self.categoryZoneSet.append(obj)


class DiskCategory(AbstractModel):
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


class InquiryPriceCreateDisksRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.diskSize = None
        self.diskAmount = None
        self.chargeType = None
        self.chargePrepaid = None
        self.diskCategory = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.diskSize = params.get("diskSize")
        self.diskAmount = params.get("diskAmount")
        self.chargeType = params.get("chargeType")
        if params.get("chargePrepaid") is not None:
            self.chargePrepaid = ChargePrepaid(params.get("chargePrepaid"))
        self.diskCategory = params.get("diskCategory")


class InquiryPriceCreateDisksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataDiskPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataDiskPrice") is not None:
            self.dataDiskPrice = PriceItem(params.get("dataDiskPrice"))


class DescribeDisksRequest(AbstractModel):
    def __init__(self):
        self.diskIds = None
        self.diskName = None
        self.diskStatus = None
        self.diskType = None
        self.diskCategory = None
        self.diskSize = None
        self.portable = None
        self.instanceId = None
        self.zoneId = None
        self.pageNum = None
        self.pageSize = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")
        self.diskName = params.get("diskName")
        self.diskStatus = params.get("diskStatus")
        self.diskType = params.get("diskType")
        self.diskCategory = params.get("diskCategory")
        self.diskSize = params.get("diskSize")
        self.portable = params.get("portable")
        self.instanceId = params.get("instanceId")
        self.zoneId = params.get("zoneId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.resourceGroupId = params.get("resourceGroupId")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


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
        self.zoneId = None
        self.diskType = None
        self.portable = None
        self.diskCategory = None
        self.diskSize = None
        self.diskStatus = None
        self.instanceId = None
        self.instanceName = None
        self.chargeType = None
        self.createTime = None
        self.expiredTime = None
        self.period = None
        self.autoRenew = None
        self.tags = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.diskName = params.get("diskName")
        self.zoneId = params.get("zoneId")
        self.diskType = params.get("diskType")
        self.portable = params.get("portable")
        self.diskCategory = params.get("diskCategory")
        self.diskSize = params.get("diskSize")
        self.diskStatus = params.get("diskStatus")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.chargeType = params.get("chargeType")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.period = params.get("period")
        self.autoRenew = params.get("autoRenew")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))


class CreateDisksRequest(AbstractModel):
    def __init__(self):
        self.chargeType = None
        self.chargePrepaid = None
        self.diskName = None
        self.diskSize = None
        self.diskAmount = None
        self.instanceId = None
        self.zoneId = None
        self.resourceGroupId = None
        self.diskCategory = None
        self.marketingOptions = None
        self.tags = None

    def _deserialize(self, params):
        self.chargeType = params.get("chargeType")
        if params.get("chargePrepaid") is not None:
            self.chargePrepaid = ChargePrepaid(params.get("chargePrepaid"))
        self.diskName = params.get("diskName")
        self.diskSize = params.get("diskSize")
        self.diskAmount = params.get("diskAmount")
        self.instanceId = params.get("instanceId")
        self.zoneId = params.get("zoneId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.diskCategory = params.get("diskCategory")
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


class CreateDisksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.diskIds = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.diskIds = params.get("diskIds")
        self.orderNumber = params.get("orderNumber")


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

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")


class DetachDisksResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ChangeDisksAttachRequest(AbstractModel):
    def __init__(self):
        self.diskIds = None
        self.instanceId = None

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")
        self.instanceId = params.get("instanceId")


class ChangeDisksAttachResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class TerminateDiskRequest(AbstractModel):
    def __init__(self):
        self.diskId = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")


class TerminateDiskResponse(AbstractModel):
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
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")


class DescribeImageQuotaRequest(AbstractModel):
    def __init__(self):
        self.zoneIds = None

    def _deserialize(self, params):
        self.zoneIds = params.get("zoneIds")


class DescribeImageQuotaResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.images = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("images") is not None:
            self.images = []
            for item in params.get("images"):
                obj = ImageQuotaInfo(item)
                self.images.append(obj)


class ImageQuotaInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.count = None
        self.maxCount = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.count = params.get("count")
        self.maxCount = params.get("maxCount")


class DescribeImagesRequest(AbstractModel):
    def __init__(self):
        self.imageIds = None
        self.imageName = None
        self.zoneId = None
        self.category = None
        self.imageType = None
        self.osType = None
        self.imageStatus = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.imageIds = params.get("imageIds")
        self.imageName = params.get("imageName")
        self.zoneId = params.get("zoneId")
        self.category = params.get("category")
        self.imageType = params.get("imageType")
        self.osType = params.get("osType")
        self.imageStatus = params.get("imageStatus")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


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
                obj = ImageInfo(item)
                self.dataSet.append(obj)


class ImageInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.imageId = None
        self.imageName = None
        self.imageType = None
        self.imageSize = None
        self.imageDescription = None
        self.imageVersion = None
        self.imageStatus = None
        self.category = None
        self.osType = None

    def _deserialize(self, params):
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")
        self.imageType = params.get("imageType")
        self.imageSize = params.get("imageSize")
        self.imageDescription = params.get("imageDescription")
        self.imageVersion = params.get("imageVersion")
        self.imageStatus = params.get("imageStatus")
        self.category = params.get("category")
        self.osType = params.get("osType")


class CreateImageRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.imageName = None
        self.imageDescription = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.imageName = params.get("imageName")
        self.imageDescription = params.get("imageDescription")


class CreateImageResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.imageId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.imageId = params.get("imageId")


class ModifyImagesAttributesRequest(AbstractModel):
    def __init__(self):
        self.imageIds = None
        self.imageDescription = None
        self.imageName = None

    def _deserialize(self, params):
        self.imageIds = params.get("imageIds")
        self.imageDescription = params.get("imageDescription")
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

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeSubnetsRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.subnetIds = None
        self.cidrBlock = None
        self.subnetStatus = None
        self.subnetName = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.subnetIds = params.get("subnetIds")
        self.cidrBlock = params.get("cidrBlock")
        self.subnetStatus = params.get("subnetStatus")
        self.subnetName = params.get("subnetName")
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
        self.zoneId = None
        self.subnetName = None
        self.subnetStatus = None
        self.cidrBlockList = None
        self.usageIpCount = None
        self.totalIpCount = None
        self.createTime = None
        self.instanceIdList = None
        self.subnetDescription = None
        self.cidrBlock = None
        self.isDefault = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.zoneId = params.get("zoneId")
        self.subnetName = params.get("subnetName")
        self.subnetStatus = params.get("subnetStatus")
        self.cidrBlockList = params.get("cidrBlockList")
        self.usageIpCount = params.get("usageIpCount")
        self.totalIpCount = params.get("totalIpCount")
        self.createTime = params.get("createTime")
        self.instanceIdList = params.get("instanceIdList")
        self.subnetDescription = params.get("subnetDescription")
        self.cidrBlock = params.get("cidrBlock")
        self.isDefault = params.get("isDefault")


class CreateSubnetRequest(AbstractModel):
    def __init__(self):
        self.cidrBlock = None
        self.subnetName = None
        self.subnetDescription = None
        self.zoneId = None

    def _deserialize(self, params):
        self.cidrBlock = params.get("cidrBlock")
        self.subnetName = params.get("subnetName")
        self.subnetDescription = params.get("subnetDescription")
        self.zoneId = params.get("zoneId")


class CreateSubnetResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.subnetId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.subnetId = params.get("subnetId")


class ModifySubnetsAttributeRequest(AbstractModel):
    def __init__(self):
        self.subnetIds = None
        self.subnetName = None

    def _deserialize(self, params):
        self.subnetIds = params.get("subnetIds")
        self.subnetName = params.get("subnetName")


class ModifySubnetsAttributeResponse(AbstractModel):
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
        self.securityGroupStatus = None
        self.createTime = None
        self.description = None
        self.instanceIds = None
        self.ruleInfos = None
        self.isDefault = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.securityGroupName = params.get("securityGroupName")
        self.securityGroupStatus = params.get("securityGroupStatus")
        self.createTime = params.get("createTime")
        self.description = params.get("description")
        self.instanceIds = params.get("instanceIds")
        if params.get("ruleInfos") is not None:
            self.ruleInfos = []
            for item in params.get("ruleInfos"):
                obj = RuleInfo(item)
                self.ruleInfos.append(obj)
        self.isDefault = params.get("isDefault")


class RuleInfo(AbstractModel):
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
        self.description = None

    def _deserialize(self, params):
        self.direction = params.get("direction")
        self.policy = params.get("policy")
        self.priority = params.get("priority")
        self.ipProtocol = params.get("ipProtocol")
        self.portRange = params.get("portRange")
        self.cidrIp = params.get("cidrIp")
        self.description = params.get("description")


class CreateSecurityGroupRequest(AbstractModel):
    def __init__(self):
        self.securityGroupName = None
        self.ruleInfos = None
        self.description = None

    def _deserialize(self, params):
        self.securityGroupName = params.get("securityGroupName")
        if params.get("ruleInfos") is not None:
            self.ruleInfos = []
            for item in params.get("ruleInfos"):
                obj = RuleInfo(item)
                self.ruleInfos.append(obj)
        self.description = params.get("description")


class CreateSecurityGroupResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.securityGroupId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.securityGroupId = params.get("securityGroupId")


class ModifySecurityGroupsAttributeRequest(AbstractModel):
    def __init__(self):
        self.securityGroupName = None
        self.description = None
        self.securityGroupIds = None

    def _deserialize(self, params):
        self.securityGroupName = params.get("securityGroupName")
        self.description = params.get("description")
        self.securityGroupIds = params.get("securityGroupIds")


class ModifySecurityGroupsAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


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
                obj = RuleInfo(item)
                self.ruleInfos.append(obj)


class ConfigureSecurityGroupRulesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class RevokeSecurityGroupRulesRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None
        self.ruleInfos = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        if params.get("ruleInfos") is not None:
            self.ruleInfos = []
            for item in params.get("ruleInfos"):
                obj = RuleInfo(item)
                self.ruleInfos.append(obj)


class RevokeSecurityGroupRulesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AssociateSecurityGroupInstanceRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None
        self.instanceId = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.instanceId = params.get("instanceId")


class AssociateSecurityGroupInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnAssociateSecurityGroupInstanceRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None
        self.instanceId = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.instanceId = params.get("instanceId")


class UnAssociateSecurityGroupInstanceResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeInstanceAvailableSecurityGroupResourcesRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")


class DescribeInstanceAvailableSecurityGroupResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.instanceAvailableSecurityGroups = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("instanceAvailableSecurityGroups") is not None:
            self.instanceAvailableSecurityGroups = []
            for item in params.get("instanceAvailableSecurityGroups"):
                obj = InstanceAvailableSecurityGroup(item)
                self.instanceAvailableSecurityGroups.append(obj)


class InstanceAvailableSecurityGroup(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.securityGroupId = None
        self.securityGroupName = None
        self.isDefault = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.securityGroupName = params.get("securityGroupName")
        self.isDefault = params.get("isDefault")


class AuthorizeSecurityGroupRulesRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None
        self.ruleInfos = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        if params.get("ruleInfos") is not None:
            self.ruleInfos = []
            for item in params.get("ruleInfos"):
                obj = RuleInfo(item)
                self.ruleInfos.append(obj)


class AuthorizeSecurityGroupRulesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AuthorizeSecurityGroupRuleRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None
        self.direction = None
        self.policy = None
        self.priority = None
        self.ipProtocol = None
        self.portRange = None
        self.cidrIp = None
        self.description = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.direction = params.get("direction")
        self.policy = params.get("policy")
        self.priority = params.get("priority")
        self.ipProtocol = params.get("ipProtocol")
        self.portRange = params.get("portRange")
        self.cidrIp = params.get("cidrIp")
        self.description = params.get("description")


class AuthorizeSecurityGroupRuleResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


