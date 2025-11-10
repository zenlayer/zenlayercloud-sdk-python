#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class CreateCommandRequest(AbstractModel):
    def __init__(self):
        self.name = None
        self.content = None
        self.type = None
        self.description = None
        self.resourceGroupId = None
        self.tags = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.content = params.get("content")
        self.type = params.get("type")
        self.description = params.get("description")
        self.resourceGroupId = params.get("resourceGroupId")
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


class CreateCommandResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.commandId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.commandId = params.get("commandId")


class DescribeCommandsRequest(AbstractModel):
    def __init__(self):
        self.commandIds = None
        self.name = None
        self.types = None
        self.pageSize = None
        self.pageNum = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.commandIds = params.get("commandIds")
        self.name = params.get("name")
        self.types = params.get("types")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeCommandsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataSet = None
        self.totalCount = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = Command(item)
                self.dataSet.append(obj)
        self.totalCount = params.get("totalCount")


class Command(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.commandId = None
        self.name = None
        self.description = None
        self.content = None
        self.type = None
        self.createTime = None
        self.latestInvocationTime = None
        self.tags = None
        self.resourceGroup = None

    def _deserialize(self, params):
        self.commandId = params.get("commandId")
        self.name = params.get("name")
        self.description = params.get("description")
        self.content = params.get("content")
        self.type = params.get("type")
        self.createTime = params.get("createTime")
        self.latestInvocationTime = params.get("latestInvocationTime")
        if params.get("tags") is not None:
            self.tags = Tags(params.get("tags"))
        if params.get("resourceGroup") is not None:
            self.resourceGroup = ResourceGroupInfo(params.get("resourceGroup"))


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


class ModifyCommandRequest(AbstractModel):
    def __init__(self):
        self.commandId = None
        self.name = None
        self.content = None
        self.description = None

    def _deserialize(self, params):
        self.commandId = params.get("commandId")
        self.name = params.get("name")
        self.content = params.get("content")
        self.description = params.get("description")


class ModifyCommandResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteCommandRequest(AbstractModel):
    def __init__(self):
        self.commandId = None

    def _deserialize(self, params):
        self.commandId = params.get("commandId")


class DeleteCommandResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class InvokeCommandRequest(AbstractModel):
    def __init__(self):
        self.commandId = None
        self.instanceIds = None
        self.timeout = None

    def _deserialize(self, params):
        self.commandId = params.get("commandId")
        self.instanceIds = params.get("instanceIds")
        self.timeout = params.get("timeout")


class InvokeCommandResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.invocationId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.invocationId = params.get("invocationId")


class DescribeCommandInvocationsRequest(AbstractModel):
    def __init__(self):
        self.commandIds = None
        self.invocationIds = None
        self.instanceIds = None
        self.invocationStatuses = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.commandIds = params.get("commandIds")
        self.invocationIds = params.get("invocationIds")
        self.instanceIds = params.get("instanceIds")
        self.invocationStatuses = params.get("invocationStatuses")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeCommandInvocationsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.dataSet = None
        self.totalCount = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = CommandInvocation(item)
                self.dataSet.append(obj)
        self.totalCount = params.get("totalCount")


class CommandInvocation(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.invocationId = None
        self.commandId = None
        self.commandName = None
        self.commandType = None
        self.content = None
        self.timeout = None
        self.createTime = None
        self.invocationStatus = None
        self.invocationInstances = None

    def _deserialize(self, params):
        self.invocationId = params.get("invocationId")
        self.commandId = params.get("commandId")
        self.commandName = params.get("commandName")
        self.commandType = params.get("commandType")
        self.content = params.get("content")
        self.timeout = params.get("timeout")
        self.createTime = params.get("createTime")
        self.invocationStatus = params.get("invocationStatus")
        if params.get("invocationInstances") is not None:
            self.invocationInstances = []
            for item in params.get("invocationInstances"):
                obj = InvocationInstance(item)
                self.invocationInstances.append(obj)


class InvocationInstance(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.instanceId = None
        self.instanceName = None
        self.instanceExist = None
        self.taskStatus = None
        self.exitCode = None
        self.errorCode = None
        self.output = None
        self.outputError = None
        self.execStartTime = None
        self.execEndTime = None

    def _deserialize(self, params):
        self.instanceId = params.get("instanceId")
        self.instanceName = params.get("instanceName")
        self.instanceExist = params.get("instanceExist")
        self.taskStatus = params.get("taskStatus")
        self.exitCode = params.get("exitCode")
        self.errorCode = params.get("errorCode")
        self.output = params.get("output")
        self.outputError = params.get("outputError")
        self.execStartTime = params.get("execStartTime")
        self.execEndTime = params.get("execEndTime")


