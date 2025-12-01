#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.pvtdns.v20251101 import models
from zenlayercloud.common.abstract_client import AbstractClient


class PvtdnsClient(AbstractClient):
    _api_version = "2025-11-01"
    _service = "pvtdns"

    def AddPrivateZone(self, request):
        response = self._api_call("AddPrivateZone", request)
        model = models.AddPrivateZoneResponse()
        model._deserialize(response)
        return model

    def DescribePrivateZones(self, request):
        response = self._api_call("DescribePrivateZones", request)
        model = models.DescribePrivateZonesResponse()
        model._deserialize(response)
        return model

    def ModifyPrivateZone(self, request):
        response = self._api_call("ModifyPrivateZone", request)
        model = models.ModifyPrivateZoneResponse()
        model._deserialize(response)
        return model

    def DeletePrivateZone(self, request):
        response = self._api_call("DeletePrivateZone", request)
        model = models.DeletePrivateZoneResponse()
        model._deserialize(response)
        return model

    def BindPrivateZoneVpc(self, request):
        response = self._api_call("BindPrivateZoneVpc", request)
        model = models.BindPrivateZoneVpcResponse()
        model._deserialize(response)
        return model

    def UnbindPrivateZoneVpc(self, request):
        response = self._api_call("UnbindPrivateZoneVpc", request)
        model = models.UnbindPrivateZoneVpcResponse()
        model._deserialize(response)
        return model

    def AddPrivateZoneRecord(self, request):
        response = self._api_call("AddPrivateZoneRecord", request)
        model = models.AddPrivateZoneRecordResponse()
        model._deserialize(response)
        return model

    def DescribePrivateZoneRecords(self, request):
        response = self._api_call("DescribePrivateZoneRecords", request)
        model = models.DescribePrivateZoneRecordsResponse()
        model._deserialize(response)
        return model

    def ModifyPrivateZoneRecord(self, request):
        response = self._api_call("ModifyPrivateZoneRecord", request)
        model = models.ModifyPrivateZoneRecordResponse()
        model._deserialize(response)
        return model

    def ModifyPrivateZoneRecordsStatus(self, request):
        response = self._api_call("ModifyPrivateZoneRecordsStatus", request)
        model = models.ModifyPrivateZoneRecordsStatusResponse()
        model._deserialize(response)
        return model

    def DeletePrivateZoneRecord(self, request):
        response = self._api_call("DeletePrivateZoneRecord", request)
        model = models.DeletePrivateZoneRecordResponse()
        model._deserialize(response)
        return model

