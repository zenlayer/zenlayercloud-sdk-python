#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.ccs.v20250901 import models
from zenlayercloud.common.abstract_client import AbstractClient


class CcsClient(AbstractClient):
    _api_version = "2025-09-01"
    _service = "ccs"

    def DescribeKeyPairs(self, request):
        response = self._api_call("DescribeKeyPairs", request)
        model = models.DescribeKeyPairsResponse()
        model._deserialize(response)
        return model

    def ImportKeyPair(self, request):
        response = self._api_call("ImportKeyPair", request)
        model = models.ImportKeyPairResponse()
        model._deserialize(response)
        return model

    def ModifyKeyPairAttribute(self, request):
        response = self._api_call("ModifyKeyPairAttribute", request)
        model = models.ModifyKeyPairAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteKeyPairs(self, request):
        response = self._api_call("DeleteKeyPairs", request)
        model = models.DeleteKeyPairsResponse()
        model._deserialize(response)
        return model

