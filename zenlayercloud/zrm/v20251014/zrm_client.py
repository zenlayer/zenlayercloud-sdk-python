#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zrm.v20251014 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZrmClient(AbstractClient):
    _api_version = "2025-10-14"
    _service = "zrm"

    def CreateTags(self, request):
        response = self._api_call("CreateTags", request)
        model = models.CreateTagsResponse()
        model._deserialize(response)
        return model

    def DeleteTags(self, request):
        response = self._api_call("DeleteTags", request)
        model = models.DeleteTagsResponse()
        model._deserialize(response)
        return model

    def DescribeTags(self, request):
        response = self._api_call("DescribeTags", request)
        model = models.DescribeTagsResponse()
        model._deserialize(response)
        return model

    def TagBindResources(self, request):
        response = self._api_call("TagBindResources", request)
        model = models.TagBindResourcesResponse()
        model._deserialize(response)
        return model

    def TagUnbindResources(self, request):
        response = self._api_call("TagUnbindResources", request)
        model = models.TagUnbindResourcesResponse()
        model._deserialize(response)
        return model

    def DescribeResourceTags(self, request):
        response = self._api_call("DescribeResourceTags", request)
        model = models.DescribeResourceTagsResponse()
        model._deserialize(response)
        return model

