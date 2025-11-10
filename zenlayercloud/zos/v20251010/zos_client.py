#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zos.v20251010 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZOSClient(AbstractClient):
    _api_version = "2025-10-10"
    _service = "zos"

    def CreateCommand(self, request):
        response = self._api_call("CreateCommand", request)
        model = models.CreateCommandResponse()
        model._deserialize(response)
        return model

    def DescribeCommands(self, request):
        response = self._api_call("DescribeCommands", request)
        model = models.DescribeCommandsResponse()
        model._deserialize(response)
        return model

    def ModifyCommand(self, request):
        response = self._api_call("ModifyCommand", request)
        model = models.ModifyCommandResponse()
        model._deserialize(response)
        return model

    def DeleteCommand(self, request):
        response = self._api_call("DeleteCommand", request)
        model = models.DeleteCommandResponse()
        model._deserialize(response)
        return model

    def InvokeCommand(self, request):
        response = self._api_call("InvokeCommand", request)
        model = models.InvokeCommandResponse()
        model._deserialize(response)
        return model

    def DescribeCommandInvocations(self, request):
        response = self._api_call("DescribeCommandInvocations", request)
        model = models.DescribeCommandInvocationsResponse()
        model._deserialize(response)
        return model

