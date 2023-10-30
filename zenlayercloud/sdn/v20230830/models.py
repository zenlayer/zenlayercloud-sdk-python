#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel

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
                obj = DatacenterInfo(item)
                self.dcSet.append(obj)


class CreatePortRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.portName = None
        self.portRemarks = None
        self.portType = None
        self.businessEntityName = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.portName = params.get("portName")
        self.portRemarks = params.get("portRemarks")
        self.portType = params.get("portType")
        self.businessEntityName = params.get("businessEntityName")


class CreatePortResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.portId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.portId = params.get("portId")


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
        self.portDailyPrice = None
        self.portMonthlyPrice = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.portType = params.get("portType")
        self.portDailyPrice = params.get("portDailyPrice")
        self.portMonthlyPrice = params.get("portMonthlyPrice")

class DescribePortsRequest(AbstractModel):
    def __init__(self):
        self.portIds = None
        self.dcId = None
        self.portName = None
        self.portRemarks = None
        self.cityName = None

    def _deserialize(self, params):
        self.portIds = params.get("portIds")
        self.dcId = params.get("dcId")
        self.portName = params.get("portName")
        self.portRemarks = params.get("portRemarks")
        self.cityName = params.get("cityName")


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
        self.connectionStatus = None
        self.portStatus = None
        self.dcId = None
        self.dcName = None
        self.cityName = None
        self.areaName = None
        self.loaStatus = None
        self.loaDownloadUrl = None
        self.createdTime = None
        self.expiredTime = None
        self.portChargeType = None
        self.period = None

    def _deserialize(self, params):
        self.portId = params.get("portId")
        self.portName = params.get("portName")
        self.portRemarks = params.get("portRemarks")
        self.portType = params.get("portType")
        self.connectionStatus = params.get("connectionStatus")
        self.portStatus = params.get("portStatus")
        self.dcId = params.get("dcId")
        self.dcName = params.get("dcName")
        self.cityName = params.get("cityName")
        self.areaName = params.get("areaName")
        self.loaStatus = params.get("loaStatus")
        self.loaDownloadUrl = params.get("loaDownloadUrl")
        self.createdTime = params.get("createdTime")
        self.expiredTime = params.get("expiredTime")
        self.portChargeType = params.get("portChargeType")
        self.period = params.get("period")


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
        self.inTotal = None
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
        self.inTotal = params.get("inTotal")
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
        self.dcId = None
        self.portId = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.portId = params.get("portId")


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


class DescribePrivateConnectsRequest(AbstractModel):
    def __init__(self):
        self.privateConnectIds = None
        self.privateConnectName = None
        self.connectivityStatus = None
        self.privateConnectStatus = None
        self.endpointTypes = None
        self.resourceGroupId = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.privateConnectIds = params.get("privateConnectIds")
        self.privateConnectName = params.get("privateConnectName")
        self.connectivityStatus = params.get("connectivityStatus")
        self.privateConnectStatus = params.get("privateConnectStatus")
        self.endpointTypes = params.get("endpointTypes")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")

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
        self.endpointA = None
        self.endpointZ = None
        self.privateConnectStatus = None
        self.bandwidthMbps = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.createTime = None
        self.expiredTime = None
        self.recycledTime = None

    def _deserialize(self, params):
        self.privateConnectId = params.get("privateConnectId")
        self.privateConnectName = params.get("privateConnectName")
        self.connectivityStatus = params.get("connectivityStatus")
        if params.get("endpointA") is not None:
            self.endpointA = PrivateConnectEndpoint(params.get("endpointA"))
        if params.get("endpointZ") is not None:
            self.endpointZ = PrivateConnectEndpoint(params.get("endpointZ"))
        self.privateConnectStatus = params.get("privateConnectStatus")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.recycledTime = params.get("recycledTime")


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
        self.dataCenter = None
        self.vlanId = None
        self.connectivityStatus = None

    def _deserialize(self, params):
        self.endpointId = params.get("endpointId")
        self.endpointName = params.get("endpointName")
        self.endpointType = params.get("endpointType")
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        self.vlanId = params.get("vlanId")
        self.connectivityStatus = params.get("connectivityStatus")



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

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.dcName = params.get("dcName")
        self.dcAddress = params.get("dcAddress")
        self.cityName = params.get("cityName")
        self.countryName = params.get("countryName")
        self.areaName = params.get("areaName")


class DescribeCreatePrivateConnectAvailableSubnetsRequest(AbstractModel):
    def __init__(self):
        self.dcId = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.dcId = params.get("dcId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")

class DescribeCreatePrivateConnectAvailableSubnetsResponse(AbstractModel):

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
                obj = PrivateConnectAvailableSubnet(item)
                self.dataSet.append(obj)


class PrivateConnectAvailableSubnet(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.subnetId = None
        self.zoneId = None
        self.dataCenter = None
        self.cidrBlock = None
        self.vlanId = None

    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.zoneId = params.get("zoneId")
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        self.cidrBlock = params.get("cidrBlock")
        self.vlanId = params.get("vlanId")


class CreatePrivateConnectRequest(AbstractModel):
    def __init__(self):
        self.privateConnectName = None
        self.endpointA = None
        self.endpointZ = None
        self.bandwidthMbps = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.privateConnectName = params.get("privateConnectName")
        if params.get("endpointA") is not None:
            self.endpointA = CreateEndpointParam(params.get("endpointA"))
        if params.get("endpointZ") is not None:
            self.endpointZ = CreateEndpointParam(params.get("endpointZ"))
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.resourceGroupId = params.get("resourceGroupId")

class CreatePrivateConnectResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.privateConnectId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.privateConnectId = params.get("privateConnectId")


class CreateEndpointParam(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.subnetId = None
        self.portId = None
        self.vlanId = None


    def _deserialize(self, params):
        self.subnetId = params.get("subnetId")
        self.portId = params.get("portId")
        self.vlanId = params.get("vlanId")



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


class InquiryCreatePrivateConnectPriceRequest(AbstractModel):
    def __init__(self):
        self.endpointA = None
        self.endpointZ = None
        self.bandwidthMbps = None

    def _deserialize(self, params):
        if params.get("endpointA") is not None:
            self.endpointA = CreateEndpointParam(params.get("endpointA"))
        if params.get("endpointZ") is not None:
            self.endpointZ = CreateEndpointParam(params.get("endpointZ"))
        self.bandwidthMbps = params.get("bandwidthMbps")


class InquiryCreatePrivateConnectPriceResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.privateConnectPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("privateConnectPrice") is not None:
            self.privateConnectPrice = Price(params.get("privateConnectPrice"))


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
        self.inTotal = None
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
        self.inTotal = params.get("inTotal")
        self.out95 = params.get("out95")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.unit = params.get("unit")



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


class DescribeCloudRoutersRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterIds = None
        self.cloudRouterName = None
        self.cloudRouterStatus = None
        self.egdePointId = None
        self.resourceGroupId = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.cloudRouterIds = params.get("cloudRouterIds")
        self.cloudRouterName = params.get("cloudRouterName")
        self.cloudRouterStatus = params.get("cloudRouterStatus")
        self.egdePointId = params.get("egdePointId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")

class DescribeCloudRoutersResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.dataSet = None
        self.totalCount = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = CloudRouter(item)
                self.dataSet.append(obj)
        self.totalCount = params.get("totalCount")


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
        self.edgePoints = None
        self.cloudRouterChargeType = None
        self.createTime = None
        self.expiredTime = None
        self.recycledTime = None
        self.period = None
        self.cloudRouterStatus = None
        self.connectivityStatus = None
        self.resourceGroupId = None
        self.resourceGroupName = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")
        self.cloudRouterName = params.get("cloudRouterName")
        self.cloudRouterDescription = params.get("cloudRouterDescription")
        if params.get("edgePoints") is not None:
            self.edgePoints = []
            for item in params.get("edgePoints"):
                obj = CloudRouterEdgePoint(item)
                self.edgePoints.append(obj)
        self.cloudRouterChargeType = params.get("cloudRouterChargeType")
        self.createTime = params.get("createTime")
        self.expiredTime = params.get("expiredTime")
        self.recycledTime = params.get("recycledTime")
        self.period = params.get("period")
        self.cloudRouterStatus = params.get("cloudRouterStatus")
        self.connectivityStatus = params.get("connectivityStatus")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")


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
        self.ipAddress = None
        self.edgePointType = None
        self.vpcId = None
        self.portId = None
        self.vlanId = None
        self.bandwidthMbps = None
        self.bgpConnection = None
        self.staticRoutes = None
        self.createTime = None

    def _deserialize(self, params):
        self.edgePointId = params.get("edgePointId")
        self.edgePointName = params.get("edgePointName")
        self.connectivityStatus = params.get("connectivityStatus")
        if params.get("dataCenter") is not None:
            self.dataCenter = DatacenterInfo(params.get("dataCenter"))
        self.ipAddress = params.get("ipAddress")
        self.edgePointType = params.get("edgePointType")
        self.vpcId = params.get("vpcId")
        self.portId = params.get("portId")
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


class BGPConnection(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.peerIpAddress = None
        self.peerAsn = None
        self.localAsn = None
        self.password = None

    def _deserialize(self, params):
        self.peerIpAddress = params.get("peerIpAddress")
        self.peerAsn = params.get("peerAsn")
        self.localAsn = params.get("localAsn")
        self.password = params.get("password")


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



class DescribeCloudRouterAvailableVpcsRequest(AbstractModel):
    def __init__(self):
        self.vpcId = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")

class DescribeCloudRouterAvailableVpcsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.dataSet = None
        self.totalCount = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = CloudRouterAvailableVpc(item)
                self.dataSet.append(obj)
        self.totalCount = params.get("totalCount")


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

class DescribeCloudRouterAvailablePortsRequest(AbstractModel):
    def __init__(self):
        self.portIds = None
        self.dcId = None
        self.pageNum = None
        self.pageSize = None

    def _deserialize(self, params):
        self.portIds = params.get("portIds")
        self.dcId = params.get("dcId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")


class DescribeCloudRouterAvailablePortsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.dataSet = None
        self.totalCount = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = PortInfo(item)
                self.dataSet.append(obj)
        self.totalCount = params.get("totalCount")


class CreateCloudRouterRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterName = None
        self.cloudRouterDescription = None
        self.edgePoints = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.cloudRouterName = params.get("cloudRouterName")
        self.cloudRouterDescription = params.get("cloudRouterDescription")
        if params.get("edgePoints") is not None:
            self.edgePoints = []
            for item in params.get("edgePoints"):
                obj = CreateCloudRouterEdgePoint(item)
                self.edgePoints.append(obj)
        self.resourceGroupId = params.get("resourceGroupId")


class CreateCloudRouterResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.cloudRouterId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.cloudRouterId = params.get("cloudRouterId")


class CreateCloudRouterEdgePoint(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.vpcId = None
        self.bandwidthMbps = None
        self.portId = None
        self.vlanId = None
        self.ipAddress = None
        self.bgpConnection = None
        self.staticRoutes = None

    def _deserialize(self, params):
        self.vpcId = params.get("vpcId")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.portId = params.get("portId")
        self.vlanId = params.get("vlanId")
        self.ipAddress = params.get("ipAddress")
        if params.get("bgpConnection") is not None:
            self.bgpConnection = BGPConnection(params.get("bgpConnection"))
        if params.get("staticRoutes") is not None:
            self.staticRoutes = []
            for item in params.get("staticRoutes"):
                obj = IPRoute(item)
                self.staticRoutes.append(obj)


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


class DeleteCloudRouterEdgePointRequest(AbstractModel):
    def __init__(self):
        self.edgePointId = None
        self.cloudRouterId = None

    def _deserialize(self, params):
        self.edgePointId = params.get("edgePointId")
        self.cloudRouterId = params.get("cloudRouterId")


class DeleteCloudRouterEdgePointResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteCloudRouterEdgePointRequest(AbstractModel):
    def __init__(self):
        self.cloudRouterId = None

    def _deserialize(self, params):
        self.cloudRouterId = params.get("cloudRouterId")


class DeleteCloudRouterEdgePointResponse(AbstractModel):

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


class ModifyCloudRouterEdgePointBandwidthRequest(AbstractModel):
    def __init__(self):
        self.edgePointId = None
        self.cloudRouterId = None
        self.bandwidthMbps = None

    def _deserialize(self, params):
        self.edgePointId = params.get("edgePointId")
        self.cloudRouterId = params.get("cloudRouterId")
        self.bandwidthMbps = params.get("bandwidthMbps")


class ModifyCloudRouterEdgePointBandwidthResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeCloudRouteEdgePointTrafficRequest(AbstractModel):
    def __init__(self):
        self.edgePointId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.edgePointId = params.get("edgePointId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeCloudRouteEdgePointTrafficResponse(AbstractModel):

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
        self.inTotal = params.get("inTotal")
        self.out95 = params.get("out95")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.unit = params.get("unit")


class ModifyCloudRouterEdgePointRequest(AbstractModel):
    def __init__(self):
        self.edgePointId = None
        self.cloudRouterId = None
        self.bgpConnection = None
        self.staticRoutes = None
        self.bandwidthMbps = None
        self.ipAddress = None

    def _deserialize(self, params):
        self.edgePointId = params.get("edgePointId")
        self.cloudRouterId = params.get("cloudRouterId")
        if params.get("bgpConnection") is not None:
            self.bgpConnection = BGPConnection(params.get("bgpConnection"))
        if params.get("staticRoutes") is not None:
            self.staticRoutes = []
            for item in params.get("staticRoutes"):
                obj = IPRoute(item)
                self.staticRoutes.append(obj)
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.ipAddress = params.get("ipAddress")


class ModifyCloudRouterEdgePointResponse(AbstractModel):

    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
