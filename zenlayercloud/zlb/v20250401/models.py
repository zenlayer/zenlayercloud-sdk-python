#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeListenersRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerIds = None
        self.protocol = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerIds = params.get("listenerIds")
        self.protocol = params.get("protocol")


class DescribeListenersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.listeners = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("listeners") is not None:
            self.listeners = []
            for item in params.get("listeners"):
                obj = Listener(item)
                self.listeners.append(obj)


class Listener(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.listenerId = None
        self.listenerName = None
        self.protocol = None
        self.port = None
        self.healthCheck = None
        self.scheduler = None
        self.createTime = None

    def _deserialize(self, params):
        self.listenerId = params.get("listenerId")
        self.listenerName = params.get("listenerName")
        self.protocol = params.get("protocol")
        self.port = params.get("port")
        self.healthCheck = params.get("healthCheck")
        self.scheduler = params.get("scheduler")
        self.createTime = params.get("createTime")


class HealthCheck(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.enabled = None
        self.checkType = None
        self.checkPort = None
        self.checkDelayLoop = None
        self.checkConnTimeout = None
        self.checkRetry = None
        self.checkDelayTry = None
        self.checkHttpGetUrl = None
        self.checkHttpStatusCode = None

    def _deserialize(self, params):
        self.enabled = params.get("enabled")
        self.checkType = params.get("checkType")
        self.checkPort = params.get("checkPort")
        self.checkDelayLoop = params.get("checkDelayLoop")
        self.checkConnTimeout = params.get("checkConnTimeout")
        self.checkRetry = params.get("checkRetry")
        self.checkDelayTry = params.get("checkDelayTry")
        self.checkHttpGetUrl = params.get("checkHttpGetUrl")
        self.checkHttpStatusCode = params.get("checkHttpStatusCode")


class CreateListenerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerName = None
        self.healthCheck = None
        self.protocol = None
        self.scheduler = None
        self.port = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerName = params.get("listenerName")
        self.healthCheck = params.get("healthCheck")
        self.protocol = params.get("protocol")
        self.scheduler = params.get("scheduler")
        self.port = params.get("port")


class CreateListenerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.listenerId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.listenerId = params.get("listenerId")


class DeleteListenerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerId = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")


class DeleteListenerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyListenerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerId = None
        self.listenerName = None
        self.healthCheck = None
        self.scheduler = None
        self.port = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")
        self.listenerName = params.get("listenerName")
        self.healthCheck = params.get("healthCheck")
        self.scheduler = params.get("scheduler")
        self.port = params.get("port")


class ModifyListenerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeLoadBalancerRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeLoadBalancerRegionsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.regions = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("regions") is not None:
            self.regions = []
            for item in params.get("regions"):
                obj = Region(item)
                self.regions.append(obj)


class Region(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.regionId = None
        self.cityName = None
        self.cityCode = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.cityName = params.get("cityName")
        self.cityCode = params.get("cityCode")


class RegisterBackendRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerId = None
        self.backendServers = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")
        if params.get("backendServers") is not None:
            self.backendServers = []
            for item in params.get("backendServers"):
                obj = BackendServer(item)
                self.backendServers.append(obj)


class BackendServer(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.privateIpAddress = None
        self.weight = None
        self.port = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.privateIpAddress = params.get("privateIpAddress")
        self.weight = params.get("weight")
        self.port = params.get("port")


class RegisterBackendResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeregisterBackendRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerId = None
        self.backendServers = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")
        if params.get("backendServers") is not None:
            self.backendServers = []
            for item in params.get("backendServers"):
                obj = BackendServer(item)
                self.backendServers.append(obj)


class DeregisterBackendResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyBackendRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerId = None
        self.backendServers = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")
        if params.get("backendServers") is not None:
            self.backendServers = []
            for item in params.get("backendServers"):
                obj = BackendServer(item)
                self.backendServers.append(obj)


class ModifyBackendResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeBackendsRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerId = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")


class DescribeBackendsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.backends = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("backends") is not None:
            self.backends = []
            for item in params.get("backends"):
                obj = ListenerBackend(item)
                self.backends.append(obj)


class ListenerBackend(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.privateIpAddress = None
        self.weight = None
        self.backendPort = None
        self.listenerId = None
        self.listenerName = None
        self.protocol = None
        self.listenerPort = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.privateIpAddress = params.get("privateIpAddress")
        self.weight = params.get("weight")
        self.backendPort = params.get("backendPort")
        self.listenerId = params.get("listenerId")
        self.listenerName = params.get("listenerName")
        self.protocol = params.get("protocol")
        self.listenerPort = params.get("listenerPort")


class ModifyLoadBalancersAttributeRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerIds = None
        self.loadBalancerName = None

    def _deserialize(self, params):
        self.loadBalancerIds = params.get("loadBalancerIds")
        self.loadBalancerName = params.get("loadBalancerName")


class ModifyLoadBalancersAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeLoadBalancersRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.vpcId = None
        self.loadBalancerIds = None
        self.loadBalancerName = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.loadBalancerIds = params.get("loadBalancerIds")
        self.loadBalancerName = params.get("loadBalancerName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


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
                obj = LoadBalancer(item)
                self.dataSet.append(obj)


class LoadBalancer(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.regionId = None
        self.loadBalancerId = None
        self.loadBalancerName = None
        self.vpcId = None
        self.status = None
        self.publicIpAddress = None
        self.listenerCount = None
        self.createTime = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.loadBalancerId = params.get("loadBalancerId")
        self.loadBalancerName = params.get("loadBalancerName")
        self.vpcId = params.get("vpcId")
        self.status = params.get("status")
        self.publicIpAddress = params.get("publicIpAddress")
        self.listenerCount = params.get("listenerCount")
        self.createTime = params.get("createTime")


class RestoreLoadBalancerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")


class RestoreLoadBalancerResponse(AbstractModel):
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


class CreateLoadBalancerRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.vpcId = None
        self.loadBalancerName = None
        self.internetChargeType = None
        self.ipNetworkType = None
        self.bandwidthMbps = None
        self.trafficPackageSize = None
        self.bandwidthClusterId = None
        self.resourceGroupId = None
        self.number = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.loadBalancerName = params.get("loadBalancerName")
        self.internetChargeType = params.get("internetChargeType")
        self.ipNetworkType = params.get("ipNetworkType")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.bandwidthClusterId = params.get("bandwidthClusterId")
        self.resourceGroupId = params.get("resourceGroupId")
        self.number = params.get("number")


class CreateLoadBalancerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.orderNumber = None
        self.loadBalancerIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.orderNumber = params.get("orderNumber")
        self.loadBalancerIds = params.get("loadBalancerIds")


class InquiryPriceCreateLoadBalancerRequest(AbstractModel):
    def __init__(self):
        self.regionId = None
        self.vpcId = None
        self.internetChargeType = None
        self.ipNetworkType = None
        self.bandwidthMbps = None
        self.trafficPackageSize = None
        self.bandwidthClusterId = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.internetChargeType = params.get("internetChargeType")
        self.ipNetworkType = params.get("ipNetworkType")
        self.bandwidthMbps = params.get("bandwidthMbps")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.bandwidthClusterId = params.get("bandwidthClusterId")


class InquiryPriceCreateLoadBalancerResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.loadBalancerInstancePrice = None
        self.eipPrice = None
        self.eipNetworkPrice = None
        self.lcuPrice = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.loadBalancerInstancePrice = params.get("loadBalancerInstancePrice")
        self.eipPrice = params.get("eipPrice")
        self.eipNetworkPrice = params.get("eipNetworkPrice")
        self.lcuPrice = params.get("lcuPrice")


class NewPriceItem(AbstractModel):
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


