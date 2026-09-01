#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zos.v20251010 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZosClient(AbstractClient):
    _api_version = "2025-10-10"
    _service = "zos"

    def DescribeCommands(self, request):
        """
        查询命令列表。
        """
        response = self._api_call("DescribeCommands", request)
        model = models.DescribeCommandsResponse()
        model._deserialize(response)
        return model

    def CreateCommand(self, request):
        """
        创建命令。
        """
        response = self._api_call("CreateCommand", request)
        model = models.CreateCommandResponse()
        model._deserialize(response)
        return model

    def InvokeCommand(self, request):
        """
        执行一个已经创建并保存的命令。
        """
        response = self._api_call("InvokeCommand", request)
        model = models.InvokeCommandResponse()
        model._deserialize(response)
        return model

    def ModifyCommand(self, request):
        """
        修改命令。
        """
        response = self._api_call("ModifyCommand", request)
        model = models.ModifyCommandResponse()
        model._deserialize(response)
        return model

    def DeleteCommand(self, request):
        """
        删除命令。
        """
        response = self._api_call("DeleteCommand", request)
        model = models.DeleteCommandResponse()
        model._deserialize(response)
        return model

    def DescribeCommandInvocations(self, request):
        """
        查询执行记录列表。
        """
        response = self._api_call("DescribeCommandInvocations", request)
        model = models.DescribeCommandInvocationsResponse()
        model._deserialize(response)
        return model

