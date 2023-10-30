#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.sdn.v20230830 import models
from zenlayercloud.common.abstract_client import AbstractClient


class SdnClient(AbstractClient):
    _api_version = "2023-08-30"
    _service = "sdn"

    def DescribeDatacenters(self, request):
        response = self._api_call("DescribeDatacenters", request)

        model = models.DescribeDatacentersResponse()
        model._deserialize(response)
        return model

    def CreatePort(self, request):
        response = self._api_call("CreatePort", request)

        model = models.CreatePortResponse()
        model._deserialize(response)
        return model

    def DescribeDataCenterPortPrice(self, request):
        response = self._api_call("DescribeDataCenterPortPrice", request)

        model = models.DescribeDataCenterPortPriceResponse()
        model._deserialize(response)
        return model


    def DescribePorts(self, request):
        response = self._api_call("DescribePorts", request)

        model = models.DescribePortsResponse()
        model._deserialize(response)
        return model


    def DescribePortTraffic(self, request):
        response = self._api_call("DescribePortTraffic", request)

        model = models.DescribePortTrafficResponse()
        model._deserialize(response)
        return model


    def DescribePortUsableVlan(self, request):
        response = self._api_call("DescribePortUsableVlan", request)

        model = models.DescribePortUsableVlanResponse()
        model._deserialize(response)
        return model


    def DestroyPort(self, request):
        response = self._api_call("DestroyPort", request)

        model = models.DestroyPortResponse()
        model._deserialize(response)
        return model

    def ModifyPortAttribute(self, request):
        response = self._api_call("ModifyPortAttribute", request)

        model = models.ModifyPortAttributeResponse()
        model._deserialize(response)
        return model


    def TerminatePort(self, request):
        response = self._api_call("TerminatePort", request)

        model = models.TerminatePortResponse()
        model._deserialize(response)
        return model

    def RenewPort(self, request):
        response = self._api_call("RenewPort", request)

        model = models.RenewPortResponse()
        model._deserialize(response)
        return model

    def DescribePrivateConnects(self, request):
        response = self._api_call("DescribePrivateConnects", request)

        model = models.DescribePrivateConnectsResponse()
        model._deserialize(response)
        return model


    def DescribeCreatePrivateConnectAvailableSubnets(self, request):
        response = self._api_call("DescribeCreatePrivateConnectAvailableSubnets", request)

        model = models.DescribeCreatePrivateConnectAvailableSubnetsResponse()
        model._deserialize(response)
        return model

    def CreatePrivateConnect(self, request):
        response = self._api_call("CreatePrivateConnect", request)

        model = models.CreatePrivateConnectResponse()
        model._deserialize(response)
        return model


    def ModifyPrivateConnectsAttribute(self, request):
        response = self._api_call("ModifyPrivateConnectsAttribute", request)

        model = models.ModifyPrivateConnectsAttributeResponse()
        model._deserialize(response)
        return model


    def InquiryCreatePrivateConnectPrice(self, request):
        response = self._api_call("InquiryCreatePrivateConnectPrice", request)

        model = models.InquiryCreatePrivateConnectPriceResponse()
        model._deserialize(response)
        return model


    def DeletePrivateConnect(self, request):
        response = self._api_call("DeletePrivateConnect", request)

        model = models.DeletePrivateConnectResponse()
        model._deserialize(response)
        return model


    def DestroyPrivateConnect(self, request):
        response = self._api_call("DestroyPrivateConnect", request)

        model = models.DestroyPrivateConnectResponse()
        model._deserialize(response)
        return model


    def RenewPrivateConnect(self, request):
        response = self._api_call("RenewPrivateConnect", request)

        model = models.RenewPrivateConnectResponse()
        model._deserialize(response)
        return model


    def DescribePrivateConnectTraffic(self, request):
        response = self._api_call("DescribePrivateConnectTraffic", request)

        model = models.DescribePrivateConnectTrafficResponse()
        model._deserialize(response)
        return model

    def ModifyPrivateConnectBandwidth(self, request):
        response = self._api_call("ModifyPrivateConnectBandwidth", request)

        model = models.ModifyPrivateConnectBandwidthResponse()
        model._deserialize(response)
        return model


    def DescribeCloudRouters(self, request):
        response = self._api_call("DescribeCloudRouters", request)

        model = models.DescribeCloudRoutersResponse()
        model._deserialize(response)
        return model

    def DescribeCloudRouterAvailableVpcs(self, request):
        response = self._api_call("DescribeCloudRouterAvailableVpcs", request)

        model = models.DescribeCloudRouterAvailableVpcsResponse()
        model._deserialize(response)
        return model


    def DescribeCloudRouterAvailablePorts(self, request):
        response = self._api_call("DescribeCloudRouterAvailablePorts", request)

        model = models.DescribeCloudRouterAvailablePortsResponse()
        model._deserialize(response)
        return model


    def CreateCloudRouter(self, request):
        response = self._api_call("CreateCloudRouter", request)

        model = models.CreateCloudRouterResponse()
        model._deserialize(response)
        return model


    def ModifyCloudRoutersAttribute(self, request):
        response = self._api_call("ModifyCloudRoutersAttribute", request)

        model = models.ModifyCloudRoutersAttributeResponse()
        model._deserialize(response)
        return model

    def AddCloudRouterEdgePoints(self, request):
        response = self._api_call("AddCloudRouterEdgePoints", request)

        model = models.AddCloudRouterEdgePointsResponse()
        model._deserialize(response)
        return model


    def DeleteCloudRouterEdgePoint(self, request):
        response = self._api_call("DeleteCloudRouterEdgePoint", request)

        model = models.DeleteCloudRouterEdgePointResponse()
        model._deserialize(response)
        return model

    def DeleteCloudRouter(self, request):
        response = self._api_call("DeleteCloudRouter", request)

        model = models.DeleteCloudRouterResponse()
        model._deserialize(response)
        return model


    def DestroyCloudRouter(self, request):
        response = self._api_call("DestroyCloudRouter", request)

        model = models.DestroyCloudRouterResponse()
        model._deserialize(response)
        return model

    def RenewCloudRouter(self, request):
        response = self._api_call("RenewCloudRouter", request)

        model = models.RenewCloudRouterResponse()
        model._deserialize(response)
        return model

    def ModifyCloudRouterEdgePointBandwidth(self, request):
        response = self._api_call("ModifyCloudRouterEdgePointBandwidth", request)

        model = models.ModifyCloudRouterEdgePointBandwidthResponse()
        model._deserialize(response)
        return model


    def DescribeCloudRouterEdgePointTraffic(self, request):
        response = self._api_call("DescribeCloudRouterEdgePointTraffic", request)

        model = models.DescribeCloudRouterEdgePointTrafficResponse()
        model._deserialize(response)
        return model

    def ModifyCloudRouterEdgePoint(self, request):
        response = self._api_call("ModifyCloudRouterEdgePoint", request)

        model = models.ModifyCloudRouterEdgePointResponse()
        model._deserialize(response)
        return model
