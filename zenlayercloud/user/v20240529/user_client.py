#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.user.v20240529 import models
from zenlayercloud.common.abstract_client import AbstractClient


class UserClient(AbstractClient):
    _api_version = "2024-05-29"
    _service = "user"

    def DescribeResourceGroups(self, request):
        response = self._api_call("DescribeResourceGroups", request)

        model = models.DescribeResourceGroupsResponse()
        model._deserialize(response)
        return model


    def DescribeResourceTypes(self, request):
        response = self._api_call("DescribeResourceTypes", request)

        model = models.DescribeResourceTypesResponse()
        model._deserialize(response)
        return model


    def DescribeResourcesByGroup(self, request):
        response = self._api_call("DescribeResourcesByGroup", request)

        model = models.DescribeResourcesByGroupResponse()
        model._deserialize(response)
        return model

