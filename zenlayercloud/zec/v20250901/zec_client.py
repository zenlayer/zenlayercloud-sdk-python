#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zec.v20250901 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZECClient(AbstractClient):
    _api_version = "2025-09-01"
    _service = "zec"

    def DescribeDisks(self, request):
        response = self._api_call("DescribeDisks", request)
        model = models.DescribeDisksResponse()
        model._deserialize(response)
        return model

    def DescribeDiskRegions(self, request):
        response = self._api_call("DescribeDiskRegions", request)
        model = models.DescribeDiskRegionsResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateDisks(self, request):
        response = self._api_call("InquiryPriceCreateDisks", request)
        model = models.InquiryPriceCreateDisksResponse()
        model._deserialize(response)
        return model

    def CreateDisks(self, request):
        response = self._api_call("CreateDisks", request)
        model = models.CreateDisksResponse()
        model._deserialize(response)
        return model

    def AttachDisks(self, request):
        response = self._api_call("AttachDisks", request)
        model = models.AttachDisksResponse()
        model._deserialize(response)
        return model

    def DetachDisks(self, request):
        response = self._api_call("DetachDisks", request)
        model = models.DetachDisksResponse()
        model._deserialize(response)
        return model

    def ModifyDisksAttributes(self, request):
        response = self._api_call("ModifyDisksAttributes", request)
        model = models.ModifyDisksAttributesResponse()
        model._deserialize(response)
        return model

    def ResizeDisk(self, request):
        response = self._api_call("ResizeDisk", request)
        model = models.ResizeDiskResponse()
        model._deserialize(response)
        return model

    def ReleaseDisk(self, request):
        response = self._api_call("ReleaseDisk", request)
        model = models.ReleaseDiskResponse()
        model._deserialize(response)
        return model

    def RenewDisk(self, request):
        response = self._api_call("RenewDisk", request)
        model = models.RenewDiskResponse()
        model._deserialize(response)
        return model

    def ModifyDisksResourceGroup(self, request):
        response = self._api_call("ModifyDisksResourceGroup", request)
        model = models.ModifyDisksResourceGroupResponse()
        model._deserialize(response)
        return model

    def DescribeDiskCategory(self, request):
        response = self._api_call("DescribeDiskCategory", request)
        model = models.DescribeDiskCategoryResponse()
        model._deserialize(response)
        return model

    def DescribeDiskMonitorData(self, request):
        response = self._api_call("DescribeDiskMonitorData", request)
        model = models.DescribeDiskMonitorDataResponse()
        model._deserialize(response)
        return model

    def CreateVpc(self, request):
        response = self._api_call("CreateVpc", request)
        model = models.CreateVpcResponse()
        model._deserialize(response)
        return model

    def DeleteVpc(self, request):
        response = self._api_call("DeleteVpc", request)
        model = models.DeleteVpcResponse()
        model._deserialize(response)
        return model

    def ModifyVpcsAttribute(self, request):
        response = self._api_call("ModifyVpcsAttribute", request)
        model = models.ModifyVpcsAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeSubnetRegions(self, request):
        response = self._api_call("DescribeSubnetRegions", request)
        model = models.DescribeSubnetRegionsResponse()
        model._deserialize(response)
        return model

    def CreateSubnet(self, request):
        response = self._api_call("CreateSubnet", request)
        model = models.CreateSubnetResponse()
        model._deserialize(response)
        return model

    def DeleteSubnet(self, request):
        response = self._api_call("DeleteSubnet", request)
        model = models.DeleteSubnetResponse()
        model._deserialize(response)
        return model

    def ModifySubnetAttribute(self, request):
        response = self._api_call("ModifySubnetAttribute", request)
        model = models.ModifySubnetAttributeResponse()
        model._deserialize(response)
        return model

    def ModifySubnetStackType(self, request):
        response = self._api_call("ModifySubnetStackType", request)
        model = models.ModifySubnetStackTypeResponse()
        model._deserialize(response)
        return model

    def DescribeVpcs(self, request):
        response = self._api_call("DescribeVpcs", request)
        model = models.DescribeVpcsResponse()
        model._deserialize(response)
        return model

    def ModifyVpcAttribute(self, request):
        response = self._api_call("ModifyVpcAttribute", request)
        model = models.ModifyVpcAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeSubnets(self, request):
        response = self._api_call("DescribeSubnets", request)
        model = models.DescribeSubnetsResponse()
        model._deserialize(response)
        return model

    def ModifySubnetsAttribute(self, request):
        response = self._api_call("ModifySubnetsAttribute", request)
        model = models.ModifySubnetsAttributeResponse()
        model._deserialize(response)
        return model

    def CreateSnapshot(self, request):
        response = self._api_call("CreateSnapshot", request)
        model = models.CreateSnapshotResponse()
        model._deserialize(response)
        return model

    def ModifySnapshotsAttribute(self, request):
        response = self._api_call("ModifySnapshotsAttribute", request)
        model = models.ModifySnapshotsAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteSnapshots(self, request):
        response = self._api_call("DeleteSnapshots", request)
        model = models.DeleteSnapshotsResponse()
        model._deserialize(response)
        return model

    def DescribeSnapshots(self, request):
        response = self._api_call("DescribeSnapshots", request)
        model = models.DescribeSnapshotsResponse()
        model._deserialize(response)
        return model

    def ApplySnapshot(self, request):
        response = self._api_call("ApplySnapshot", request)
        model = models.ApplySnapshotResponse()
        model._deserialize(response)
        return model

    def CreateAutoSnapshotPolicy(self, request):
        response = self._api_call("CreateAutoSnapshotPolicy", request)
        model = models.CreateAutoSnapshotPolicyResponse()
        model._deserialize(response)
        return model

    def ApplyAutoSnapshotPolicy(self, request):
        response = self._api_call("ApplyAutoSnapshotPolicy", request)
        model = models.ApplyAutoSnapshotPolicyResponse()
        model._deserialize(response)
        return model

    def CancelAutoSnapshotPolicy(self, request):
        response = self._api_call("CancelAutoSnapshotPolicy", request)
        model = models.CancelAutoSnapshotPolicyResponse()
        model._deserialize(response)
        return model

    def DescribeAutoSnapshotPolicies(self, request):
        response = self._api_call("DescribeAutoSnapshotPolicies", request)
        model = models.DescribeAutoSnapshotPoliciesResponse()
        model._deserialize(response)
        return model

    def ModifyAutoSnapshotPolicy(self, request):
        response = self._api_call("ModifyAutoSnapshotPolicy", request)
        model = models.ModifyAutoSnapshotPolicyResponse()
        model._deserialize(response)
        return model

    def DeleteAutoSnapshotPolicies(self, request):
        response = self._api_call("DeleteAutoSnapshotPolicies", request)
        model = models.DeleteAutoSnapshotPoliciesResponse()
        model._deserialize(response)
        return model

    def DescribeNetworkInterfaceRegions(self, request):
        response = self._api_call("DescribeNetworkInterfaceRegions", request)
        model = models.DescribeNetworkInterfaceRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeNetworkInterfaces(self, request):
        response = self._api_call("DescribeNetworkInterfaces", request)
        model = models.DescribeNetworkInterfacesResponse()
        model._deserialize(response)
        return model

    def ModifyNetworkInterfaceAttribute(self, request):
        response = self._api_call("ModifyNetworkInterfaceAttribute", request)
        model = models.ModifyNetworkInterfaceAttributeResponse()
        model._deserialize(response)
        return model

    def ModifyNetworkInterfacesAttribute(self, request):
        response = self._api_call("ModifyNetworkInterfacesAttribute", request)
        model = models.ModifyNetworkInterfacesAttributeResponse()
        model._deserialize(response)
        return model

    def CreateNetworkInterface(self, request):
        response = self._api_call("CreateNetworkInterface", request)
        model = models.CreateNetworkInterfaceResponse()
        model._deserialize(response)
        return model

    def DeleteNetworkInterface(self, request):
        response = self._api_call("DeleteNetworkInterface", request)
        model = models.DeleteNetworkInterfaceResponse()
        model._deserialize(response)
        return model

    def AttachNetworkInterface(self, request):
        response = self._api_call("AttachNetworkInterface", request)
        model = models.AttachNetworkInterfaceResponse()
        model._deserialize(response)
        return model

    def DetachNetworkInterface(self, request):
        response = self._api_call("DetachNetworkInterface", request)
        model = models.DetachNetworkInterfaceResponse()
        model._deserialize(response)
        return model

    def AssignNetworkInterfaceIpv4(self, request):
        response = self._api_call("AssignNetworkInterfaceIpv4", request)
        model = models.AssignNetworkInterfaceIpv4Response()
        model._deserialize(response)
        return model

    def BatchAssignNetworkInterfaceIpv4(self, request):
        response = self._api_call("BatchAssignNetworkInterfaceIpv4", request)
        model = models.BatchAssignNetworkInterfaceIpv4Response()
        model._deserialize(response)
        return model

    def UnassignNetworkInterfaceIpv4(self, request):
        response = self._api_call("UnassignNetworkInterfaceIpv4", request)
        model = models.UnassignNetworkInterfaceIpv4Response()
        model._deserialize(response)
        return model

    def DescribeNetworkInterfacePublicIPv6(self, request):
        response = self._api_call("DescribeNetworkInterfacePublicIPv6", request)
        model = models.DescribeNetworkInterfacePublicIPv6Response()
        model._deserialize(response)
        return model

    def InquiryPricePublicIpv6(self, request):
        response = self._api_call("InquiryPricePublicIpv6", request)
        model = models.InquiryPricePublicIpv6Response()
        model._deserialize(response)
        return model

    def AssignNetworkInterfaceIpv6(self, request):
        response = self._api_call("AssignNetworkInterfaceIpv6", request)
        model = models.AssignNetworkInterfaceIpv6Response()
        model._deserialize(response)
        return model

    def DescribeImages(self, request):
        response = self._api_call("DescribeImages", request)
        model = models.DescribeImagesResponse()
        model._deserialize(response)
        return model

    def CreateImage(self, request):
        response = self._api_call("CreateImage", request)
        model = models.CreateImageResponse()
        model._deserialize(response)
        return model

    def ModifyImagesAttributes(self, request):
        response = self._api_call("ModifyImagesAttributes", request)
        model = models.ModifyImagesAttributesResponse()
        model._deserialize(response)
        return model

    def DeleteImages(self, request):
        response = self._api_call("DeleteImages", request)
        model = models.DeleteImagesResponse()
        model._deserialize(response)
        return model

    def CreatePolicy(self, request):
        response = self._api_call("CreatePolicy", request)
        model = models.CreatePolicyResponse()
        model._deserialize(response)
        return model

    def DeletePolicy(self, request):
        response = self._api_call("DeletePolicy", request)
        model = models.DeletePolicyResponse()
        model._deserialize(response)
        return model

    def ModifyPolicy(self, request):
        response = self._api_call("ModifyPolicy", request)
        model = models.ModifyPolicyResponse()
        model._deserialize(response)
        return model

    def DescribePolicys(self, request):
        response = self._api_call("DescribePolicys", request)
        model = models.DescribePolicysResponse()
        model._deserialize(response)
        return model

    def DescribePolicyDetail(self, request):
        response = self._api_call("DescribePolicyDetail", request)
        model = models.DescribePolicyDetailResponse()
        model._deserialize(response)
        return model

    def AttachToPolicy(self, request):
        response = self._api_call("AttachToPolicy", request)
        model = models.AttachToPolicyResponse()
        model._deserialize(response)
        return model

    def DetachFromPolicy(self, request):
        response = self._api_call("DetachFromPolicy", request)
        model = models.DetachFromPolicyResponse()
        model._deserialize(response)
        return model

    def DescribePolicyRegions(self, request):
        response = self._api_call("DescribePolicyRegions", request)
        model = models.DescribePolicyRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeReflectUdpPortOptions(self, request):
        response = self._api_call("DescribeReflectUdpPortOptions", request)
        model = models.DescribeReflectUdpPortOptionsResponse()
        model._deserialize(response)
        return model

    def DescribeSecurityGroups(self, request):
        response = self._api_call("DescribeSecurityGroups", request)
        model = models.DescribeSecurityGroupsResponse()
        model._deserialize(response)
        return model

    def ModifySecurityGroupsAttribute(self, request):
        response = self._api_call("ModifySecurityGroupsAttribute", request)
        model = models.ModifySecurityGroupsAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeSecurityGroupRule(self, request):
        response = self._api_call("DescribeSecurityGroupRule", request)
        model = models.DescribeSecurityGroupRuleResponse()
        model._deserialize(response)
        return model

    def CreateSecurityGroup(self, request):
        response = self._api_call("CreateSecurityGroup", request)
        model = models.CreateSecurityGroupResponse()
        model._deserialize(response)
        return model

    def DeleteSecurityGroup(self, request):
        response = self._api_call("DeleteSecurityGroup", request)
        model = models.DeleteSecurityGroupResponse()
        model._deserialize(response)
        return model

    def ConfigureSecurityGroupRules(self, request):
        response = self._api_call("ConfigureSecurityGroupRules", request)
        model = models.ConfigureSecurityGroupRulesResponse()
        model._deserialize(response)
        return model

    def AssignSecurityGroupVpc(self, request):
        response = self._api_call("AssignSecurityGroupVpc", request)
        model = models.AssignSecurityGroupVpcResponse()
        model._deserialize(response)
        return model

    def UnAssignSecurityGroupVpc(self, request):
        response = self._api_call("UnAssignSecurityGroupVpc", request)
        model = models.UnAssignSecurityGroupVpcResponse()
        model._deserialize(response)
        return model

    def DescribeEipRegions(self, request):
        response = self._api_call("DescribeEipRegions", request)
        model = models.DescribeEipRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeEipInternetChargeTypes(self, request):
        response = self._api_call("DescribeEipInternetChargeTypes", request)
        model = models.DescribeEipInternetChargeTypesResponse()
        model._deserialize(response)
        return model

    def DescribeEipRemoteRegions(self, request):
        response = self._api_call("DescribeEipRemoteRegions", request)
        model = models.DescribeEipRemoteRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeEips(self, request):
        response = self._api_call("DescribeEips", request)
        model = models.DescribeEipsResponse()
        model._deserialize(response)
        return model

    def CreateEips(self, request):
        response = self._api_call("CreateEips", request)
        model = models.CreateEipsResponse()
        model._deserialize(response)
        return model

    def DeleteEip(self, request):
        response = self._api_call("DeleteEip", request)
        model = models.DeleteEipResponse()
        model._deserialize(response)
        return model

    def RenewEip(self, request):
        response = self._api_call("RenewEip", request)
        model = models.RenewEipResponse()
        model._deserialize(response)
        return model

    def ConfigEipEgressIp(self, request):
        response = self._api_call("ConfigEipEgressIp", request)
        model = models.ConfigEipEgressIpResponse()
        model._deserialize(response)
        return model

    def DescribeEipPrice(self, request):
        response = self._api_call("DescribeEipPrice", request)
        model = models.DescribeEipPriceResponse()
        model._deserialize(response)
        return model

    def ChangeEipInternetChargeType(self, request):
        response = self._api_call("ChangeEipInternetChargeType", request)
        model = models.ChangeEipInternetChargeTypeResponse()
        model._deserialize(response)
        return model

    def AvailableLanIp(self, request):
        response = self._api_call("AvailableLanIp", request)
        model = models.AvailableLanIpResponse()
        model._deserialize(response)
        return model

    def DescribeEipTraffic(self, request):
        response = self._api_call("DescribeEipTraffic", request)
        model = models.DescribeEipTrafficResponse()
        model._deserialize(response)
        return model

    def AssociateEipAddress(self, request):
        response = self._api_call("AssociateEipAddress", request)
        model = models.AssociateEipAddressResponse()
        model._deserialize(response)
        return model

    def UnassociateEipAddress(self, request):
        response = self._api_call("UnassociateEipAddress", request)
        model = models.UnassociateEipAddressResponse()
        model._deserialize(response)
        return model

    def ReplaceEipAddress(self, request):
        response = self._api_call("ReplaceEipAddress", request)
        model = models.ReplaceEipAddressResponse()
        model._deserialize(response)
        return model

    def ModifyEipAttribute(self, request):
        response = self._api_call("ModifyEipAttribute", request)
        model = models.ModifyEipAttributeResponse()
        model._deserialize(response)
        return model

    def ModifyEipBandwidth(self, request):
        response = self._api_call("ModifyEipBandwidth", request)
        model = models.ModifyEipBandwidthResponse()
        model._deserialize(response)
        return model

    def ChangeEipBindType(self, request):
        response = self._api_call("ChangeEipBindType", request)
        model = models.ChangeEipBindTypeResponse()
        model._deserialize(response)
        return model

    def DescribeEipMonitorData(self, request):
        response = self._api_call("DescribeEipMonitorData", request)
        model = models.DescribeEipMonitorDataResponse()
        model._deserialize(response)
        return model

    def DescribeDDosAllEventList(self, request):
        response = self._api_call("DescribeDDosAllEventList", request)
        model = models.DescribeDDosAllEventListResponse()
        model._deserialize(response)
        return model

    def DescribeDDosEventDetail(self, request):
        response = self._api_call("DescribeDDosEventDetail", request)
        model = models.DescribeDDosEventDetailResponse()
        model._deserialize(response)
        return model

    def DescribeZones(self, request):
        response = self._api_call("DescribeZones", request)
        model = models.DescribeZonesResponse()
        model._deserialize(response)
        return model

    def DescribePools(self, request):
        response = self._api_call("DescribePools", request)
        model = models.DescribePoolsResponse()
        model._deserialize(response)
        return model

    def DescribeCidrRegions(self, request):
        response = self._api_call("DescribeCidrRegions", request)
        model = models.DescribeCidrRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeCidrPrice(self, request):
        response = self._api_call("DescribeCidrPrice", request)
        model = models.DescribeCidrPriceResponse()
        model._deserialize(response)
        return model

    def DescribeCidrs(self, request):
        response = self._api_call("DescribeCidrs", request)
        model = models.DescribeCidrsResponse()
        model._deserialize(response)
        return model

    def CreateCidr(self, request):
        response = self._api_call("CreateCidr", request)
        model = models.CreateCidrResponse()
        model._deserialize(response)
        return model

    def ModifyCidrAttribute(self, request):
        response = self._api_call("ModifyCidrAttribute", request)
        model = models.ModifyCidrAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteCidr(self, request):
        response = self._api_call("DeleteCidr", request)
        model = models.DeleteCidrResponse()
        model._deserialize(response)
        return model

    def RenewCidr(self, request):
        response = self._api_call("RenewCidr", request)
        model = models.RenewCidrResponse()
        model._deserialize(response)
        return model

    def DeleteCidrs(self, request):
        response = self._api_call("DeleteCidrs", request)
        model = models.DeleteCidrsResponse()
        model._deserialize(response)
        return model

    def CreateCrossRegionBandwidth(self, request):
        response = self._api_call("CreateCrossRegionBandwidth", request)
        model = models.CreateCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateCrossRegionBandwidth(self, request):
        response = self._api_call("InquiryPriceCreateCrossRegionBandwidth", request)
        model = models.InquiryPriceCreateCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyCrossRegionBandwidthAttribute(self, request):
        response = self._api_call("ModifyCrossRegionBandwidthAttribute", request)
        model = models.ModifyCrossRegionBandwidthAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteCrossRegionBandwidth(self, request):
        response = self._api_call("DeleteCrossRegionBandwidth", request)
        model = models.DeleteCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def DescribeCrossRegionBandwidthMonitorData(self, request):
        response = self._api_call("DescribeCrossRegionBandwidthMonitorData", request)
        model = models.DescribeCrossRegionBandwidthMonitorDataResponse()
        model._deserialize(response)
        return model

    def InquiryPriceModifyCrossRegionBandwidth(self, request):
        response = self._api_call("InquiryPriceModifyCrossRegionBandwidth", request)
        model = models.InquiryPriceModifyCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def DescribeCrossRegionBandwidthRegions(self, request):
        response = self._api_call("DescribeCrossRegionBandwidthRegions", request)
        model = models.DescribeCrossRegionBandwidthRegionsResponse()
        model._deserialize(response)
        return model

    def ModifyCrossRegionBandwidth(self, request):
        response = self._api_call("ModifyCrossRegionBandwidth", request)
        model = models.ModifyCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def RenewCrossRegionBandwidth(self, request):
        response = self._api_call("RenewCrossRegionBandwidth", request)
        model = models.RenewCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def DescribeCrossRegionBandwidth(self, request):
        response = self._api_call("DescribeCrossRegionBandwidth", request)
        model = models.DescribeCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def CreateBorderGateway(self, request):
        response = self._api_call("CreateBorderGateway", request)
        model = models.CreateBorderGatewayResponse()
        model._deserialize(response)
        return model

    def DescribeBorderGateways(self, request):
        response = self._api_call("DescribeBorderGateways", request)
        model = models.DescribeBorderGatewaysResponse()
        model._deserialize(response)
        return model

    def DeleteBorderGateway(self, request):
        response = self._api_call("DeleteBorderGateway", request)
        model = models.DeleteBorderGatewayResponse()
        model._deserialize(response)
        return model

    def ModifyBorderGatewayAsn(self, request):
        response = self._api_call("ModifyBorderGatewayAsn", request)
        model = models.ModifyBorderGatewayAsnResponse()
        model._deserialize(response)
        return model

    def ModifyBorderGatewaysAttribute(self, request):
        response = self._api_call("ModifyBorderGatewaysAttribute", request)
        model = models.ModifyBorderGatewaysAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeAvailableNats(self, request):
        response = self._api_call("DescribeAvailableNats", request)
        model = models.DescribeAvailableNatsResponse()
        model._deserialize(response)
        return model

    def AssignBorderGateway(self, request):
        response = self._api_call("AssignBorderGateway", request)
        model = models.AssignBorderGatewayResponse()
        model._deserialize(response)
        return model

    def UnassignBorderGateway(self, request):
        response = self._api_call("UnassignBorderGateway", request)
        model = models.UnassignBorderGatewayResponse()
        model._deserialize(response)
        return model

    def AssignBorderGatewayRoute(self, request):
        response = self._api_call("AssignBorderGatewayRoute", request)
        model = models.AssignBorderGatewayRouteResponse()
        model._deserialize(response)
        return model

    def UnassignBorderGatewayRoute(self, request):
        response = self._api_call("UnassignBorderGatewayRoute", request)
        model = models.UnassignBorderGatewayRouteResponse()
        model._deserialize(response)
        return model

    def DescribeZoneInstanceConfigInfos(self, request):
        response = self._api_call("DescribeZoneInstanceConfigInfos", request)
        model = models.DescribeZoneInstanceConfigInfosResponse()
        model._deserialize(response)
        return model

    def DescribeTimeZones(self, request):
        response = self._api_call("DescribeTimeZones", request)
        model = models.DescribeTimeZonesResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateInstance(self, request):
        response = self._api_call("InquiryPriceCreateInstance", request)
        model = models.InquiryPriceCreateInstanceResponse()
        model._deserialize(response)
        return model

    def CreateZecInstances(self, request):
        response = self._api_call("CreateZecInstances", request)
        model = models.CreateZecInstancesResponse()
        model._deserialize(response)
        return model

    def DescribeInstances(self, request):
        response = self._api_call("DescribeInstances", request)
        model = models.DescribeInstancesResponse()
        model._deserialize(response)
        return model

    def DescribeInstancesStatus(self, request):
        response = self._api_call("DescribeInstancesStatus", request)
        model = models.DescribeInstancesStatusResponse()
        model._deserialize(response)
        return model

    def ModifyInstancesAttribute(self, request):
        response = self._api_call("ModifyInstancesAttribute", request)
        model = models.ModifyInstancesAttributeResponse()
        model._deserialize(response)
        return model

    def StartInstances(self, request):
        response = self._api_call("StartInstances", request)
        model = models.StartInstancesResponse()
        model._deserialize(response)
        return model

    def StopInstances(self, request):
        response = self._api_call("StopInstances", request)
        model = models.StopInstancesResponse()
        model._deserialize(response)
        return model

    def RebootInstances(self, request):
        response = self._api_call("RebootInstances", request)
        model = models.RebootInstancesResponse()
        model._deserialize(response)
        return model

    def ResetInstancePassword(self, request):
        response = self._api_call("ResetInstancePassword", request)
        model = models.ResetInstancePasswordResponse()
        model._deserialize(response)
        return model

    def ResetInstance(self, request):
        response = self._api_call("ResetInstance", request)
        model = models.ResetInstanceResponse()
        model._deserialize(response)
        return model

    def ResetInstances(self, request):
        response = self._api_call("ResetInstances", request)
        model = models.ResetInstancesResponse()
        model._deserialize(response)
        return model

    def StartIpForward(self, request):
        response = self._api_call("StartIpForward", request)
        model = models.StartIpForwardResponse()
        model._deserialize(response)
        return model

    def StopIpForward(self, request):
        response = self._api_call("StopIpForward", request)
        model = models.StopIpForwardResponse()
        model._deserialize(response)
        return model

    def StartAgentMonitor(self, request):
        response = self._api_call("StartAgentMonitor", request)
        model = models.StartAgentMonitorResponse()
        model._deserialize(response)
        return model

    def StopAgentMonitor(self, request):
        response = self._api_call("StopAgentMonitor", request)
        model = models.StopAgentMonitorResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceType(self, request):
        response = self._api_call("ModifyInstanceType", request)
        model = models.ModifyInstanceTypeResponse()
        model._deserialize(response)
        return model

    def ChangeNicNetworkType(self, request):
        response = self._api_call("ChangeNicNetworkType", request)
        model = models.ChangeNicNetworkTypeResponse()
        model._deserialize(response)
        return model

    def ReleaseInstances(self, request):
        response = self._api_call("ReleaseInstances", request)
        model = models.ReleaseInstancesResponse()
        model._deserialize(response)
        return model

    def DescribeVncUrl(self, request):
        response = self._api_call("DescribeVncUrl", request)
        model = models.DescribeVncUrlResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceMonitorData(self, request):
        response = self._api_call("DescribeInstanceMonitorData", request)
        model = models.DescribeInstanceMonitorDataResponse()
        model._deserialize(response)
        return model

    def CreateNatGateway(self, request):
        response = self._api_call("CreateNatGateway", request)
        model = models.CreateNatGatewayResponse()
        model._deserialize(response)
        return model

    def ModifyNatGatewayAttribute(self, request):
        response = self._api_call("ModifyNatGatewayAttribute", request)
        model = models.ModifyNatGatewayAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeNatGatewayRegions(self, request):
        response = self._api_call("DescribeNatGatewayRegions", request)
        model = models.DescribeNatGatewayRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeNatGateways(self, request):
        response = self._api_call("DescribeNatGateways", request)
        model = models.DescribeNatGatewaysResponse()
        model._deserialize(response)
        return model

    def DescribeNatGatewayDetail(self, request):
        response = self._api_call("DescribeNatGatewayDetail", request)
        model = models.DescribeNatGatewayDetailResponse()
        model._deserialize(response)
        return model

    def DeleteNatGateway(self, request):
        response = self._api_call("DeleteNatGateway", request)
        model = models.DeleteNatGatewayResponse()
        model._deserialize(response)
        return model

    def RenewNatGateway(self, request):
        response = self._api_call("RenewNatGateway", request)
        model = models.RenewNatGatewayResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateNatGateway(self, request):
        response = self._api_call("InquiryPriceCreateNatGateway", request)
        model = models.InquiryPriceCreateNatGatewayResponse()
        model._deserialize(response)
        return model

    def CreateSnatEntry(self, request):
        response = self._api_call("CreateSnatEntry", request)
        model = models.CreateSnatEntryResponse()
        model._deserialize(response)
        return model

    def ModifySnatEntry(self, request):
        response = self._api_call("ModifySnatEntry", request)
        model = models.ModifySnatEntryResponse()
        model._deserialize(response)
        return model

    def DeleteSnatEntry(self, request):
        response = self._api_call("DeleteSnatEntry", request)
        model = models.DeleteSnatEntryResponse()
        model._deserialize(response)
        return model

    def CreateDnatEntry(self, request):
        response = self._api_call("CreateDnatEntry", request)
        model = models.CreateDnatEntryResponse()
        model._deserialize(response)
        return model

    def ModifyDnatEntry(self, request):
        response = self._api_call("ModifyDnatEntry", request)
        model = models.ModifyDnatEntryResponse()
        model._deserialize(response)
        return model

    def DeleteDnatEntry(self, request):
        response = self._api_call("DeleteDnatEntry", request)
        model = models.DeleteDnatEntryResponse()
        model._deserialize(response)
        return model

    def DescribeAvailableBorderGateway(self, request):
        response = self._api_call("DescribeAvailableBorderGateway", request)
        model = models.DescribeAvailableBorderGatewayResponse()
        model._deserialize(response)
        return model

    def CreateRoute(self, request):
        response = self._api_call("CreateRoute", request)
        model = models.CreateRouteResponse()
        model._deserialize(response)
        return model

    def ModifyRouteAttribute(self, request):
        response = self._api_call("ModifyRouteAttribute", request)
        model = models.ModifyRouteAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteRoute(self, request):
        response = self._api_call("DeleteRoute", request)
        model = models.DeleteRouteResponse()
        model._deserialize(response)
        return model

    def DescribeRoutes(self, request):
        response = self._api_call("DescribeRoutes", request)
        model = models.DescribeRoutesResponse()
        model._deserialize(response)
        return model

