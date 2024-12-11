#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeInstanceMonitorDataRequest(AbstractModel):
    def __init__(self):
        self.instanceId = None
        self.metricType = None
        self.ipAddress = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.metricType = params.get("metricType")
        self.ipAddress = params.get("ipAddress")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeInstanceMonitorDataResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.maxValue = None
        self.avgValue = None
        self.dataList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.maxValue = params.get("maxValue")
        self.avgValue = params.get("avgValue")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = MetricValue(item)
                self.dataList.append(obj)


class MetricValue(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.value = None
        self.timeInSecond = None

    def _deserialize(self, params):
        self.value = params.get("value")
        self.timeInSecond = params.get("timeInSecond")


class CreateVpcRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.cidrBlock = None
        self.mtu = None
        self.enablePriIpv6 = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.mtu = params.get("mtu")
        self.enablePriIpv6 = params.get("enablePriIpv6")
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


class DescribeVpcsRequest(AbstractModel):

    def __init__(self):
        self.vpcIds = None
        self.name = None
        self.cidrBlock = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.vpcIds = params.get("vpcIds")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
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
        self.name = None
        self.cidrBlock = None
        self.ipv6CidrBlock = None
        self.mtu = None
        self.isDefault = None
        self.createTime = None
        self.usageIpv4Count = None
        self.usageIpv6Count = None
        self.securityGroupId = None

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
        self.regionId = None
        self.stackType = None
        self.ipv6Type = None
        self.name = None
        self.cidrBlock = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.regionId = params.get("regionId")
        self.stackType = params.get("stackType")
        self.ipv6Type = params.get("ipv6Type")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")


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


class DescribeSubnetsRequest(AbstractModel):

    def __init__(self):
        self.subnetIds = None
        self.name = None
        self.cidrBlock = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.subnetIds = params.get("subnetIds")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
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
        self.regionId = None
        self.name = None
        self.cidrBlock = None
        self.ipv6CidrBlock = None
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
        self.ipv6CidrBlock = params.get("ipv6CidrBlock")
        self.stackType = params.get("stackType")
        self.ipv6Type = params.get("ipv6Type")
        self.vpcId = params.get("vpcId")
        self.vpcName = params.get("vpcName")
        self.usageIpv4Count = params.get("usageIpv4Count")
        self.usageIpv6Count = params.get("usageIpv6Count")
        self.createTime = params.get("createTime")
        self.isDefault = params.get("isDefault")


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


class CreateRouteRequest(AbstractModel):

    def __init__(self):
        self.vpcId = None
        self.ipVersion = None
        self.cidrBlock = None
        self.priority = None
        self.nextHotId = None
        self.name = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.ipVersion = params.get("ipVersion")
        self.cidrBlock = params.get("cidrBlock")
        self.priority = params.get("priority")
        self.nextHotId = params.get("nextHotId")
        self.name = params.get("name")


class CreateRouteResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.routeId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.routeId = params.get("routeId")


class DeleteRouteRequest(AbstractModel):

    def __init__(self):
        self.vpcId = None
        self.routeId = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.routeId = params.get("routeId")


class DeleteRouteResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeRoutesRequest(AbstractModel):

    def __init__(self):
        self.routeIds = None
        self.ipVersion = None
        self.type = None
        self.name = None
        self.cidrBlock = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.routeIds = params.get("routeIds")
        self.ipVersion = params.get("ipVersion")
        self.type = params.get("type")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
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
        self.cidrBlock = params.get("cidrBlock")
        self.priority = params.get("priority")
        self.nextHopId = params.get("nextHopId")
        self.nextHopName = params.get("nextHopName")
        self.nextHopType = params.get("nextHopType")
        self.createTime = params.get("createTime")


class DescribeInstancesRequest(AbstractModel):

    def __init__(self):
        self.instanceIds = None
        self.zoneId = None
        self.imageId = None
        self.status = None
        self.name = None
        self.ipv4Address = None
        self.ipv6Address = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.zoneId = params.get("zoneId")
        self.imageId = params.get("imageId")
        self.status = params.get("status")
        self.name = params.get("name")
        self.ipv4Address = params.get("ipv4Address")
        self.ipv6Address = params.get("ipv6Address")
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
        self.instanceName = None
        self.zoneId = None
        self.cpu = None
        self.memory = None
        self.imageId = None
        self.imageName = None
        self.status = None
        self.systemDisk = None
        self.dataDisks = None
        self.publicIpAddresses = None
        self.privateIpAddresses = None
        self.keyId = None
        self.createTime = None
        self.expiredTime = None
        self.resourceGroupId = None
        self.resourceGroupName = None


    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.zoneId = params.get("zoneId")
        self.cpu = params.get("cpu")
        self.memory = params.get("memory")
        self.imageId = params.get("imageId")
        self.imageName = params.get("imageName")
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
        self.period = params.get("period")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")

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
        self.instanceId = None
        self.instanceStatus = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.instanceStatus = params.get("instanceStatus")



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


class ResetInstanceRequest(AbstractModel):

    def __init__(self):
        self.instanceId = None
        self.imageId = None
        self.password = None
        self.keyId = None
        self.timezone = None
        self.enableAgent = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.imageId = params.get("imageId")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.timezone = params.get("timezone")
        self.enableAgent = params.get("enableAgent")

class ResetInstanceResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


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
        self.forceShutdown = None

    def _deserialize(self, params):
        self.instanceIds = params.get("instanceIds")
        self.forceShutdown = params.get("forceShutdown")


class StopInstancesResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class DescribeCidrsRequest(AbstractModel):

    def __init__(self):
        self.cidrIds = None
        self.regionId = None
        self.name = None
        self.cidrBlock = None
        self.source = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.cidrIds = params.get("cidrIds")
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.source = params.get("source")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


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
        self.networkType = None
        self.netmask = None
        self.createTime = None
        self.expiredTime = None
        self.period = None
        self.instanceChargeType = None
        self.resourceGroupId = None
        self.resourceGroupName = None


    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")
        self.regionId = params.get("regionId")
        self.name = params.get("name")
        self.cidrBlock = params.get("cidrBlock")
        self.totalCount = params.get("totalCount")
        self.usedCount = params.get("usedCount")
        self.source = params.get("source")
        self.networkType = params.get("networkType")
        self.netmask = params.get("netmask")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.period = params.get("period")
        self.instanceChargeType = params.get("instanceChargeType")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")


class DescribeCidrRegionsRequest(AbstractModel):

    def __init__(self):
        self.instanceChargeType = None

    def _deserialize(self, params):
        self.instanceChargeType = params.get("instanceChargeType")


class DescribeCidrRegionsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")


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
        self.excessUnitPrice = None
        self.excessDiscountUnitPrice = None
        self.excessAmountUnit = None
        self.stepPrices = None

    def _deserialize(self, params):
        self.originalPrice = params.get("originalPrice")
        self.discountPrice = params.get("discountPrice")
        self.discount = params.get("discount")
        self.unitPrice = params.get("unitPrice")
        self.discountUnitPrice = params.get("discountUnitPrice")
        self.chargeUnit = params.get("chargeUnit")
        self.excessUnitPrice = params.get("excessUnitPrice")
        self.excessDiscountUnitPrice = params.get("excessDiscountUnitPrice")
        self.excessAmountUnit = params.get("excessAmountUnit")
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


class DescribeOwnCidrPriceRequest(AbstractModel):

    def __init__(self):
        self.regionId = None
        self.chargeType = None
        self.instanceChargePrepaid = None
        self.networkType = None
        self.cidrBlock = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.chargeType = params.get("chargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.networkType = params.get("networkType")
        self.cidrBlock = params.get("cidrBlock")


class DescribeOwnCidrPriceResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.bandwidthPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = Price(params.get("bandwidthPrice"))



class NetmaskInfo(AbstractModel):

    def __init__(self, params=None):
        """
        """
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


class DescribeCidrPriceRequest(AbstractModel):

    def __init__(self):
        self.regionId = None
        self.chargeType = None
        self.instanceChargePrepaid = None
        self.networkType = None
        self.netmask = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.chargeType = params.get("chargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.networkType = params.get("networkType")
        if params.get("netmask") is not None:
            self.netmask = NetmaskInfo(params.get("netmask"))


class DescribeCidrPriceResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.bandwidthPrice = None
        self.cidrPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = Price(params.get("bandwidthPrice"))
        if params.get("cidrPrice") is not None:
            self.cidrPrice = Price(params.get("cidrPrice"))


class DescribeCidrUsedIpsRequest(AbstractModel):

    def __init__(self):
        self.cidrId = None
        self.publicIp = None
        self.instanceId = None
        self.instanceName = None
        self.nicId = None
        self.nicName = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")
        self.publicIp = params.get("publicIp")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.nicId = params.get("nicId")
        self.nicName = params.get("nicName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeCidrUsedIpsResponse(AbstractModel):

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
                obj = CidrUsedIpInfo(item)
                self.dataSet.append(obj)


class CidrUsedIpInfo(AbstractModel):

    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.publicIp = None
        self.lanIp = None
        self.nicId = None
        self.nicName = None
        self.instanceId = None
        self.instanceName = None


    def _deserialize(self, params):
        self.publicIp = params.get("publicIp")
        self.lanIp = params.get("lanIp")
        self.nicId = params.get("nicId")
        self.nicName = params.get("nicName")
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")


class CreateOwnCidrRequest(AbstractModel):

    def __init__(self):
        self.regionId = None
        self.chargeType = None
        self.resourceGroupId = None
        self.instanceChargePrepaid = None
        self.networkType = None
        self.cidrBlock = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.chargeType = params.get("chargeType")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.networkType = params.get("networkType")
        self.cidrBlock = params.get("cidrBlock")


class CreateOwnCidrResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class CreateCidrRequest(AbstractModel):

    def __init__(self):
        self.regionId = None
        self.chargeType = None
        self.resourceGroupId = None
        self.instanceChargePrepaid = None
        self.networkType = None
        self.netmask = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.chargeType = params.get("chargeType")
        self.resourceGroupId = params.get("resourceGroupId")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = ChargePrepaid(params.get("instanceChargePrepaid"))
        self.networkType = params.get("networkType")
        if params.get("netmask") is not None:
            self.netmask = NetmaskInfo(params.get("netmask"))


class CreateCidrResponse(AbstractModel):

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



class UnAssignCidrIpRequest(AbstractModel):

    def __init__(self):
        self.cidrId = None
        self.publicIp = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")
        self.publicIp = params.get("publicIp")


class UnAssignCidrIpResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AssignCidrIpRequest(AbstractModel):

    def __init__(self):
        self.cidrId = None
        self.nicId = None
        self.publicIp = None
        self.lanIp = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")
        self.nicId = params.get("nicId")
        self.publicIp = params.get("publicIp")
        self.lanIp = params.get("lanIp")


class AssignCidrIpResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class BatchAssignCidrIpRequest(AbstractModel):

    def __init__(self):
        self.cidrId = None
        self.cidrIpBinds = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")
        if params.get("cidrIpBinds") is not None:
            self.cidrIpBinds = []
            for item in params.get("cidrIpBinds"):
                obj = CidrIpBind(item)
                self.cidrIpBinds.append(obj)


class CidrIpBind(AbstractModel):

    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.nicId = None
        self.publicIp = None
        self.lanIp = None


    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.publicIp = params.get("publicIp")
        self.lanIp = params.get("lanIp")


class BatchAssignCidrIpResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AvailableCidrIpRequest(AbstractModel):

    def __init__(self):
        self.cidrId = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")


class AvailableCidrIpResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.ips = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.ips = params.get("ips")


class ConfigEgressIpRequest(AbstractModel):

    def __init__(self):
        self.cidrId = None
        self.publicIp = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")
        self.publicIp = params.get("publicIp")


class ConfigEgressIpResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class DescribeOwnCidrsRequest(AbstractModel):

    def __init__(self):
        self.regionId = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")


class DescribeOwnCidrsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.cidrs = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("cidrs") is not None:
            self.cidrs = []
            for item in params.get("cidrs"):
                obj = OwnCidr(item)
                self.cidrs.append(obj)


class OwnCidr(AbstractModel):

    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.cidrBlock = None
        self.ipNum = None
        self.networkType = None


    def _deserialize(self, params):
        self.cidrBlock = params.get("cidrBlock")
        self.ipNum = params.get("ipNum")
        self.networkType = params.get("networkType")



class AvailableLanIpRequest(AbstractModel):

    def __init__(self):
        self.cidrId = None

    def _deserialize(self, params):
        self.cidrId = params.get("cidrId")


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



class DescribeDiskRegionsRequest(AbstractModel):

    def __init__(self):
        self.chargeType = None

    def _deserialize(self, params):
        self.chargeType = params.get("chargeType")


class DescribeDiskRegionsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")



class CreateDisksRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.diskName = None
        self.diskSize = None
        self.diskAmount = None
        self.instanceId = None
        self.resourceGroupId = None
        self.diskCategory = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.diskName = params.get("diskName")
        self.diskSize = params.get("diskSize")
        self.diskAmount = params.get("diskAmount")
        self.instanceId = params.get("instanceId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.diskCategory = params.get("diskCategory")


class CreateDisksResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.diskIds = None
        self.orderNumber = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.diskIds = params.get("diskIds")
        self.orderNumber = params.get("orderNumber")



class DescribeDisksRequest(AbstractModel):

    def __init__(self):
        self.diskIds = None
        self.diskName = None
        self.diskStatus = None
        self.diskType = None
        self.diskCategory = None
        self.instanceId = None
        self.zoneId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.diskIds = params.get("diskIds")
        self.diskName = params.get("diskName")
        self.diskStatus = params.get("diskStatus")
        self.diskType = params.get("diskType")
        self.diskCategory = params.get("diskCategory")
        self.instanceId = params.get("instanceId")
        self.zoneId = params.get("zoneId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


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
        self.resourceGroupId = None
        self.resourceGroupName = None


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
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")



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
            self.dataDiskPrice = Price(params.get("dataDiskPrice"))


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


    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.securityGroupName = params.get("securityGroupName")
        self.scope = params.get("scope")
        self.createTime = params.get("createTime")
        self.vpcIds = params.get("vpcIds")
        self.isDefault = params.get("isDefault")



class ModifySecurityGroupsAttributeRequest(AbstractModel):

    def __init__(self):
        self.securityGroupIds = None
        self.securityGroupName = None

    def _deserialize(self, params):
        self.securityGroupIds = params.get("securityGroupIds")
        self.securityGroupName = params.get("securityGroupName")


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
                obj = RuleInfo(item)
                self.ingressRuleList.append(obj)
        if params.get("egressRuleList") is not None:
            self.egressRuleList = []
            for item in params.get("egressRuleList"):
                obj = RuleInfo(item)
                self.egressRuleList.append(obj)


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
        self.securityGroupName = None
        self.ruleInfos = None

    def _deserialize(self, params):
        self.securityGroupName = params.get("securityGroupName")
        if params.get("ruleInfos") is not None:
            self.ruleInfos = []
            for item in params.get("ruleInfos"):
                obj = RuleInfo(item)
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
                obj = RuleInfo(item)
                self.ruleInfos.append(obj)

class ConfigureSecurityGroupRulesResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class AssignSecurityGroupVpcRequest(AbstractModel):

    def __init__(self):
        self.securityGroupId = None
        self.vpcId = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.vpcId = params.get("vpcId")


class AssignSecurityGroupVpcResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnAssignSecurityGroupVpcRequest(AbstractModel):

    def __init__(self):
        self.securityGroupId = None
        self.vpcId = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.vpcId = params.get("vpcId")


class UnAssignSecurityGroupVpcResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class DescribeNicsRequest(AbstractModel):

    def __init__(self):
        self.nicIds = None
        self.name = None
        self.regionId = None
        self.vpcId = None
        self.subnetId = None
        self.status = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.nicIds = params.get("nicIds")
        self.name = params.get("name")
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.subnetId = params.get("subnetId")
        self.status = params.get("status")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeNicsResponse(AbstractModel):

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
        self.instanceId = None
        self.vpcId = None
        self.subnetId = None
        self.createTime = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.name = params.get("name")
        self.status = params.get("status")
        self.nicType = params.get("nicType")
        self.regionId = params.get("regionId")
        self.nicSubnetType = params.get("nicSubnetType")
        self.publicIpList = params.get("publicIpList")
        self.privateIpList = params.get("privateIpList")
        self.instanceId = params.get("instanceId")
        self.vpcId = params.get("vpcId")
        self.subnetId = params.get("subnetId")
        self.createTime = params.get("createTime")



class ModifyNicsAttributeRequest(AbstractModel):

    def __init__(self):
        self.nicIds = None
        self.name = None

    def _deserialize(self, params):
        self.nicIds = params.get("nicIds")
        self.name = params.get("name")


class ModifyNicsAttributeResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class CreateNicRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.subnetId = None
        self.packageSize = None
        self.internetChargeType = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.subnetId = params.get("subnetId")
        self.packageSize = params.get("packageSize")
        self.internetChargeType = params.get("internetChargeType")
        self.resourceGroupId = params.get("resourceGroupId")


class CreateNicResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class DeleteNicRequest(AbstractModel):
    def __init__(self):
        self.nicId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")


class DeleteNicResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AttachNicRequest(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.instanceId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.instanceId = params.get("instanceId")


class AttachNicResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AssignNicIpv6Request(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.internetChargeType = None
        self.packageSize = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.internetChargeType = params.get("internetChargeType")
        self.packageSize = params.get("packageSize")


class AssignNicIpv6Response(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class UnAssignNicIpv4Request(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.ipAddress = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.ipAddress = params.get("ipAddress")


class UnAssignNicIpv4Response(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")



class AssignNicIpv4Request(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.ipAddress = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.ipAddress = params.get("ipAddress")


class AssignNicIpv4Response(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class BatchAssignNicIpv4Request(AbstractModel):
    def __init__(self):
        self.nicId = None
        self.ipAddresses = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")
        self.ipAddresses = params.get("ipAddresses")


class BatchAssignNicIpv4Response(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")

class DetachNicRequest(AbstractModel):
    def __init__(self):
        self.nicId = None

    def _deserialize(self, params):
        self.nicId = params.get("nicId")


class DetachNicResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeNicRegionsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.regionIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.regionIds = params.get("regionIds")



class InquiryPricePublicIpv6Request(AbstractModel):

    def __init__(self):
        self.regionId = None
        self.packageSize = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.packageSize = params.get("packageSize")


class InquiryPricePublicIpv6Response(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.bandwidthPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("bandwidthPrice") is not None:
            self.bandwidthPrice = Price(params.get("bandwidthPrice"))



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
        self.diskSize = None
        self.diskName = None
        self.diskCategory = None
        self.portable = None
        self.diskAmount = None

    def _deserialize(self, params):
        self.diskId = params.get("diskId")
        self.diskSize = params.get("diskSize")
        self.diskName = params.get("diskName")
        self.diskCategory = params.get("diskCategory")
        self.portable = params.get("portable")
        self.diskAmount = params.get("diskAmount")

class CreateZecInstancesRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.instanceType = None
        self.imageId = None
        self.resourceGroupId = None
        self.instanceName = None
        self.instanceCount = None
        self.password = None
        self.keyId = None
        self.internetChargeType = None
        self.trafficPackageSize = None
        self.subnetId = None
        self.systemDisk = None
        self.dataDisks = None
        self.timeZone = None
        self.enableAgent = None
        self.enableIpForward = None
        self.eipV4Type = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceType = params.get("instanceType")
        self.imageId = params.get("imageId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.instanceName = params.get("instanceName")
        self.instanceCount = params.get("instanceCount")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.internetChargeType = params.get("internetChargeType")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.subnetId = params.get("subnetId")
        if params.get("systemDisk") is not None:
            self.systemDisk = SystemDisk(params.get("systemDisk"))
        if params.get("dataDisks") is not None:
            self.dataDisks = []
            for item in params.get("dataDisks"):
                obj = DataDisk(item)
                self.dataDisks.append(obj)
        self.timeZone = params.get("timeZone")
        self.enableAgent = params.get("enableAgent")
        self.enableIpForward = params.get("enableIpForward")
        self.eipV4Type = params.get("eipV4Type")


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




class CreateInstancesRequest(AbstractModel):

    def __init__(self):
        self.zoneId = None
        self.instanceType = None
        self.imageId = None
        self.resourceGroupId = None
        self.instanceName = None
        self.instanceCount = None
        self.password = None
        self.keyId = None
        self.internetChargeType = None
        self.trafficPackageSize = None
        self.subnetId = None
        self.systemDisk = None
        self.dataDisks = None
        self.timeZone = None
        self.enableAgent = None
        self.enableIpForward = None
        self.eipV4Type = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceType = params.get("instanceType")
        self.imageId = params.get("imageId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.instanceName = params.get("instanceName")
        self.instanceCount = params.get("instanceCount")
        self.password = params.get("password")
        self.keyId = params.get("keyId")
        self.internetChargeType = params.get("internetChargeType")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.subnetId = params.get("subnetId")
        if params.get("systemDisk") is not None:
            self.systemDisk = SystemDisk(params.get("systemDisk"))
        if params.get("dataDisks") is not None:
            self.dataDisks = []
            for item in params.get("dataDisks"):
                obj = DataDisk(item)
                self.dataDisks.append(obj)
        self.timeZone = params.get("timeZone")
        self.enableAgent = params.get("enableAgent")
        self.enableIpForward = params.get("enableIpForward")
        self.eipV4Type = params.get("eipV4Type")


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
        self.cpuCount = None
        self.memory = None
        self.frequency = None
        self.internetMaxBandwidthOutLimit = None
        self.instanceTypeName = None
        self.internetChargeTypes = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceType = params.get("instanceType")
        self.cpuCount = params.get("cpuCount")
        self.memory = params.get("memory")
        self.frequency = params.get("frequency")
        self.internetMaxBandwidthOutLimit = params.get("internetMaxBandwidthOutLimit")
        self.instanceTypeName = params.get("instanceTypeName")
        self.internetChargeTypes = params.get("internetChargeTypes")



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

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.zoneName = params.get("zoneName")



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



class DescribeKeyPairsRequest(AbstractModel):

    def __init__(self):
        self.keyIds = None
        self.keyName = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.keyIds = params.get("keyIds")
        self.keyName = params.get("keyName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeKeyPairsResponse(AbstractModel):

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
                obj = KeyPair(item)
                self.dataSet.append(obj)


class KeyPair(AbstractModel):

    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.keyId = None
        self.keyName = None
        self.publicKey = None
        self.keyDescription = None
        self.createTime = None

    def _deserialize(self, params):
        self.keyId = params.get("keyId")
        self.keyName = params.get("keyName")
        self.publicKey = params.get("publicKey")
        self.keyDescription = params.get("keyDescription")
        self.createTime = params.get("createTime")