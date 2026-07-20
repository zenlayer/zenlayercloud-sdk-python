#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.sdn.v20260401 import models
from zenlayercloud.common.abstract_client import AbstractClient


class SdnClient(AbstractClient):
    _api_version = "2026-04-01"
    _service = "sdn"

    def CreatePort(self, request):
        """
        创建端口
        """
        response = self._api_call("CreatePort", request)
        model = models.CreatePortResponse()
        model._deserialize(response)
        return model

    def DestroyPort(self, request):
        """
        销毁端口
        """
        response = self._api_call("DestroyPort", request)
        model = models.DestroyPortResponse()
        model._deserialize(response)
        return model

    def TerminatePort(self, request):
        """
        终止端口
        """
        response = self._api_call("TerminatePort", request)
        model = models.TerminatePortResponse()
        model._deserialize(response)
        return model

    def RenewPort(self, request):
        """
        恢复端口
        """
        response = self._api_call("RenewPort", request)
        model = models.RenewPortResponse()
        model._deserialize(response)
        return model

    def ModifyPortAttribute(self, request):
        """
        修改端口属性
        """
        response = self._api_call("ModifyPortAttribute", request)
        model = models.ModifyPortAttributeResponse()
        model._deserialize(response)
        return model

    def DescribePorts(self, request):
        """
        获取端口列表
        """
        response = self._api_call("DescribePorts", request)
        model = models.DescribePortsResponse()
        model._deserialize(response)
        return model

    def DescribeDataCenterPortPrice(self, request):
        """
        获取数据中心在售端口类型及价格
        """
        response = self._api_call("DescribeDataCenterPortPrice", request)
        model = models.DescribeDataCenterPortPriceResponse()
        model._deserialize(response)
        return model

    def DescribePortTraffic(self, request):
        """
        查询端口流量
        """
        response = self._api_call("DescribePortTraffic", request)
        model = models.DescribePortTrafficResponse()
        model._deserialize(response)
        return model

    def DescribePortUsableVlan(self, request):
        """
        查询端口可用vlan
        """
        response = self._api_call("DescribePortUsableVlan", request)
        model = models.DescribePortUsableVlanResponse()
        model._deserialize(response)
        return model

    def QueryCloudOnrampPrice(self, request):
        """
        云连接带宽询价
        """
        response = self._api_call("QueryCloudOnrampPrice", request)
        model = models.QueryCloudOnrampPriceResponse()
        model._deserialize(response)
        return model

    def QueryDataCenterPortPrice(self, request):
        """
        数据中心端口询价
        """
        response = self._api_call("QueryDataCenterPortPrice", request)
        model = models.QueryDataCenterPortPriceResponse()
        model._deserialize(response)
        return model

    def QueryDataCenterPortPrices(self, request):
        """
        数据中心端口批量询价
        """
        response = self._api_call("QueryDataCenterPortPrices", request)
        model = models.QueryDataCenterPortPricesResponse()
        model._deserialize(response)
        return model

    def QueryPrivateConnectPrice(self, request):
        """
        二层网络专线询价
        """
        response = self._api_call("QueryPrivateConnectPrice", request)
        model = models.QueryPrivateConnectPriceResponse()
        model._deserialize(response)
        return model

    def QueryPrivateConnectBandwidthPrice(self, request):
        """
        二层专线带宽询价
        """
        response = self._api_call("QueryPrivateConnectBandwidthPrice", request)
        model = models.QueryPrivateConnectBandwidthPriceResponse()
        model._deserialize(response)
        return model

    def QueryCloudRouterBandwidthPrice(self, request):
        """
        三层骨干带宽询价
        """
        response = self._api_call("QueryCloudRouterBandwidthPrice", request)
        model = models.QueryCloudRouterBandwidthPriceResponse()
        model._deserialize(response)
        return model

    def DescribeGoogleVlanUsage(self, request):
        """
        查询Google接入点VLAN使用情况
        """
        response = self._api_call("DescribeGoogleVlanUsage", request)
        model = models.DescribeGoogleVlanUsageResponse()
        model._deserialize(response)
        return model

    def DescribeTencentVlanUsage(self, request):
        """
        查询腾讯云接入点VLAN使用情况
        """
        response = self._api_call("DescribeTencentVlanUsage", request)
        model = models.DescribeTencentVlanUsageResponse()
        model._deserialize(response)
        return model

    def DescribeAliCloudVlanUsage(self, request):
        """
        查询阿里云接入点VLAN使用情况
        """
        response = self._api_call("DescribeAliCloudVlanUsage", request)
        model = models.DescribeAliCloudVlanUsageResponse()
        model._deserialize(response)
        return model

    def DescribeHuaweiCloudVlanUsage(self, request):
        """
        查询华为云接入点VLAN使用情况
        """
        response = self._api_call("DescribeHuaweiCloudVlanUsage", request)
        model = models.DescribeHuaweiCloudVlanUsageResponse()
        model._deserialize(response)
        return model

    def DescribeAzureVlanUsage(self, request):
        """
        查询Azure接入点VLAN使用情况
        """
        response = self._api_call("DescribeAzureVlanUsage", request)
        model = models.DescribeAzureVlanUsageResponse()
        model._deserialize(response)
        return model

    def DescribeOracleVlanUsage(self, request):
        """
        查询Oracle接入点VLAN使用情况
        """
        response = self._api_call("DescribeOracleVlanUsage", request)
        model = models.DescribeOracleVlanUsageResponse()
        model._deserialize(response)
        return model

    def DescribeBytePlusVlanUsage(self, request):
        """
        查询BytePlus接入点VLAN使用情况
        """
        response = self._api_call("DescribeBytePlusVlanUsage", request)
        model = models.DescribeBytePlusVlanUsageResponse()
        model._deserialize(response)
        return model

    def ModifyCloudBandwidth(self, request):
        """
        修改云连接带宽
        """
        response = self._api_call("ModifyCloudBandwidth", request)
        model = models.ModifyCloudBandwidthResponse()
        model._deserialize(response)
        return model

    def DescribeCloudAvailableBandwidthTiers(self, request):
        """
        查询云连接可用带宽阶梯
        """
        response = self._api_call("DescribeCloudAvailableBandwidthTiers", request)
        model = models.DescribeCloudAvailableBandwidthTiersResponse()
        model._deserialize(response)
        return model

    def DescribeAWSRegions(self, request):
        """
        查询AWS接入点区域
        """
        response = self._api_call("DescribeAWSRegions", request)
        model = models.DescribeAWSRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeTencentRegions(self, request):
        """
        查询腾讯云接入点区域
        """
        response = self._api_call("DescribeTencentRegions", request)
        model = models.DescribeTencentRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeGoogleRegions(self, request):
        """
        查询Google接入点区域
        """
        response = self._api_call("DescribeGoogleRegions", request)
        model = models.DescribeGoogleRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeAzureRegions(self, request):
        """
        查询Azure接入点区域
        """
        response = self._api_call("DescribeAzureRegions", request)
        model = models.DescribeAzureRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeOracleRegions(self, request):
        """
        查询Oracle接入点区域
        """
        response = self._api_call("DescribeOracleRegions", request)
        model = models.DescribeOracleRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeAliCloudRegions(self, request):
        """
        查询阿里云接入点区域
        """
        response = self._api_call("DescribeAliCloudRegions", request)
        model = models.DescribeAliCloudRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeHuaweiCloudRegions(self, request):
        """
        查询华为云接入点区域
        """
        response = self._api_call("DescribeHuaweiCloudRegions", request)
        model = models.DescribeHuaweiCloudRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeBytePlusRegions(self, request):
        """
        查询BytePlus接入点区域
        """
        response = self._api_call("DescribeBytePlusRegions", request)
        model = models.DescribeBytePlusRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeAWSVlanUsage(self, request):
        """
        查询AWS接入点VLAN使用情况
        """
        response = self._api_call("DescribeAWSVlanUsage", request)
        model = models.DescribeAWSVlanUsageResponse()
        model._deserialize(response)
        return model

    def CreateCloudRouter(self, request):
        """
        创建三层网络
        """
        response = self._api_call("CreateCloudRouter", request)
        model = models.CreateCloudRouterResponse()
        model._deserialize(response)
        return model

    def DeleteCloudRouterEdgePoint(self, request):
        """
        删除连接点
        """
        response = self._api_call("DeleteCloudRouterEdgePoint", request)
        model = models.DeleteCloudRouterEdgePointResponse()
        model._deserialize(response)
        return model

    def AddCloudRouterEdgePoints(self, request):
        """
        新增连接点
        """
        response = self._api_call("AddCloudRouterEdgePoints", request)
        model = models.AddCloudRouterEdgePointsResponse()
        model._deserialize(response)
        return model

    def ModifyCloudRoutersAttribute(self, request):
        """
        修改三层网络属性
        """
        response = self._api_call("ModifyCloudRoutersAttribute", request)
        model = models.ModifyCloudRoutersAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeCloudRouterAvailableVpcs(self, request):
        """
        查询可用VPC
        """
        response = self._api_call("DescribeCloudRouterAvailableVpcs", request)
        model = models.DescribeCloudRouterAvailableVpcsResponse()
        model._deserialize(response)
        return model

    def DescribeCloudRouterEdgePointTraffic(self, request):
        """
        查询连接点流量
        """
        response = self._api_call("DescribeCloudRouterEdgePointTraffic", request)
        model = models.DescribeCloudRouterEdgePointTrafficResponse()
        model._deserialize(response)
        return model

    def DescribeCloudRouterDCToDCTraffic(self, request):
        """
        查询数据中心间流量
        """
        response = self._api_call("DescribeCloudRouterDCToDCTraffic", request)
        model = models.DescribeCloudRouterDCToDCTrafficResponse()
        model._deserialize(response)
        return model

    def ModifyCloudRouterEdgePointBandwidth(self, request):
        """
        修改连接点带宽
        """
        response = self._api_call("ModifyCloudRouterEdgePointBandwidth", request)
        model = models.ModifyCloudRouterEdgePointBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyCloudRouterEdgePoint(self, request):
        """
        修改连接点配置
        """
        response = self._api_call("ModifyCloudRouterEdgePoint", request)
        model = models.ModifyCloudRouterEdgePointResponse()
        model._deserialize(response)
        return model

    def DeleteCloudRouter(self, request):
        """
        删除三层网络
        """
        response = self._api_call("DeleteCloudRouter", request)
        model = models.DeleteCloudRouterResponse()
        model._deserialize(response)
        return model

    def DestroyCloudRouter(self, request):
        """
        销毁三层网络
        """
        response = self._api_call("DestroyCloudRouter", request)
        model = models.DestroyCloudRouterResponse()
        model._deserialize(response)
        return model

    def RenewCloudRouter(self, request):
        """
        恢复三层网络
        """
        response = self._api_call("RenewCloudRouter", request)
        model = models.RenewCloudRouterResponse()
        model._deserialize(response)
        return model

    def DescribeCloudRouterAvailablePorts(self, request):
        """
        查询可用端口
        """
        response = self._api_call("DescribeCloudRouterAvailablePorts", request)
        model = models.DescribeCloudRouterAvailablePortsResponse()
        model._deserialize(response)
        return model

    def DescribeCloudRouters(self, request):
        """
        查询三层网络列表
        """
        response = self._api_call("DescribeCloudRouters", request)
        model = models.DescribeCloudRoutersResponse()
        model._deserialize(response)
        return model

    def DescribeDatacenters(self, request):
        """
        查询数据中心列表
        """
        response = self._api_call("DescribeDatacenters", request)
        model = models.DescribeDatacentersResponse()
        model._deserialize(response)
        return model

    def DescribeVirtualEdgeDatacenters(self, request):
        """
        查询边缘网关数据中心列表
        """
        response = self._api_call("DescribeVirtualEdgeDatacenters", request)
        model = models.DescribeVirtualEdgeDatacentersResponse()
        model._deserialize(response)
        return model

    def DescribeBorderGatewayDatacenters(self, request):
        """
        查询边界网关数据中心列表
        """
        response = self._api_call("DescribeBorderGatewayDatacenters", request)
        model = models.DescribeBorderGatewayDatacentersResponse()
        model._deserialize(response)
        return model

    def DescribeVPCDatacenters(self, request):
        """
        查询 VPC 数据中心列表
        """
        response = self._api_call("DescribeVPCDatacenters", request)
        model = models.DescribeVPCDatacentersResponse()
        model._deserialize(response)
        return model

    def DescribeDatacentersWithService(self, request):
        """
        查询含服务的数据中心列表
        """
        response = self._api_call("DescribeDatacentersWithService", request)
        model = models.DescribeDatacentersWithServiceResponse()
        model._deserialize(response)
        return model

    def DescribePrivateConnects(self, request):
        """
        获取二层网络专线列表
        """
        response = self._api_call("DescribePrivateConnects", request)
        model = models.DescribePrivateConnectsResponse()
        model._deserialize(response)
        return model

    def CreatePrivateConnect(self, request):
        """
        创建二层网络专线
        """
        response = self._api_call("CreatePrivateConnect", request)
        model = models.CreatePrivateConnectResponse()
        model._deserialize(response)
        return model

    def ModifyPrivateConnectBandwidth(self, request):
        """
        修改二层网络专线带宽
        """
        response = self._api_call("ModifyPrivateConnectBandwidth", request)
        model = models.ModifyPrivateConnectBandwidthResponse()
        model._deserialize(response)
        return model

    def DescribePrivateConnectTraffic(self, request):
        """
        查询二层网络专线流量
        """
        response = self._api_call("DescribePrivateConnectTraffic", request)
        model = models.DescribePrivateConnectTrafficResponse()
        model._deserialize(response)
        return model

    def DeletePrivateConnect(self, request):
        """
        删除二层网络专线
        """
        response = self._api_call("DeletePrivateConnect", request)
        model = models.DeletePrivateConnectResponse()
        model._deserialize(response)
        return model

    def DestroyPrivateConnect(self, request):
        """
        销毁二层网络专线
        """
        response = self._api_call("DestroyPrivateConnect", request)
        model = models.DestroyPrivateConnectResponse()
        model._deserialize(response)
        return model

    def DescribePrivateConnectAvailablePorts(self, request):
        """
        查询可加入的数据中心端口
        """
        response = self._api_call("DescribePrivateConnectAvailablePorts", request)
        model = models.DescribePrivateConnectAvailablePortsResponse()
        model._deserialize(response)
        return model

    def ModifyPrivateConnectsAttribute(self, request):
        """
        修改二层网络专线属性
        """
        response = self._api_call("ModifyPrivateConnectsAttribute", request)
        model = models.ModifyPrivateConnectsAttributeResponse()
        model._deserialize(response)
        return model

    def RenewPrivateConnect(self, request):
        """
        恢复二层网络专线
        """
        response = self._api_call("RenewPrivateConnect", request)
        model = models.RenewPrivateConnectResponse()
        model._deserialize(response)
        return model

    def InquiryCreatePrivateConnectPrice(self, request):
        """
        二层网络专线询价
        """
        response = self._api_call("InquiryCreatePrivateConnectPrice", request)
        model = models.InquiryCreatePrivateConnectPriceResponse()
        model._deserialize(response)
        return model

