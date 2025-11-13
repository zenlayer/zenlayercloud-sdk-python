#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class CreateTagsRequest(AbstractModel):
    def __init__(self):
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


class CreateTagsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteTagsRequest(AbstractModel):
    def __init__(self):
        self.tags = None

    def _deserialize(self, params):
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DeleteTagsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeTagsRequest(AbstractModel):
    def __init__(self):
        self.pageNum = None
        self.pageSize = None
        self.keySort = None
        self.createdDateSort = None
        self.tagKeys = None
        self.tags = None

    def _deserialize(self, params):
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.keySort = params.get("keySort")
        self.createdDateSort = params.get("createdDateSort")
        self.tagKeys = params.get("tagKeys")
        if params.get("tags") is not None:
            self.tags = []
            for item in params.get("tags"):
                obj = Tag(item)
                self.tags.append(obj)


class DescribeTagsResponse(AbstractModel):
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
                obj = TagInfo(item)
                self.dataSet.append(obj)


class TagInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.key = None
        self.value = None
        self.bindResourceCount = None
        self.createdDate = None

    def _deserialize(self, params):
        self.key = params.get("key")
        self.value = params.get("value")
        self.bindResourceCount = params.get("bindResourceCount")
        self.createdDate = params.get("createdDate")


class TagBindResourcesRequest(AbstractModel):
    def __init__(self):
        self.tag = None
        self.resourceUuids = None

    def _deserialize(self, params):
        if params.get("tag") is not None:
            self.tag = Tag(params.get("tag"))
        self.resourceUuids = params.get("resourceUuids")


class TagBindResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class TagUnbindResourcesRequest(AbstractModel):
    def __init__(self):
        self.tag = None
        self.resourceUuids = None

    def _deserialize(self, params):
        if params.get("tag") is not None:
            self.tag = Tag(params.get("tag"))
        self.resourceUuids = params.get("resourceUuids")


class TagUnbindResourcesResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DescribeResourceTagsRequest(AbstractModel):
    def __init__(self):
        self.resourceUuid = None

    def _deserialize(self, params):
        self.resourceUuid = params.get("resourceUuid")


class DescribeResourceTagsResponse(AbstractModel):
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
                obj = ResourceTag(item)
                self.dataSet.append(obj)


class ResourceTag(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.key = None
        self.value = None
        self.createdDate = None

    def _deserialize(self, params):
        self.key = params.get("key")
        self.value = params.get("value")
        self.createdDate = params.get("createdDate")


