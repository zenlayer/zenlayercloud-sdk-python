#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class CreateInstancesRequest(AbstractModel):
    """CreateInstances请求参数结构体
    """

    def __init__(self):
        self.zoneId = None
        self.instanceChargeType = None
        self.instanceChargePrepaid = None
        self.instanceTypeId = None
        self.imageId = None
        self.ipxeUrl = None
        self.resourceGroupId = None
        self.instanceName = None
        self.hostname = None
        self.amount = None
        self.password = None
        self.sshKeys = None
        self.internetChargeType = None
        self.internetMaxBandwidthOut = None
        self.trafficPackageSize = None
        self.subnetId = None
        self.raidConfig = None
        self.partitions = None
        self.nic = None
        self.clusterId = None
        self.enablePrimaryIPv6 = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceChargeType = params.get("instanceChargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.instanceTypeId = params.get("instanceTypeId")
        self.imageId = params.get("imageId")
        self.ipxeUrl = params.get("ipxeUrl")
        self.resourceGroupId = params.get("imageId")
        self.instanceName = params.get("instanceName")
        self.hostname = params.get("hostname")
        self.amount = params.get("amount")
        self.password = params.get("password")
        self.sshKeys = params.get("sshKeys")
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
        self.clusterId = params.get("clusterId")
        self.enablePrimaryIPv6 = params.get("enablePrimaryIPv6")


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回参数结构体
    """

    def __init__(self):
        self.instanceIdSet = None
        self.requestId = None

    def _deserialize(self, params):
        self.instanceIdSet = params.get("instanceIdSet")
        self.requestId = params.get("requestId")


class ChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self, params=None):
        """
        :param period: 购买实例的时长，单位：月。
        :type period: int
        """
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.period = None

    def _deserialize(self, params):
        self.period = params.get("period")


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

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.zoneName = params.get("zoneName")
        self.cityName = params.get("cityName")
        self.areaName = params.get("areaName")


class RaidConfig(AbstractModel):
    """描述了Raid的配置信息

    """

    def __init__(self, params=None):
        r"""
        :param raidType: Raid类型。
该配置进行快捷raid配置，支持0, 1, 5, 10。
raidType和customRaids只能指定其中一个参数。
        :type raidType: int
        :param customRaids: 自定义Raid配置。
自定义磁盘进行raid的配置。
raidType和customRaids只能指定其中一个参数。
        :type customRaids: list of CustomRaid
        """
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
    """进行自定义Raid配置时需要的raid级别和指定的磁盘序号。


    """

    def __init__(self, params=None):
        r"""
         :param raidType: Raid类型。
 支持0, 1, 5, 10。
         :type raidType: int
         :param diskSequence: 磁盘序号。
 根据机型里的磁盘从1开始顺序编号。如果是多个磁盘序号，则必须连续。
         :type diskSequence: list of int
         """
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
    """分区配置信息。包括文件类型, 分区大小等。


    """

    def __init__(self, params=None):
        r"""

        :param fsType: 分区的文件类型。
linux系统：支持的值ext2,ext3, ext4, ext类型必须要有。
windows系统: 只能为NTFS。
        :type fsType: int
        :param fsPath: 分区盘符。
linux系统：必须为/开头，且第一个为系统分区必须为/。
windows系统：支持C~H，第一个系统分区必须指定为C。
        :type fsPath: str
        :param size: 分区大小。
单位为GB。
        :type size: str
        """
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.fsType = None
        self.fsPath = None
        self.size = None

    def _deserialize(self, params):
        self.fsType = params.get("fsType")
        self.fsPath = params.get("fsPath")
        self.size = params.get("size")


class Nic(AbstractModel):
    """分区配置信息。包括文件类型, 分区大小等。


    """

    def __init__(self, params=None):
        r"""

        :param wanName: 公网网卡名称。
只能是数字和大小写字母，且必须以字母开头，长度限制为4-10。
非高可用机型，默认的公网网卡名称为wan0。且不能为lan开头。
高可用机型，默认的公网网卡名称为bond0。
公网名称和内网名称不能相同。
        :type wanName: str
        :param lanName: 内网网卡名称。
只能是数字和大小写字母，且必须以字母开头，长度限制为4-10。
非高可用机型，默认的内网网卡名称为lan0。且不能为wan开头。
高可用机型，默认的内网网卡名称为bond1。
公网名称和内网名称不能相同。
        :type lanName: str
        """
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


class DescribeZonesRequest(AbstractModel):
    def __init__(self):
        self.acceptLanguage = None

    def _deserialize(self, params):
        self.acceptLanguage = params.get("acceptLanguage")


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
        self.pageSize = None
        self.pageNum = None

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
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


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
        self.publicIpAddresses = None
        self.privateIpAddresses = None
        self.ipv6Addresses = None
        self.subnetIds = None
        self.createTime = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.instanceStatus = None
        self.primaryPublicIpAddress = None
        self.trafficPackageSize = None
        self.raidConfig = None
        self.partitions = None
        self.nic = None
        self.autoRenew = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.zoneId = params.get("zoneId")
        self.instanceName = params.get("instanceName")
        self.hostname = params.get("hostname")
        self.instanceTypeId = params.get("instanceTypeId")
        self.instanceType = InstanceType(params.get("instanceType"))
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")
        self.ipxeUrl = params.get("ipxeUrl")
        self.instanceChargeType = params.get("instanceChargeType")
        self.bandwidthOutMbps = params.get("bandwidthOutMbps")
        self.internetChargeType = params.get("internetChargeType")
        self.period = params.get("period")
        self.publicIpAddresses = params.get("publicIpAddresses")
        self.privateIpAddresses = params.get("privateIpAddresses")
        self.ipv6Addresses = params.get("ipv6Addresses")
        self.subnetIds = params.get("subnetIds")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.instanceStatus = params.get("instanceStatus")
        self.primaryPublicIpAddress = params.get("primaryPublicIpAddress")
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
        self.instanceId = None
        self.imageId = None
        self.ipxeUrl = None
        self.hostname = None
        self.password = None
        self.sshKeys = None
        self.raidConfig = None
        self.partitions = None
        self.nic = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.imageId = params.get("imageId")
        self.ipxeUrl = params.get("ipxeUrl")
        self.hostname = params.get("hostname")
        self.password = params.get("password")
        self.sshKeys = params.get("sshKeys")
        if params.get("raidConfig") is not None:
            self.raidConfig = RaidConfig(params.get("raidConfig"))
        if params.get("partitions") is not None:
            self.partitions = []
            for item in params.get("partitions"):
                obj = Partition(item)
                self.partitions.append(obj)
        if params.get("nic") is not None:
            self.nic = Nic(params.get("nic"))


class ReinstallInstanceResponse(AbstractModel):

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


class InquiryPriceCreateInstanceRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.instanceTypeId = None
        self.instanceChargeType = None
        self.internetChargeType = None
        self.instanceChargePrepaid = None
        self.trafficPackageSize = None
        self.internetMaxBandwidthOut = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceTypeId = params.get("instanceTypeId")
        self.instanceChargeType = params.get("instanceChargeType")
        self.internetChargeType = params.get("internetChargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")


class InquiryPriceCreateInstanceResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.instancePrice = None
        self.bandwidthPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("instancePrice") is not None:
            self.instancePrice = Price(params.get("instancePrice"))
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = []
            for item in params.get("bandwidthPrice"):
                obj = Price(item)
                self.bandwidthPrice.append(obj)


class Price(AbstractModel):

    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.originalPrice = None
        self.discountPrice = None
        self.discount = None
        self.unitPrice = None
        self.discountUnitPrice = None
        self.chargeUnit = None
        self.stepPrices = None

    def _deserialize(self, params):
        self.originalPrice = params.get("originalPrice")
        self.discountPrice = params.get("discountPrice")
        self.discount = params.get("discount")
        self.unitPrice = params.get("unitPrice")
        self.discountUnitPrice = params.get("discountUnitPrice")
        self.chargeUnit = params.get("chargeUnit")
        if params.get("stepPrices") is not None:
            self.stepPrices = []
            for item in params.get("stepPrices"):
                obj = StepPrice(item)
                self.stepPrices.append(obj)


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


class DescribeInstanceTypesRequest(AbstractModel):

    def __init__(self):
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
        self.imageId = None

    def _deserialize(self, params):
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
        self.imageId = params.get("imageId")


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
        self.instanceTypeId = None
        self.description = None
        self.cpuCoreCount = None
        self.memorySize = None
        self.supportRaids = None
        self.supportSubnet = None
        self.maximumBandwidth = None
        self.diskInfo = None
        self.imageIds = None
        self.isHA = None

    def _deserialize(self, params):
        self.instanceTypeId = params.get("instanceTypeId")
        self.description = params.get("description")
        self.cpuCoreCount = params.get("cpuCoreCount")
        self.memorySize = params.get("memorySize")
        self.supportRaids = params.get("supportRaids")
        self.supportSubnet = params.get("supportSubnet")
        self.maximumBandwidth = params.get("maximumBandwidth")
        if params.get("diskInfo") is not None:
            self.diskInfo = InstanceDiskInfo(params.get("diskInfo"))
        self.imageIds = params.get("imageIds")
        self.isHA = params.get("isHA")


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
        self.zoneId = None
        self.instanceTypeId = None
        self.sellStatus = None

    def _deserialize(self, params):
        self.instanceChargeType = params.get("instanceChargeType")
        self.zoneId = params.get("zoneId")
        self.instanceTypeId = params.get("instanceTypeId")
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
                obj = Price(item)
                self.bandwidthPrice.append(obj)


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
                obj = Price(item)
                self.trafficPackagePrice.append(obj)


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
        self.maxBandwidth95ValueMbps = None
        self.out95 = None
        self.out95Time = None
        self.outAvg = None
        self.outMax = None
        self.outMin = None
        self.outTotal = None
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
        self.maxBandwidth95ValueMbps = params.get("maxBandwidth95ValueMbps")
        self.out95 = params.get("out95")
        self.out95Time = params.get("out95Time")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.outTotal = params.get("outTotal")
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
        self.serverBrand = None
        self.serverModel = None
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
        self.serverBrand = params.get("serverBrand")
        self.serverModel = params.get("serverModel")
        self.fanStatus = params.get("fanStatus")
        self.serverBrand = params.get("serverBrand")
        self.serverModel = params.get("serverModel")
        self.cpuTemp = params.get("cpuTemp")
        self.cpu0Temp = params.get("cpu0Temp")
        self.cpu1Temp = params.get("cpu1Temp")
        self.cpu2Temp = params.get("cpu2Temp")
        self.inletTemp = params.get("inletTemp")
        self.tempUnit = params.get("tempUnit")

class DescribeEipAddressesRequest(AbstractModel):

    def __init__(self):
        self.eipChargeType = None
        self.eipIds = None
        self.eipStatus = None
        self.instanceId = None
        self.instanceName = None
        self.ipAddress = None
        self.zoneId = None
        self.resourceGroupId = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.eipChargeType = params.get("eipChargeType")
        self.eipIds = params.get("eipIds")
        self.eipStatus = params.get("eipStatus")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.ipAddress = params.get("ipAddress")
        self.zoneId = params.get("zoneId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


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
        self.instanceId = None
        self.instanceName = None
        self.eipChargeType = None
        self.period = None
        self.createTime = None
        self.expiredTime = None
        self.eipStatus = None
        self.resourceGroupId = None
        self.resourceGroupName = None

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.zoneId = params.get("zoneId")
        self.ipAddress = params.get("ipAddress")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.eipChargeType = params.get("eipChargeType")
        self.period = params.get("period")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.eipStatus = params.get("eipStatus")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")


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

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.status = params.get("status")


class AllocateEipAddressesRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.eipChargeType = None
        self.eipChargePrepaid = None
        self.amount = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.eipChargeType = params.get("eipChargeType")
        if params.get("eipChargePrepaid") is not None:
            self.eipChargePrepaid = ChargePrepaid(params.get("eipChargePrepaid"))
        self.amount = params.get("amount")
        self.resourceGroupId = params.get("resourceGroupId")


class AllocateEipAddressesResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.eipIdSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.eipIdSet = params.get("eipIdSet")


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


class InquiryPriceCreateEipAddressRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.eipChargeType = None
        self.eipChargePrepaid = None
        self.amount = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.eipChargeType = params.get("eipChargeType")
        if params.get("eipChargePrepaid") is not None:
            self.eipChargePrepaid = ChargePrepaid(params.get("eipChargePrepaid"))
        self.amount = params.get("amount")


class InquiryPriceCreateEipAddressResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.eipPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("eipPrice") is not None:
            self.eipPrice = Price(params.get("eipPrice"))


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

    def _deserialize(self, params):
        self.eipId = params.get("eipId")
        self.ipAddress = params.get("ipAddress")


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
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.cidrBlockIds = params.get("cidrBlockIds")
        self.cidrBlock = params.get("cidrBlock")
        self.cidrBlockName = params.get("cidrBlockName")
        self.zoneId = params.get("zoneId")
        self.cidrBlockType = params.get("cidrBlockType")
        self.gateway = params.get("gateway")
        self.chargeType = params.get("chargeType")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


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

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")
        self.cidrBlockType = params.get("cidrBlockType")
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


class DescribeCidrBlockIpsRequest(AbstractModel):

    def __init__(self):
        self.cidrBlockId = None
        self.instanceId = None
        self.ip = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")
        self.instanceId = params.get("instanceId")
        self.ip = params.get("ip")


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

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.netmask = params.get("netmask")
        self.sellStatus = params.get("sellStatus")


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
        self.cidrBlockIpType = None
        self.cidrBlock = None
        self.availableIps = None
        self.availableIpCount = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")
        self.zoneId = params.get("zoneId")
        self.cidrBlockIpType = params.get("cidrBlockIpType")
        self.cidrBlock = params.get("cidrBlock")
        self.availableIps = params.get("availableIps")
        self.availableIpCount = params.get("availableIpCount")


class InquiryPriceCreateIpv4BlockRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.chargeType = None
        self.chargePrepaid = None
        self.netmask = None
        self.amount = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.chargeType = params.get("chargeType")
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
            self.price = Price(params.get("price"))


class CreateIpv4BlockRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.name = None
        self.chargeType = None
        self.chargePrepaid = None
        self.netmask = None
        self.amount = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.name = params.get("name")
        self.chargeType = params.get("chargeType")
        if params.get("chargePrepaid") is not None:
            self.chargePrepaid = ChargePrepaid(params.get("chargePrepaid"))
        self.netmask = params.get("netmask")
        self.amount = params.get("amount")
        self.resourceGroupId = params.get("resourceGroupId")


class CreateIpv4BlockResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.cidrBlockIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.cidrBlockIds = params.get("cidrBlockIds")


class CreateIpv6BlockRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.name = None
        self.amount = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.name = params.get("name")
        self.amount = params.get("amount")
        self.resourceGroupId = params.get("resourceGroupId")


class CreateIpv6BlockResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.cidrBlockIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.cidrBlockIds = params.get("cidrBlockIds")


class ModifyCidrBlocksAttributeRequest(AbstractModel):

    def __init__(self):
        self.cidrBlockIds = None
        self.name = None

    def _deserialize(self, params):
        self.cidrBlockIds = params.get("cidrBlockIds")
        self.name = params.get("name")


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


class BindCidrBlockIpsRequest(AbstractModel):

    def __init__(self):
        self.cidrBlockId = None
        self.ipBindList = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")
        if params.get("ipBindList") is not None:
            self.ipBindList = []
            for item in params.get("ipBindList"):
                obj = IpBindParam(item)
                self.ipBindList.append(obj)


class BindCidrBlockIpsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


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


class UnbindCidrBlockIpsRequest(AbstractModel):

    def __init__(self):
        self.cidrBlockId = None
        self.ipList = None

    def _deserialize(self, params):
        self.cidrBlockId = params.get("cidrBlockId")
        self.ipList = params.get("ipList")


class UnbindCidrBlockIpsResponse(AbstractModel):

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


class ModifyVpcsAttributeRequest(AbstractModel):

    def __init__(self):
        self.vpcIds = None
        self.vpcName = None

    def _deserialize(self, params):
        self.vpcIds = params.get("vpcIds")
        self.vpcName = params.get("vpcName")


class ModifyVpcsAttributeResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeVpcsRequest(AbstractModel):

    def __init__(self):
        self.vpcIds = None
        self.cidrBlock = None
        self.vpcStatus = None
        self.vpcName = None
        self.vpcRegionId = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.vpcIds = params.get("vpcIds")
        self.cidrBlock = params.get("cidrBlock")
        self.vpcStatus = params.get("vpcStatus")
        self.vpcName = params.get("vpcName")
        self.vpcRegionId = params.get("vpcRegionId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


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
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.vpcStatus = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.vpcRegionId = params.get("vpcRegionId")
        self.vpcRegionName = params.get("vpcRegionName")
        self.vpcName = params.get("vpcName")
        self.cidrBlock = params.get("cidrBlock")
        self.createTime = params.get("createTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.vpcStatus = params.get("vpcStatus")


class CreateVpcRequest(AbstractModel):

    def __init__(self):
        self.vpcRegionId = None
        self.cidrBlock = None
        self.vpcName = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.vpcRegionId = params.get("vpcRegionId")
        self.cidrBlock = params.get("cidrBlock")
        self.vpcName = params.get("vpcName")
        self.resourceGroupId = params.get("resourceGroupId")


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


class DescribeSubnetsRequest(AbstractModel):

    def __init__(self):
        self.subnetIds = None
        self.cidrBlock = None
        self.zoneId = None
        self.subnetStatus = None
        self.subnetName = None
        self.resourceGroupId = None
        self.vpcId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.subnetIds = params.get("subnetIds")
        self.cidrBlock = params.get("cidrBlock")
        self.zoneId = params.get("zoneId")
        self.subnetStatus = params.get("subnetStatus")
        self.subnetName = params.get("subnetName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.vpcId = params.get("vpcId")
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


class AssociateSubnetInstancesResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


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
