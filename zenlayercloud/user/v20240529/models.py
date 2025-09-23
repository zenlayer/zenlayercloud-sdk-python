#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel

class DescribeResourceGroupsRequest(AbstractModel):
    pass

class DescribeResourceGroupsResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.resourceGroups = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("resourceGroups") is not None:
            self.resourceGroups = []
            for item in params.get("resourceGroups"):
                obj = ResourceGroupInfo(item)
                self.resourceGroups.append(obj)


class ResourceGroupInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceGroupId = None
        self.name = None
        self.createTime = None

    def _deserialize(self, params):
        self.resourceGroupId = params.get("resourceGroupId")
        self.name = params.get("name")
        self.createTime = params.get("createTime")



class DescribeResourceTypesRequest(AbstractModel):
    pass

class DescribeResourceTypesResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.resourceTypeList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.resourceTypeList = params.get("resourceTypeList")



class DescribeResourcesByGroupRequest(AbstractModel):

    def __init__(self):
        self.pageNum = None
        self.pageSize = None
        self.resourceGroupId = None
        self.resourceType = None
        self.updateTimeSort = None

    def _deserialize(self, params):
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceType = params.get("resourceType")
        self.updateTimeSort = params.get("updateTimeSort")


class DescribeResourcesByGroupResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.pageNum = None
        self.pageSize = None
        self.total = None
        self.list = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.total = params.get("total")
        if params.get("list") is not None:
            self.list = []
            for item in params.get("list"):
                obj = ResourceInfo(item)
                self.list.append(obj)


class ResourceInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceId = None
        self.name = None
        self.aliasName = None
        self.resourceType = None
        self.createTime = None
        self.updateTime = None

    def _deserialize(self, params):
        self.resourceId = params.get("resourceId")
        self.name = params.get("name")
        self.aliasName = params.get("aliasName")
        self.resourceType = params.get("resourceType")
        self.createTime = params.get("createTime")
        self.updateTime = params.get("updateTime")


class CreateResourceGroupRequest(AbstractModel):

    def __init__(self):
        self.name = None

    def _deserialize(self, params):
        self.name = params.get("name")


class CreateResourceGroupResponse(AbstractModel):

    def __init__(self):
        self.name = None
        self.resourceGroupId = None
        self.createTime = None

    def _deserialize(self, params):
        self.name = params.get("name")
        self.createTime = params.get("createTime")
        self.resourceGroupId = params.get("resourceGroupId")

class AddResourceResourceGroupRequest(AbstractModel):

    def __init__(self):
        self.resources = None
        self.resourceGroupId = None


    def _deserialize(self, params):
        self.resources = params.get("resources")
        self.resourceGroupId = params.get("resourceGroupId")


class AddResourceResourceGroupResponse(AbstractModel):

    def __init__(self):
        self.requestId = None


    def _deserialize(self, params):
        self.requestId = params.get("requestId")

class DeleteResourceGroupRequest(AbstractModel):

    def __init__(self):
        self.resourceGroupId = None


    def _deserialize(self, params):
        self.resourceGroupId = params.get("resourceGroupId")

class DeleteResourceGroupResponse(AbstractModel):

    def __init__(self):
        self.requestId = None


    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class ModifyResourceGroupRequest(AbstractModel):

    def __init__(self):
        self.resourceGroupId = None
        self.name = None

    def _deserialize(self, params):
        self.resourceGroupId = params.get("resourceGroupId")
        self.name = params.get("name")

class ModifyResourceGroupResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.name = None
        self.resourceGroupId = None
        self.createTime = None


    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.name = params.get("name")
        self.createTime = params.get("createTime")
        self.resourceGroupId = params.get("resourceGroupId")



