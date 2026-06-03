#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.mcpgw.v20260602 import models
from zenlayercloud.common.abstract_client import AbstractClient


class McpgwClient(AbstractClient):
    _api_version = "2026-06-02"
    _service = "mcpgw"

    def DescribeMcpMonthlyBilling(self, request):
        """
        查询MCP网关按月计费明细
        """
        response = self._api_call("DescribeMcpMonthlyBilling", request)
        model = models.DescribeMcpMonthlyBillingResponse()
        model._deserialize(response)
        return model

