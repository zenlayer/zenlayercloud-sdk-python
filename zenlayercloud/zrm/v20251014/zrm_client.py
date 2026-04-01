#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zrm.v20251014 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZrmClient(AbstractClient):
    _api_version = "2025-10-14"
    _service = "zrm"

    def DescribeTags(self, request):
        """
        获取某个资源下绑定的所有标签列表。
        """
        response = self._api_call("DescribeTags", request)
        model = models.DescribeTagsResponse()
        model._deserialize(response)
        return model

    def CreateTags(self, request):
        """
        批量创建标签。
        """
        response = self._api_call("CreateTags", request)
        model = models.CreateTagsResponse()
        model._deserialize(response)
        return model

    def DeleteTags(self, request):
        """
        批量删除标签。
        """
        response = self._api_call("DeleteTags", request)
        model = models.DeleteTagsResponse()
        model._deserialize(response)
        return model

    def DescribeResourceTags(self, request):
        """
        获取某个资源下绑定的所有标签列表。
        """
        response = self._api_call("DescribeResourceTags", request)
        model = models.DescribeResourceTagsResponse()
        model._deserialize(response)
        return model

    def ModifyResourceTags(self, request):
        """
        修改某个资源的标签。
        """
        response = self._api_call("ModifyResourceTags", request)
        model = models.ModifyResourceTagsResponse()
        model._deserialize(response)
        return model

    def TagBindResources(self, request):
        """
        标签批量绑定资源。
        """
        response = self._api_call("TagBindResources", request)
        model = models.TagBindResourcesResponse()
        model._deserialize(response)
        return model

    def TagUnbindResources(self, request):
        """
        标签批量解绑资源。
        """
        response = self._api_call("TagUnbindResources", request)
        model = models.TagUnbindResourcesResponse()
        model._deserialize(response)
        return model

    def DescribeResourceByTags(self, request):
        """
        获取标签下绑定的所有资源列表。
        """
        response = self._api_call("DescribeResourceByTags", request)
        model = models.DescribeResourceByTagsResponse()
        model._deserialize(response)
        return model

