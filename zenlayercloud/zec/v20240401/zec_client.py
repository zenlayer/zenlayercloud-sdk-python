#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_client import AbstractClient
from zenlayercloud.zec.v20240401 import models


class ZecClient(AbstractClient):
    _api_version = "2024-04-01"
    _service = "zec"

    def DescribeInstanceMonitorData(self, request):
        response = self._api_call("DescribeInstanceMonitorData", request)

        model = models.DescribeInstanceMonitorDataResponse()
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

    def DescribeVpcs(self, request):
        response = self._api_call("DescribeVpcs", request)

        model = models.DescribeVpcsResponse()
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

    def ModifySubnetsAttribute(self, request):
        response = self._api_call("ModifySubnetsAttribute", request)

        model = models.ModifySubnetsAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeSubnets(self, request):
        response = self._api_call("DescribeSubnets", request)

        model = models.DescribeSubnetsResponse()
        model._deserialize(response)
        return model

    def ModifySubnetStackType(self, request):
        response = self._api_call("ModifySubnetStackType", request)

        model = models.ModifySubnetStackTypeResponse()
        model._deserialize(response)
        return model

    def CreateRoute(self, request):
        response = self._api_call("CreateRoute", request)

        model = models.CreateRouteResponse()
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

    def ModifyInstancesResourceGroup(self, request):
        response = self._api_call("ModifyInstancesResourceGroup", request)

        model = models.ModifyInstancesResourceGroupResponse()
        model._deserialize(response)
        return model


    def ModifyInstancesAttribute(self, request):
        response = self._api_call("ModifyInstancesAttribute", request)

        model = models.ModifyInstancesAttributeResponse()
        model._deserialize(response)
        return model


    def RebootInstances(self, request):
        response = self._api_call("RebootInstances", request)

        model = models.RebootInstancesResponse()
        model._deserialize(response)
        return model


    def ResetInstance(self, request):
        response = self._api_call("ResetInstance", request)

        model = models.ResetInstanceResponse()
        model._deserialize(response)
        return model


    def ResetInstancesPassword(self, request):
        response = self._api_call("ResetInstancesPassword", request)

        model = models.ResetInstancesPasswordResponse()
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


    def DescribeCidrs(self, request):
        response = self._api_call("DescribeCidrs", request)

        model = models.DescribeCidrsResponse()
        model._deserialize(response)
        return model


    def DescribeCidrRegions(self, request):
        response = self._api_call("DescribeCidrRegions", request)

        model = models.DescribeCidrRegionsResponse()
        model._deserialize(response)
        return model


    def DescribeOwnCidrPrice(self, request):
        response = self._api_call("DescribeOwnCidrPrice", request)

        model = models.DescribeOwnCidrPriceResponse()
        model._deserialize(response)
        return model


    def DescribeCidrPrice(self, request):
        response = self._api_call("DescribeCidrPrice", request)

        model = models.DescribeCidrPriceResponse()
        model._deserialize(response)
        return model


    def DescribeCidrUsedIps(self, request):
        response = self._api_call("DescribeCidrUsedIps", request)

        model = models.DescribeCidrUsedIpsResponse()
        model._deserialize(response)
        return model

    def CreateOwnCidr(self, request):
        response = self._api_call("CreateOwnCidr", request)

        model = models.CreateOwnCidrResponse()
        model._deserialize(response)
        return model

    def CreateCidr(self, request):
        response = self._api_call("CreateCidr", request)

        model = models.CreateCidrResponse()
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


    def UnAssignCidrIp(self, request):
        response = self._api_call("UnAssignCidrIp", request)

        model = models.UnAssignCidrIpResponse()
        model._deserialize(response)
        return model


    def AssignCidrIp(self, request):
        response = self._api_call("AssignCidrIp", request)

        model = models.AssignCidrIpResponse()
        model._deserialize(response)
        return model

    def BatchAssignCidrIp(self, request):
        response = self._api_call("BatchAssignCidrIp", request)

        model = models.BatchAssignCidrIpResponse()
        model._deserialize(response)
        return model


    def AvailableCidrIp(self, request):
        response = self._api_call("AvailableCidrIp", request)

        model = models.AvailableCidrIpResponse()
        model._deserialize(response)
        return model


    def ConfigEgressIp(self, request):
        response = self._api_call("ConfigEgressIp", request)

        model = models.ConfigEgressIpResponse()
        model._deserialize(response)
        return model


    def DescribeOwnCidrs(self, request):
        response = self._api_call("DescribeOwnCidrs", request)

        model = models.DescribeOwnCidrsResponse()
        model._deserialize(response)
        return model


    def AvailableLanIp(self, request):
        response = self._api_call("AvailableLanIp", request)

        model = models.AvailableLanIpResponse()
        model._deserialize(response)
        return model



    def DescribeDiskRegions(self, request):
        response = self._api_call("DescribeDiskRegions", request)

        model = models.DescribeDiskRegionsResponse()
        model._deserialize(response)
        return model



    def CreateDisks(self, request):
        response = self._api_call("CreateDisks", request)

        model = models.CreateDisksResponse()
        model._deserialize(response)
        return model


    def DescribeDisks(self, request):
        response = self._api_call("DescribeDisks", request)

        model = models.DescribeDisksResponse()
        model._deserialize(response)
        return model


    def AttachDisks(self, request):
        response = self._api_call("AttachDisks", request)

        model = models.AttachDisksResponse()
        model._deserialize(response)
        return model


    def ChangeDisksAttach(self, request):
        response = self._api_call("ChangeDisksAttach", request)

        model = models.ChangeDisksAttachResponse()
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


    def InquiryPriceCreateDisks(self, request):
        response = self._api_call("InquiryPriceCreateDisks", request)

        model = models.InquiryPriceCreateDisksResponse()
        model._deserialize(response)
        return model


    def TerminateDisk(self, request):
        response = self._api_call("TerminateDisk", request)

        model = models.TerminateDiskResponse()
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


    def DescribeNetworkInterfaces(self, request):
        response = self._api_call("DescribeNetworkInterfaces", request)

        model = models.DescribeNicsResponse()
        model._deserialize(response)
        return model


    def ModifyNetworkInterfacesAttribute(self, request):
        response = self._api_call("ModifyNetworkInterfacesAttribute", request)

        model = models.ModifyNicsAttributeResponse()
        model._deserialize(response)
        return model


    def CreateNetworkInterface(self, request):
        response = self._api_call("CreateNetworkInterface", request)

        model = models.CreateNicResponse()
        model._deserialize(response)
        return model

    def DeleteNetworkInterface(self, request):
        response = self._api_call("DeleteNetworkInterface", request)

        model = models.DeleteNicResponse()
        model._deserialize(response)
        return model


    def AttachNetworkInterface(self, request):
        response = self._api_call("AttachNetworkInterface", request)

        model = models.AttachNicResponse()
        model._deserialize(response)
        return model


    def AssignNetworkInterfaceIpv6(self, request):
        response = self._api_call("AssignNetworkInterfaceIpv6", request)

        model = models.AssignNicIpv6Response()
        model._deserialize(response)
        return model


    def UnassignNetworkInterfaceIpv4(self, request):
        response = self._api_call("UnAssignNetworkInterfaceIpv4", request)

        model = models.UnAssignNicIpv4Response()
        model._deserialize(response)
        return model


    def AssignNetworkInterfaceIpv4(self, request):
        response = self._api_call("AssignNetworkInterfaceIpv4", request)

        model = models.AssignNicIpv4Response()
        model._deserialize(response)
        return model

    def BatchAssignNetworkInterfaceIpv4(self, request):
        response = self._api_call("BatchAssignNetworkInterfaceIpv4", request)

        model = models.BatchAssignNicIpv4Response()
        model._deserialize(response)
        return model

    def DetachNetworkInterface(self, request):
        response = self._api_call("DetachNetworkInterface", request)

        model = models.DetachNicResponse()
        model._deserialize(response)
        return model


    def DescribeNetworkInterfaceRegions(self, request):
        response = self._api_call("DescribeNetworkInterfaceRegions", request)

        model = models.DescribeNicRegionsResponse()
        model._deserialize(response)
        return model


    def InquiryPricePublicIpv6(self, request):
        response = self._api_call("InquiryPricePublicIpv6", request)

        model = models.InquiryPricePublicIpv6Response()
        model._deserialize(response)
        return model


    def CreateZecInstances(self, request):
        response = self._api_call("CreateZecInstances", request)

        model = models.CreateZecInstancesResponse()
        model._deserialize(response)
        return model


    def CreateInstances(self, request):
        response = self._api_call("CreateInstances", request)

        model = models.CreateInstancesResponse()
        model._deserialize(response)
        return model


    def DescribeZoneInstanceConfigInfos(self, request):
        response = self._api_call("DescribeZoneInstanceConfigInfos", request)

        model = models.DescribeZoneInstanceConfigInfosResponse()
        model._deserialize(response)
        return model


    def DescribeZones(self, request):
        response = self._api_call("DescribeZones", request)

        model = models.DescribeZonesResponse()
        model._deserialize(response)
        return model


    def DescribeImages(self, request):
        response = self._api_call("DescribeImages", request)

        model = models.DescribeImagesResponse()
        model._deserialize(response)
        return model


    def DescribeKeyPairs(self, request):
        response = self._api_call("DescribeKeyPairs", request)

        model = models.DescribeKeyPairsResponse()
        model._deserialize(response)
        return model