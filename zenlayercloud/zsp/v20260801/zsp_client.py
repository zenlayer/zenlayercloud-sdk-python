#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zsp.v20260801 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZspClient(AbstractClient):
    _api_version = "2026-08-01"
    _service = "zsp"

    def DescribeTickets(self, request):
        """
        查询当前团队提交的工单列表。
        """
        response = self._api_call("DescribeTickets", request)
        model = models.DescribeTicketsResponse()
        model._deserialize(response)
        return model

    def CreateTicket(self, request):
        """
        创建一个工单。
        """
        response = self._api_call("CreateTicket", request)
        model = models.CreateTicketResponse()
        model._deserialize(response)
        return model

    def DescribeTicketDetail(self, request):
        """
        查询指定工单的详细信息与沟通记录。
        """
        response = self._api_call("DescribeTicketDetail", request)
        model = models.DescribeTicketDetailResponse()
        model._deserialize(response)
        return model

    def DescribeTicketCreationQuota(self, request):
        """
        查询当前团队一小时内是否还可以创建工单。
        """
        response = self._api_call("DescribeTicketCreationQuota", request)
        model = models.DescribeTicketCreationQuotaResponse()
        model._deserialize(response)
        return model

