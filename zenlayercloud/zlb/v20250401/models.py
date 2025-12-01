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
        self.kind = None
        self.createTime = None

    def _deserialize(self, params):
        self.listenerId = params.get("listenerId")
        self.listenerName = params.get("listenerName")
        self.protocol = params.get("protocol")
        self.port = params.get("port")
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))
        self.scheduler = params.get("scheduler")
        self.kind = params.get("kind")
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
        self.failOpen = None

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
        self.failOpen = params.get("failOpen")


class CreateListenerRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerName = None
        self.healthCheck = None
        self.protocol = None
        self.scheduler = None
        self.port = None
        self.kind = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerName = params.get("listenerName")
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))
        self.protocol = params.get("protocol")
        self.scheduler = params.get("scheduler")
        self.port = params.get("port")
        self.kind = params.get("kind")


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
        self.kind = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")
        self.listenerName = params.get("listenerName")
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))
        self.scheduler = params.get("scheduler")
        self.port = params.get("port")
        self.kind = params.get("kind")


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


class DescribeBackendHealthRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerId = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")


class DescribeBackendHealthResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.backends = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("backends") is not None:
            self.backends = []
            for item in params.get("backends"):
                obj = ListenerBackendHealth(item)
                self.backends.append(obj)


class ListenerBackendHealth(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.healthStatus = None
        self.healthStatusDetail = None
        self.instanceId = None
        self.privateIpAddress = None
        self.weight = None
        self.backendPort = None
        self.listenerId = None
        self.listenerName = None
        self.protocol = None
        self.listenerPort = None

    def _deserialize(self, params):
        self.healthStatus = params.get("healthStatus")
        if params.get("healthStatusDetail") is not None:
            self.healthStatusDetail = []
            for item in params.get("healthStatusDetail"):
                obj = BackendHealthStatusDetail(item)
                self.healthStatusDetail.append(obj)
        self.instanceId = params.get("instanceId")
        self.privateIpAddress = params.get("privateIpAddress")
        self.weight = params.get("weight")
        self.backendPort = params.get("backendPort")
        self.listenerId = params.get("listenerId")
        self.listenerName = params.get("listenerName")
        self.protocol = params.get("protocol")
        self.listenerPort = params.get("listenerPort")


class BackendHealthStatusDetail(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.port = None
        self.healthStatus = None

    def _deserialize(self, params):
        self.port = params.get("port")
        self.healthStatus = params.get("healthStatus")


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
        self.pageSize = None
        self.pageNum = None
        self.resourceGroupId = None
        self.tagKeys = None
        self.tags = None
        self.securityGroupId = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.vpcId = params.get("vpcId")
        self.loadBalancerIds = params.get("loadBalancerIds")
        self.loadBalancerName = params.get("loadBalancerName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.resourceGroupId = params.get("resourceGroupId")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)
        self.securityGroupId = params.get("securityGroupId")


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
        self.privateIpAddress = None
        self.healthCheckPrivateIps = None
        self.listenerCount = None
        self.createTime = None
        self.resourceGroup = None
        self.tags = None
        self.securityGroupId = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.loadBalancerId = params.get("loadBalancerId")
        self.loadBalancerName = params.get("loadBalancerName")
        self.vpcId = params.get("vpcId")
        self.status = params.get("status")
        self.publicIpAddress = params.get("publicIpAddress")
        self.privateIpAddress = params.get("privateIpAddress")
        self.healthCheckPrivateIps = params.get("healthCheckPrivateIps")
        self.listenerCount = params.get("listenerCount")
        self.createTime = params.get("createTime")
        if params.get("resourceGroup") is not None:
            self.resourceGroup = ResourceGroupInfo(params.get("resourceGroup"))
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))
        self.securityGroupId = params.get("securityGroupId")


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
        self.marketingOptions = None
        self.tags = None
        self.subnetId = None
        self.healthCheckPrivateIps = None
        self.securityGroupId = None

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
        if params.get("marketingOptions") is not None:
            self.marketingOptions = MarketingInfo(params.get("marketingOptions"))
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))
        self.subnetId = params.get("subnetId")
        self.healthCheckPrivateIps = params.get("healthCheckPrivateIps")
        self.securityGroupId = params.get("securityGroupId")


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
        self.internetChargeType = None
        self.ipNetworkType = None
        self.bandwidthMbps = None
        self.trafficPackageSize = None
        self.bandwidthClusterId = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
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
        if params.get("loadBalancerInstancePrice") is not None:
            self.loadBalancerInstancePrice = PriceItem(params.get("loadBalancerInstancePrice"))
        if params.get("eipPrice") is not None:
            self.eipPrice = PriceItem(params.get("eipPrice"))
        if params.get("eipNetworkPrice") is not None:
            self.eipNetworkPrice = PriceItem(params.get("eipNetworkPrice"))
        if params.get("lcuPrice") is not None:
            self.lcuPrice = PriceItem(params.get("lcuPrice"))


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


class DescribeLoadBalancerMonitorDataRequest(AbstractModel):
    def __init__(self):
        self.loadBalancerId = None
        self.listenerId = None
        self.metricType = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.loadBalancerId = params.get("loadBalancerId")
        self.listenerId = params.get("listenerId")
        self.metricType = params.get("metricType")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeLoadBalancerMonitorDataResponse(AbstractModel):
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


class SetSecurityGroupForLoadBalancersRequest(AbstractModel):
    def __init__(self):
        self.securityGroupId = None
        self.loadBalancerIds = None

    def _deserialize(self, params):
        self.securityGroupId = params.get("securityGroupId")
        self.loadBalancerIds = params.get("loadBalancerIds")


class SetSecurityGroupForLoadBalancersResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.failedLoadBalancerIds = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.failedLoadBalancerIds = params.get("failedLoadBalancerIds")


class AddLoadBalancersPrivateIpsRequest(AbstractModel):
    def __init__(self):
        self.privateIps = None
        self.loadBalancerId = None
        self.subnetId = None

    def _deserialize(self, params):
        self.privateIps = params.get("privateIps")
        self.loadBalancerId = params.get("loadBalancerId")
        self.subnetId = params.get("subnetId")


class AddLoadBalancersPrivateIpsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteLoadBalancersPrivateIpsRequest(AbstractModel):
    def __init__(self):
        self.privateIps = None
        self.loadBalancerId = None

    def _deserialize(self, params):
        self.privateIps = params.get("privateIps")
        self.loadBalancerId = params.get("loadBalancerId")


class DeleteLoadBalancersPrivateIpsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


