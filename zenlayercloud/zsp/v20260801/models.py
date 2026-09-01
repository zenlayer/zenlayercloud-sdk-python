#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel
import warnings

class DescribeTicketsRequest(AbstractModel):
    def __init__(self):
        self.ticketNumber = None
        self.type = None
        self.description = None
        self.statuses = None
        self.startTime = None
        self.endTime = None
        self.createTimeDesc = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.ticketNumber = params.get("ticketNumber")
        self.type = params.get("type")
        self.description = params.get("description")
        self.statuses = params.get("statuses")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")
        self.createTimeDesc = params.get("createTimeDesc")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeTicketsResponse(AbstractModel):
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
                obj = TicketItem(item)
                self.dataSet.append(obj)


class TicketItem(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.ticketId = None
        self.ticketNumber = None
        self.type = None
        self.status = None
        self.description = None
        self.createTime = None

    def _deserialize(self, params):
        self.ticketId = params.get("ticketId")
        self.ticketNumber = params.get("ticketNumber")
        self.type = params.get("type")
        self.status = params.get("status")
        self.description = params.get("description")
        self.createTime = params.get("createTime")


class CreateTicketRequest(AbstractModel):
    def __init__(self):
        self.type = None
        self.description = None
        self.contactName = None
        self.contactEmail = None
        self.contactPhone = None

    def _deserialize(self, params):
        self.type = params.get("type")
        self.description = params.get("description")
        self.contactName = params.get("contactName")
        self.contactEmail = params.get("contactEmail")
        self.contactPhone = params.get("contactPhone")


class CreateTicketResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.ticketId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.ticketId = params.get("ticketId")


class DescribeTicketDetailRequest(AbstractModel):
    def __init__(self):
        self.ticketId = None

    def _deserialize(self, params):
        self.ticketId = params.get("ticketId")


class DescribeTicketDetailResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.ticketId = None
        self.ticketNumber = None
        self.type = None
        self.status = None
        self.description = None
        self.contactName = None
        self.contactEmail = None
        self.contactPhone = None
        self.createTime = None
        self.messages = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.ticketId = params.get("ticketId")
        self.ticketNumber = params.get("ticketNumber")
        self.type = params.get("type")
        self.status = params.get("status")
        self.description = params.get("description")
        self.contactName = params.get("contactName")
        self.contactEmail = params.get("contactEmail")
        self.contactPhone = params.get("contactPhone")
        self.createTime = params.get("createTime")
        if params.get("messages") is not None:
            self.messages = []
            for item in params.get("messages"):
                obj = TicketMessage(item)
                self.messages.append(obj)


class TicketMessage(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.subject = None
        self.content = None
        self.fromName = None
        self.fromAddress = None
        self.toAddress = None
        self.ccAddress = None
        self.messageDate = None

    def _deserialize(self, params):
        self.subject = params.get("subject")
        self.content = params.get("content")
        self.fromName = params.get("fromName")
        self.fromAddress = params.get("fromAddress")
        self.toAddress = params.get("toAddress")
        self.ccAddress = params.get("ccAddress")
        self.messageDate = params.get("messageDate")


class DescribeTicketCreationQuotaRequest(AbstractModel):
    def __init__(self):
        pass

    def _deserialize(self, params):
        pass


class DescribeTicketCreationQuotaResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.canCreate = None
        self.createdCountLastHour = None
        self.limitPerHour = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.canCreate = params.get("canCreate")
        self.createdCountLastHour = params.get("createdCountLastHour")
        self.limitPerHour = params.get("limitPerHour")


