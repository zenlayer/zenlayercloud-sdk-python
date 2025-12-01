#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeOriginRegionsRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeOriginRegionsResponse(AbstractModel):
    def __init__(self):
        self.regionSet = None
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("regionSet") is not None:
            self.regionSet = []
            for item in params.get("regionSet"):
                obj = Region(item)
                self.regionSet.append(obj)


class DescribeAccelerateRegionsRequest(AbstractModel):
    def __init__(self, originRegionId):
        self.originRegionId = originRegionId

    def _deserialize(self, params):
        self.originRegionId = params.get("originRegionId")


class DescribeAccelerateRegionsResponse(DescribeOriginRegionsResponse):
    pass


class DescribeCertificatesRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.certificateIds = None
        self.certificateLabel = None
        self.san = None
        self.resourceGroupId = None
        self.expired = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.certificateIds = params.get("certificateIds")
        self.certificateLabel = params.get("certificateLabel")
        self.san = params.get("san")
        self.resourceGroupId = params.get("resourceGroupId")
        self.expired = params.get("expired")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeCertificatesResponse(AbstractModel):
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
                obj = CertificateInfo(item)
                self.dataSet.append(obj)


class CreateCertificateRequest(AbstractModel):
    def __init__(self, certificateContent, certificateKey):
        self.certificateContent = certificateContent
        self.certificateKey = certificateKey
        self.certificateLabel = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.certificateContent = params.get("certificateContent")
        self.certificateKey = params.get("certificateKey")
        self.certificateLabel = params.get("certificateLabel")
        self.resourceGroupId = params.get("resourceGroupId")


class CreateCertificateResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.certificateId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.certificateId = params.get("certificateId")


class ModifyCertificateRequest(AbstractModel):
    def __init__(self, certificateId, certificateContent, certificateKey):
        self.certificateId = certificateId
        self.certificateContent = certificateContent
        self.certificateKey = certificateKey

    def _deserialize(self, params):
        self.certificateId = params.get("certificateId")
        self.certificateContent = params.get("certificateContent")
        self.certificateKey = params.get("certificateKey")


class ModifyCertificateResponse(CreateCertificateResponse):
    pass


class DeleteCertificateRequest(AbstractModel):
    def __init__(self, certificateId):
        self.certificateId = certificateId

    def _deserialize(self, params):
        self.certificateId = params.get("certificateId")


class DeleteCertificateResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeAcceleratorsRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorIds = None
        self.acceleratorName = None
        self.acceleratorStatus = None
        self.accelerateRegionId = None
        self.vip = None
        self.domain = None
        self.origin = None
        self.originRegionId = None
        self.cname = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.acceleratorIds = params.get("acceleratorIds")
        self.acceleratorName = params.get("acceleratorName")
        self.acceleratorStatus = params.get("acceleratorStatus")
        self.accelerateRegionId = params.get("accelerateRegionId")
        self.vip = params.get("vip")
        self.domain = params.get("domain")
        self.origin = params.get("origin")
        self.originRegionId = params.get("originRegionId")
        self.cname = params.get("cname")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeAcceleratorsResponse(AbstractModel):
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
                obj = AcceleratorInfo(item)
                self.dataSet.append(obj)


class CreateAcceleratorRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorName = None
        self.chargeType = None
        self.resourceGroupId = None
        self.certificateId = None
        self.domain = None
        self.origin = None
        self.accelerateRegions = None
        self.l4Listeners = None
        self.l7Listeners = None
        self.protocolOpts = None
        self.healthCheck = None

    def _deserialize(self, params):
        self.acceleratorName = params.get("acceleratorName")
        self.chargeType = params.get("chargeType")
        self.resourceGroupId = params.get("resourceGroupId")
        self.certificateId = params.get("certificateId")
        if params.get("domain") is not None:
            self.domain = Domain(params.get("domain"))
        if params.get("origin") is not None:
            self.origin = Origin(params.get("origin"))
        if params.get("accelerateRegions") is not None:
            self.accelerateRegions = []
            for item in params.get("accelerateRegions"):
                obj = AccelerateRegion(item)
                self.accelerateRegions.append(obj)
        if params.get("l4Listeners") is not None:
            self.l4Listeners = []
            for item in params.get("l4Listeners"):
                obj = AccelerationRuleL4Listener(item)
                self.l4Listeners.append(obj)
        if params.get("l7Listeners") is not None:
            self.l7Listeners = []
            for item in params.get("l7Listeners"):
                obj = AccelerationRuleL7Listener(item)
                self.l7Listeners.append(obj)
        if params.get("protocolOpts") is not None:
            self.protocolOpts = AccelerationRuleProtocolOpts(params.get("protocolOpts"))
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))


class CreateAcceleratorResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.acceleratorId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.acceleratorId = params.get("acceleratorId")


class DeleteAcceleratorRequest(AbstractModel):
    def __init__(self, acceleratorId):
        self.acceleratorId = acceleratorId

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")


class DeleteAcceleratorResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class StartAcceleratorRequest(DeleteAcceleratorRequest):
    pass


class StartAcceleratorResponse(DeleteAcceleratorResponse):
    pass


class RedeployAcceleratorRequest(DeleteAcceleratorRequest):
    pass


class RedeployAcceleratorResponse(DeleteAcceleratorResponse):
    pass


class PauseAcceleratorRequest(DeleteAcceleratorRequest):
    pass


class PauseAcceleratorResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorDomainRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.domain = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        if params.get("domain") is not None:
            self.domain = Domain(params.get("domain"))


class ModifyAcceleratorDomainResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorNameRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.acceleratorName = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        self.acceleratorName = params.get("acceleratorName")


class ModifyAcceleratorNameResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorOriginRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.origin = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        if params.get("origin") is not None:
            self.origin = Origin(params.get("origin"))


class ModifyAcceleratorOriginResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorAccRegionRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.accelerateRegions = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        if params.get("accelerateRegions") is not None:
            self.accelerateRegions = []
            for item in params.get("accelerateRegions"):
                obj = AccelerateRegion(item)
                self.accelerateRegions.append(obj)


class ModifyAcceleratorAccRegionResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorRuleRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.l4Listeners = None
        self.l7Listeners = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        if params.get("l4Listeners") is not None:
            self.l4Listeners = []
            for item in params.get("l4Listeners"):
                obj = AccelerationRuleL4Listener(item)
                self.l4Listeners.append(obj)
        if params.get("l7Listeners") is not None:
            self.l7Listeners = []
            for item in params.get("l7Listeners"):
                obj = AccelerationRuleL7Listener(item)
                self.l7Listeners.append(obj)


class ModifyAcceleratorRuleResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorProtocolOptsRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.protocolOpts = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        if params.get("protocolOpts") is not None:
            self.protocolOpts = AccelerationRuleProtocolOpts(params.get("protocolOpts"))


class ModifyAcceleratorProtocolOptsResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorCertificateRequest(AbstractModel):
    def __init__(self, acceleratorId, certificateId):
        self.acceleratorId = acceleratorId
        self.certificateId = certificateId

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        self.certificateId = params.get("certificateId")


class ModifyAcceleratorCertificateResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorHealthCheckRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.healthCheck = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))


class ModifyAcceleratorHealthCheckResponse(DeleteAcceleratorResponse):
    pass


class ModifyAcceleratorAccessControlRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.accessControlRules = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        if params.get("accessControlRules") is not None:
            self.accessControlRules = []
            for item in params.get("accessControlRules"):
                obj = AccessControlRule(item)
                self.accessControlRules.append(obj)


class ModifyAcceleratorAccessControlResponse(DeleteAcceleratorResponse):
    pass


class OpenAcceleratorAccessControlRequest(DeleteAcceleratorRequest):
    pass


class OpenAcceleratorAccessControlResponse(DeleteAcceleratorResponse):
    pass


class CloseAcceleratorAccessControlRequest(DeleteAcceleratorRequest):
    pass


class CloseAcceleratorAccessControlResponse(DeleteAcceleratorResponse):
    pass


class DescribeAcceleratorsAlertsRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorIds = None
        self.resourceGroupId = None
        self.alertType = None
        self.alertId = None
        self.firing = None
        self.startTimeFrom = None
        self.startTimeTo = None
        self.endTimeFrom = None
        self.endTimeTo = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.acceleratorIds = params.get("acceleratorIds")
        self.resourceGroupId = params.get("resourceGroupId")
        self.alertType = params.get("alertType")
        self.alertId = params.get("alertId")
        self.firing = params.get("firing")
        self.startTimeFrom = params.get("startTimeFrom")
        self.startTimeTo = params.get("startTimeTo")
        self.endTimeFrom = params.get("endTimeFrom")
        self.endTimeTo = params.get("endTimeTo")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeAcceleratorsAlertsResponse(AbstractModel):
    def __init__(self, params=None):
        self.requestId = None
        self.totalCount = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalCount = params.get("totalCount")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = AcceleratorAlert(item)
                self.dataSet.append(obj)


class DescribeAcceleratorLogsRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.vips = None
        self.domains = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        self.vips = params.get("vips")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.domains = params.get("domains")


class DescribeAcceleratorLogsResponse(AbstractModel):
    def __init__(self, params=None):
        self.requestId = None
        self.totalCount = None
        self.logSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalCount = params.get("totalCount")
        if params.get("logSet") is not None:
            self.logSet = []
            for item in params.get("logSet"):
                obj = AcceleratorLog(item)
                self.logSet.append(obj)


class DescribeAcceleratorTrafficRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.accelerateRegionId = None
        self.listener = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        self.accelerateRegionId = params.get("accelerateRegionId")
        self.listener = params.get("listener")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeAcceleratorTrafficResponse(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.requestId = None
        self.dataList = None
        self.inMax = None
        self.inMin = None
        self.inTotal = None
        self.outMax = None
        self.outMin = None
        self.outTotal = None
        self.totalUnit = None
        self.unit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.inMax = params.get("inMax")
        self.inMin = params.get("inMin")
        self.inTotal = params.get("inTotal")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.outTotal = params.get("outTotal")
        self.totalUnit = params.get("totalUnit")
        self.unit = params.get("unit")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = AcceleratorTrafficData(item)
                self.dataList.append(obj)


class AcceleratorTrafficData(AbstractModel):
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


class AcceleratorLog(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.logUrl = None
        self.logName = None
        self.logSize = None

    def _deserialize(self, params):
        self.logUrl = params.get("logUrl")
        self.logName = params.get("logName")
        self.logSize = params.get("logSize")


class AcceleratorAlert(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.alertId = None
        self.alertType = None
        self.labels = None
        self.message = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        self.alertId = params.get("alertId")
        self.alertType = params.get("alertType")
        self.labels = params.get("labels")
        self.message = params.get("message")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class AcceleratorInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.acceleratorType = None
        self.acceleratorName = None
        self.chargeType = None
        self.domain = None
        self.acceleratorStatus = None
        self.cname = None
        self.origin = None
        self.accelerateRegions = None
        self.l4Listeners = None
        self.l7Listeners = None
        self.protocolOpts = None
        self.certificate = None
        self.accessControl = None
        self.healthCheck = None
        self.createTime = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        self.acceleratorType = params.get("acceleratorType")
        self.acceleratorName = params.get("acceleratorName")
        self.chargeType = params.get("chargeType")
        if params.get("domain") is not None:
            self.domain = Domain(params.get("domain"))
        self.acceleratorStatus = params.get("acceleratorStatus")
        self.cname = params.get("cname")
        if params.get("origin") is not None:
            self.origin = OriginInfo(params.get("origin"))
        if params.get("accelerateRegions") is not None:
            self.accelerateRegions = []
            for item in params.get("accelerateRegions"):
                obj = AccelerateRegionInfo(item)
                self.accelerateRegions.append(obj)
        if params.get("l4Listeners") is not None:
            self.l4Listeners = []
            for item in params.get("l4Listeners"):
                obj = AccelerationRuleL4Listener(item)
                self.l4Listeners.append(obj)
        if params.get("l7Listeners") is not None:
            self.l7Listeners = []
            for item in params.get("l7Listeners"):
                obj = AccelerationRuleL7Listener(item)
                self.l7Listeners.append(obj)
        if params.get("protocolOpts") is not None:
            self.protocolOpts = AccelerationRuleProtocolOpts(params.get("protocolOpts"))
        if params.get("certificate") is not None:
            self.certificate = CertificateInfo(params.get("certificate"))
        if params.get("accessControl") is not None:
            self.accessControl = AccessControl(params.get("accessControl"))
        if params.get("healthCheck") is not None:
            self.healthCheck = HealthCheck(params.get("healthCheck"))
        self.createTime = params.get("createTime")
        self.resourceGroupId = params.get("resourceGroupId")


class AccelerateRegion(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.accelerateRegionId = None
        self.bandwidth = None
        self.vip = None

    def _deserialize(self, params):
        self.accelerateRegionId = params.get("accelerateRegionId")
        self.bandwidth = params.get("bandwidth")
        self.vip = params.get("vip")


class AccelerateRegionInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.accelerateRegionId = None
        self.accelerateRegionName = None
        self.accelerateRegionStatus = None
        self.bandwidth = None
        self.vip = None

    def _deserialize(self, params):
        self.accelerateRegionId = params.get("accelerateRegionId")
        self.accelerateRegionName = params.get("accelerateRegionName")
        self.accelerateRegionStatus = params.get("accelerateRegionStatus")
        self.bandwidth = params.get("bandwidth")
        self.vip = params.get("vip")


class AccelerationRuleL4Listener(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.port = None
        self.backPort = None
        self.portRange = None
        self.backPortRange = None
        self.protocol = None

    def _deserialize(self, params):
        self.port = params.get("port")
        self.backPort = params.get("backPort")
        self.portRange = params.get("portRange")
        self.backPortRange = params.get("backPortRange")
        self.protocol = params.get("protocol")


class AccelerationRuleL7Listener(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.port = None
        self.backPort = None
        self.portRange = None
        self.backPortRange = None
        self.protocol = None
        self.backProtocol = None
        self.host = None

    def _deserialize(self, params):
        self.port = params.get("port")
        self.backPort = params.get("backPort")
        self.portRange = params.get("portRange")
        self.backPortRange = params.get("backPortRange")
        self.protocol = params.get("protocol")
        self.backProtocol = params.get("backProtocol")
        self.host = params.get("host")


class AccelerationRuleProtocolOpts(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.toa = None
        self.toaValue = None
        self.websocket = None
        self.proxyProtocol = None
        self.gzip = None
        self.sniCheck = None
        self.httpRedirect = None

    def _deserialize(self, params):
        self.toa = params.get("toa")
        self.toaValue = params.get("toaValue")
        self.websocket = params.get("websocket")
        self.proxyProtocol = params.get("proxyProtocol")
        self.gzip = params.get("gzip")
        self.sniCheck = params.get("sniCheck")
        self.httpRedirect = params.get("httpRedirect")


class AccessControl(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.enable = None
        self.rules = None

    def _deserialize(self, params):
        self.enable = params.get("enable")
        if params.get("rules") is not None:
            self.rules = []
            for item in params.get("rules"):
                obj = AccessControlRule(item)
                self.rules.append(obj)


class AccessControlRule(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.listener = None
        self.directory = None
        self.cidrIp = None
        self.policy = None
        self.note = None

    def _deserialize(self, params):
        self.listener = params.get("listener")
        self.directory = params.get("directory")
        self.cidrIp = params.get("cidrIp")
        self.policy = params.get("policy")
        self.note = params.get("note")


class CertificateInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.certificateId = None
        self.certificateLabel = None
        self.common = None
        self.fingerprint = None
        self.issuer = None
        self.sans = None
        self.algorithm = None
        self.createTime = None
        self.startTime = None
        self.endTime = None
        self.expired = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.certificateId = params.get("certificateId")
        self.certificateLabel = params.get("certificateLabel")
        self.common = params.get("common")
        self.fingerprint = params.get("fingerprint")
        self.issuer = params.get("issuer")
        self.sans = params.get("sans")
        self.algorithm = params.get("algorithm")
        self.createTime = params.get("createTime")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.expired = params.get("expired")
        self.resourceGroupId = params.get("resourceGroupId")


class Domain(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.domain = None
        self.relateDomains = None

    def _deserialize(self, params):
        self.domain = params.get("domain")
        self.relateDomains = params.get("relateDomains")


class HealthCheck(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.enable = None
        self.alarm = None
        self.port = None

    def _deserialize(self, params):
        self.enable = params.get("enable")
        self.alarm = params.get("alarm")
        self.port = params.get("port")


class Origin(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.originRegionId = None
        self.origin = None
        self.backupOrigin = None

    def _deserialize(self, params):
        self.originRegionId = params.get("originRegionId")
        self.origin = params.get("origin")
        self.backupOrigin = params.get("backupOrigin")


class OriginInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.originRegionId = None
        self.origin = None
        self.backupOrigin = None
        self.backupOrigin = None

    def _deserialize(self, params):
        self.originRegionId = params.get("originRegionId")
        self.originRegionName = params.get("originRegionName")
        self.origin = params.get("origin")
        self.backupOrigin = params.get("backupOrigin")


class Region(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.regionId = None
        self.regionName = None

    def _deserialize(self, params):
        self.regionId = params.get("regionId")
        self.regionName = params.get("regionName")


class DescribeAcceleratorMetricsRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.acceleratorId = params.get("acceleratorId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeAcceleratorMetricsResponse(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.requestId = None
        self.dataList = None
        self.speedUnit = None
        self.timeUnit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.speedUnit = params.get("speedUnit")
        self.timeUnit = params.get("timeUnit")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = AcceleratorMetricsData(item)
                self.dataList.append(obj)


class AcceleratorMetricsData(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.requestCount = None
        self.averageDownloadSpeed = None
        self.averageFirstByteTime = None
        self.averageSslHandshakeTime = None
        self.averageRequestTime = None
        self.time = None

    def _deserialize(self, params):
        self.requestCount = params.get("requestCount")
        self.averageDownloadSpeed = params.get("averageDownloadSpeed")
        self.averageFirstByteTime = params.get("averageFirstByteTime")
        self.averageSslHandshakeTime = params.get("averageSslHandshakeTime")
        self.averageRequestTime = params.get("averageRequestTime")
        self.time = params.get("time")

class ModifyResourceGroupBandwidthLimitRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceGroupId = None
        self.enable = None
        self.bandwidth = None

    def _deserialize(self, params):
        self.resourceGroupId = params.get("resourceGroupId")
        self.enable = params.get("enable")
        self.bandwidth = params.get("bandwidth")

class ModifyResourceGroupBandwidthLimitResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.resourceGroupId = params.get("resourceGroupId")

class DescribeResourceGroupsBandwidthLimitRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceGroupIds = None

    def _deserialize(self, params):
        self.resourceGroupIds = params.get("resourceGroupIds")

class DescribeResourceGroupsBandwidthLimitResponse(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.requestId = None
        self.resourceGroups = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("resourceGroups") is not None:
            self.resourceGroups = []
            for item in params.get("resourceGroups"):
                obj = ResourceGroupBandwidthLimitInfo(item)
                self.resourceGroups.append(obj)

class ResourceGroupBandwidthLimitInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceGroupId = None
        self.enable = None
        self.bandwidth = None

    def _deserialize(self, params):
        self.resourceGroupId = params.get("resourceGroupId")
        self.enable = params.get("enable")
        self.bandwidth = params.get("bandwidth")

class DescribeTrafficRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorIds = None
        self.startTime = None
        self.endTime = None
        self.originRegionId = None
        self.accelerateRegionId = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.acceleratorIds = params.get("acceleratorIds")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.originRegionId = params.get("originRegionId")
        self.accelerateRegionId = params.get("accelerateRegionId")
        self.resourceGroupId = params.get("resourceGroupId")

class DescribeTrafficResponse(DescribeAcceleratorTrafficResponse):
   pass


class DescribeStatusCodeRequest(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.acceleratorIds = None
        self.startTime = None
        self.endTime = None
        self.originRegionId = None
        self.accelerateRegionId = None
        self.resourceGroupId = None

    def _deserialize(self, params):
        self.acceleratorIds = params.get("acceleratorIds")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.originRegionId = params.get("originRegionId")
        self.accelerateRegionId = params.get("accelerateRegionId")
        self.resourceGroupId = params.get("resourceGroupId")

class DescribeStatusCodeResponse(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.requestId = None
        self.dataList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = StatusCodeData(item)
                self.dataList.append(obj)


class StatusCodeData(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.detail = None
        self.time = None

    def _deserialize(self, params):
        self.time = params.get("time")
        if params.get("detail") is not None:
            self.detail = []
            for item in params.get("detail"):
                obj = StatusCodeDetailData(item)
                self.detail.append(obj)

class StatusCodeDetailData(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.code = None
        self.count = None

    def _deserialize(self, params):
        self.code = params.get("code")
        self.count = params.get("count")
