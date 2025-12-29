#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class AddPrivateZoneRequest(AbstractModel):
    def __init__(self):
        self.zoneName = None
        self.proxyPattern = None
        self.vpcIds = None
        self.resourceGroupId = None
        self.remark = None
        self.tags = None

    def _deserialize(self, params):
        self.zoneName = params.get("zoneName")
        self.proxyPattern = params.get("proxyPattern")
        self.vpcIds = params.get("vpcIds")
        self.resourceGroupId = params.get("resourceGroupId")
        self.remark = params.get("remark")
        if params.get("tags") is not None:
            self.tags = TagAssociation(params.get("tags"))


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


class AddPrivateZoneResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.zoneId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.zoneId = params.get("zoneId")


class DescribePrivateZonesRequest(AbstractModel):
    def __init__(self):
        self.zoneIds = None
        self.vpcIds = None
        self.zoneName = None
        self.resourceGroupId = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.zoneIds = params.get("zoneIds")
        self.vpcIds = params.get("vpcIds")
        self.zoneName = params.get("zoneName")
        self.resourceGroupId = params.get("resourceGroupId")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribePrivateZonesResponse(AbstractModel):
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
                obj = PrivateZone(item)
                self.dataSet.append(obj)


class PrivateZone(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.zoneId = None
        self.zoneName = None
        self.proxyPattern = None
        self.remark = None
        self.recordCount = None
        self.vpcIds = None
        self.tags = None
        self.resourceGroup = None
        self.createTime = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.zoneName = params.get("zoneName")
        self.proxyPattern = params.get("proxyPattern")
        self.remark = params.get("remark")
        self.recordCount = params.get("recordCount")
        self.vpcIds = params.get("vpcIds")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))
        if params.get("resourceGroup") is not None:
            self.resourceGroup = ResourceGroupInfo(params.get("resourceGroup"))
        self.createTime = params.get("createTime")


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


class ModifyPrivateZoneRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.remark = None
        self.proxyPattern = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.remark = params.get("remark")
        self.proxyPattern = params.get("proxyPattern")


class ModifyPrivateZoneResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeletePrivateZoneRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")


class DeletePrivateZoneResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class BindPrivateZoneVpcRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.vpcIds = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.vpcIds = params.get("vpcIds")


class BindPrivateZoneVpcResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class UnbindPrivateZoneVpcRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.vpcIds = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.vpcIds = params.get("vpcIds")


class UnbindPrivateZoneVpcResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class AddPrivateZoneRecordRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.type = None
        self.recordName = None
        self.value = None
        self.weight = None
        self.ttl = None
        self.priority = None
        self.remark = None
        self.line = None
        self.status = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.type = params.get("type")
        self.recordName = params.get("recordName")
        self.value = params.get("value")
        self.weight = params.get("weight")
        self.ttl = params.get("ttl")
        self.priority = params.get("priority")
        self.remark = params.get("remark")
        self.line = params.get("line")
        self.status = params.get("status")


class AddPrivateZoneRecordResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.recordId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.recordId = params.get("recordId")


class DescribePrivateZoneRecordsRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.recordIds = None
        self.recordName = None
        self.type = None
        self.line = None
        self.status = None
        self.value = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.recordIds = params.get("recordIds")
        self.recordName = params.get("recordName")
        self.type = params.get("type")
        self.line = params.get("line")
        self.status = params.get("status")
        self.value = params.get("value")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribePrivateZoneRecordsResponse(AbstractModel):
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
                obj = PrivateZoneRecord(item)
                self.dataSet.append(obj)


class PrivateZoneRecord(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.recordId = None
        self.zoneId = None
        self.type = None
        self.recordName = None
        self.value = None
        self.weight = None
        self.ttl = None
        self.line = None
        self.lineInfo = None
        self.priority = None
        self.remark = None
        self.status = None
        self.createTime = None

    def _deserialize(self, params):
        self.recordId = params.get("recordId")
        self.zoneId = params.get("zoneId")
        self.type = params.get("type")
        self.recordName = params.get("recordName")
        self.value = params.get("value")
        self.weight = params.get("weight")
        self.ttl = params.get("ttl")
        self.line = params.get("line")
        if params.get("lineInfo") is not None:
            self.lineInfo = LineInfo(params.get("lineInfo"))
        self.priority = params.get("priority")
        self.remark = params.get("remark")
        self.status = params.get("status")
        self.createTime = params.get("createTime")


class LineInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.line = None
        self.city = None

    def _deserialize(self, params):
        self.line = params.get("line")
        self.city = params.get("city")


class ModifyPrivateZoneRecordRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.recordId = None
        self.value = None
        self.weight = None
        self.ttl = None
        self.priority = None
        self.remark = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.recordId = params.get("recordId")
        self.value = params.get("value")
        self.weight = params.get("weight")
        self.ttl = params.get("ttl")
        self.priority = params.get("priority")
        self.remark = params.get("remark")


class ModifyPrivateZoneRecordResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyPrivateZoneRecordsStatusRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.recordIds = None
        self.status = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.recordIds = params.get("recordIds")
        self.status = params.get("status")


class ModifyPrivateZoneRecordsStatusResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeletePrivateZoneRecordRequest(AbstractModel):
    def __init__(self):
        self.zoneId = None
        self.recordIds = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.recordIds = params.get("recordIds")


class DeletePrivateZoneRecordResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


