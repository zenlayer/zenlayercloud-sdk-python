#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.bmc.v20221120 import models
from zenlayercloud.common.abstract_client import AbstractClient


class BmcClient(AbstractClient):
    _api_version = "2022-11-20"
    _service = "bmc"

    def DescribeZones(self, request):
        response = self._api_call("DescribeZones", request)

        model = models.DescribeZonesResponse()
        model._deserialize(response)
        return model


    #
    def DescribeImages(self, request):
        response = self._api_call("DescribeImages", request)

        model = models.DescribeImagesResponse()
        model._deserialize(response)
        return model

    #
    def DescribeInstances(self, request):
        response = self._api_call("DescribeInstances", request)

        model = models.DescribeInstancesResponse()
        model._deserialize(response)
        return model


    def CreateInstances(self, request):
        """ 本接口 (CreateInstances) 用于创建一个或多个指定配置的BMC实例。

        :param request: Request instance for CreateInstances.
        :return:
        """

        response = self._api_call("CreateInstances", request)
        model = models.CreateInstancesResponse()
        model._deserialize(response)
        return model


    #
    def StartInstances(self, request):
        response = self._api_call("StartInstances", request)

        model = models.StartInstancesResponse()
        model._deserialize(response)
        return model

    #
    def StopInstances(self, request):
        response = self._api_call("StopInstances", request)

        model = models.StopInstancesResponse()
        model._deserialize(response)
        return model

    #
    def RebootInstances(self, request):
        response = self._api_call("RebootInstances", request)

        model = models.RebootInstancesResponse()
        model._deserialize(response)
        return model


    #
    def ReinstallInstance(self, request):
        response = self._api_call("ReinstallInstance", request)

        model = models.ReinstallInstanceResponse()
        model._deserialize(response)
        return model


    #
    def TerminateInstance(self, request):
        response = self._api_call("TerminateInstance", request)

        model = models.TerminateInstanceResponse()
        model._deserialize(response)
        return model


    #
    def ReleaseInstances(self, request):
        response = self._api_call("ReleaseInstances", request)

        model = models.ReleaseInstancesResponse()
        model._deserialize(response)
        return model


    #
    def RenewInstance(self, request):
        response = self._api_call("RenewInstance", request)

        model = models.RenewInstanceResponse()
        model._deserialize(response)
        return model


    #
    def ModifyInstancesAttribute(self, request):
        response = self._api_call("ModifyInstancesAttribute", request)

        model = models.ModifyInstancesAttributeResponse()
        model._deserialize(response)
        return model


    #
    def InquiryPriceCreateInstance(self, request):
        response = self._api_call("InquiryPriceCreateInstance", request)

        model = models.InquiryPriceCreateInstanceResponse()
        model._deserialize(response)
        return model


    #
    def DescribeInstanceTypes(self, request):
        response = self._api_call("DescribeInstanceTypes", request)

        model = models.DescribeInstanceTypesResponse()
        model._deserialize(response)
        return model

    #
    def DescribeAvailableResources(self, request):
        response = self._api_call("DescribeAvailableResources", request)

        model = models.DescribeAvailableResourcesResponse()
        model._deserialize(response)
        return model


    #
    def ModifyInstanceBandwidth(self, request):
        response = self._api_call("ModifyInstanceBandwidth", request)

        model = models.ModifyInstanceBandwidthResponse()
        model._deserialize(response)
        return model


    #
    def CancelInstanceBandwidthDowngrade(self, request):
        response = self._api_call("CancelInstanceBandwidthDowngrade", request)

        model = models.CancelInstanceBandwidthDowngradeResponse()
        model._deserialize(response)
        return model


    #
    def InquiryPriceInstanceBandwidth(self, request):
        response = self._api_call("InquiryPriceInstanceBandwidth", request)

        model = models.InquiryPriceInstanceBandwidthResponse()
        model._deserialize(response)
        return model


    #
    def ModifyInstanceTrafficPackage(self, request):
        response = self._api_call("ModifyInstanceTrafficPackage", request)

        model = models.ModifyInstanceTrafficPackageResponse()
        model._deserialize(response)
        return model


    #
    def CancelInstanceTrafficPackageDowngrade(self, request):
        response = self._api_call("CancelInstanceTrafficPackageDowngrade", request)

        model = models.CancelInstanceTrafficPackageDowngradeResponse()
        model._deserialize(response)
        return model


    #
    def InquiryPriceInstanceTrafficPackage(self, request):
        response = self._api_call("InquiryPriceInstanceTrafficPackage", request)

        model = models.InquiryPriceInstanceTrafficPackageResponse()
        model._deserialize(response)
        return model


    #
    def DescribeInstanceInternetStatus(self, request):
        response = self._api_call("DescribeInstanceInternetStatus", request)

        model = models.DescribeInstanceInternetStatusResponse()
        model._deserialize(response)
        return model


    #
    def ModifyInstancesResourceGroup(self, request):
        response = self._api_call("ModifyInstancesResourceGroup", request)

        model = models.ModifyInstancesResourceGroupResponse()
        model._deserialize(response)
        return model


    #
    def DescribeInstanceTraffic(self, request):
        response = self._api_call("DescribeInstanceTraffic", request)

        model = models.DescribeInstanceTrafficResponse()
        model._deserialize(response)
        return model

    def DescribeInstancesMonitorHealth(self, request):
        response = self._api_call("DescribeInstancesMonitorHealth", request)

        model = models.DescribeInstancesMonitorHealthResponse()
        model._deserialize(response)
        return model

    # eip

    def DescribeEipAddresses(self, request):
        response = self._api_call("DescribeEipAddresses", request)

        model = models.DescribeEipAddressesResponse()
        model._deserialize(response)
        return model


    def DescribeEipAvailableResources(self, request):
        response = self._api_call("DescribeEipAvailableResources", request)

        model = models.DescribeEipAvailableResourcesResponse()
        model._deserialize(response)
        return model

    def AllocateEipAddresses(self, request):
        response = self._api_call("AllocateEipAddresses", request)

        model = models.AllocateEipAddressesResponse()
        model._deserialize(response)
        return model

    def TerminateEipAddress(self, request):
        response = self._api_call("TerminateEipAddress", request)

        model = models.TerminateEipAddressResponse()
        model._deserialize(response)
        return model

    def ReleaseEipAddresses(self, request):
        response = self._api_call("ReleaseEipAddresses", request)

        model = models.ReleaseEipAddressesResponse()
        model._deserialize(response)
        return model

    def RenewEipAddress(self, request):
        response = self._api_call("RenewEipAddress", request)

        model = models.RenewEipAddressResponse()
        model._deserialize(response)
        return model


    def AssociateEipAddress(self, request):
        response = self._api_call("AssociateEipAddress", request)

        model = models.AssociateEipAddressResponse()
        model._deserialize(response)
        return model

    def UnAssociateEipAddress(self, request):
        response = self._api_call("UnAssociateEipAddress", request)

        model = models.UnAssociateEipAddressResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateEipAddress(self, request):
        response = self._api_call("InquiryPriceCreateEipAddress", request)

        model = models.InquiryPriceCreateEipAddressResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceAvailableEipResources(self, request):
        response = self._api_call("DescribeInstanceAvailableEipResources", request)

        model = models.DescribeInstanceAvailableEipResourcesResponse()
        model._deserialize(response)
        return model

    def ModifyEipAddressesResourceGroup(self, request):
        response = self._api_call("ModifyEipAddressesResourceGroup", request)

        model = models.ModifyEipAddressesResourceGroupResponse()
        model._deserialize(response)
        return model

    # cidr

    def DescribeCidrBlocks(self, request):
        response = self._api_call("DescribeCidrBlocks", request)

        model = models.DescribeCidrBlocksResponse()
        model._deserialize(response)
        return model

    def DescribeCidrBlockIps(self, request):
        response = self._api_call("DescribeCidrBlockIps", request)

        model = models.DescribeCidrBlockIpsResponse()
        model._deserialize(response)
        return model

    def DescribeAvailableIpv4Resources(self, request):
        response = self._api_call("DescribeAvailableIpv4Resources", request)

        model = models.DescribeAvailableIpv4ResourcesResponse()
        model._deserialize(response)
        return model


    def DescribeAvailableIpv6Resources(self, request):
        response = self._api_call("DescribeAvailableIpv6Resources", request)

        model = models.DescribeAvailableIpv6ResourcesResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceAvailableCidrBlock(self, request):
        response = self._api_call("DescribeInstanceAvailableCidrBlock", request)

        model = models.DescribeInstanceAvailableCidrBlockResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateIpv4Block(self, request):
        response = self._api_call("InquiryPriceCreateIpv4Block", request)

        model = models.InquiryPriceCreateIpv4BlockResponse()
        model._deserialize(response)
        return model

    def CreateIpv4Block(self, request):
        response = self._api_call("CreateIpv4Block", request)

        model = models.CreateIpv4BlockResponse()
        model._deserialize(response)
        return model

    def CreateIpv6Block(self, request):
        response = self._api_call("CreateIpv6Block", request)

        model = models.CreateIpv6BlockResponse()
        model._deserialize(response)
        return model

    def ModifyCidrBlocksAttribute(self, request):
        response = self._api_call("ModifyCidrBlocksAttribute", request)

        model = models.ModifyCidrBlocksAttributeResponse()
        model._deserialize(response)
        return model

    def RenewCidrBlock(self, request):
        response = self._api_call("RenewCidrBlock", request)

        model = models.RenewCidrBlockResponse()
        model._deserialize(response)
        return model

    def TerminateCidrBlock(self, request):
        response = self._api_call("TerminateCidrBlock", request)

        model = models.TerminateCidrBlockResponse()
        model._deserialize(response)
        return model

    def ReleaseCidrBlocks(self, request):
        response = self._api_call("ReleaseCidrBlocks", request)

        model = models.ReleaseCidrBlocksResponse()
        model._deserialize(response)
        return model

    def BindCidrBlockIps(self, request):
        response = self._api_call("BindCidrBlockIps", request)

        model = models.BindCidrBlockIpsResponse()
        model._deserialize(response)
        return model

    def UnbindCidrBlockIps(self, request):
        response = self._api_call("UnbindCidrBlockIps", request)

        model = models.UnbindCidrBlockIpsResponse()
        model._deserialize(response)
        return model

    # vpc、subnet

    def DescribeVpcAvailableRegions(self, request):
        response = self._api_call("DescribeVpcAvailableRegions", request)

        model = models.DescribeVpcAvailableRegionsResponse()
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

    def AssociateSubnetInstances(self, request):
        response = self._api_call("AssociateSubnetInstances", request)

        model = models.AssociateSubnetInstancesResponse()
        model._deserialize(response)
        return model

    def UnAssociateSubnetInstance(self, request):
        response = self._api_call("UnAssociateSubnetInstance", request)

        model = models.UnAssociateSubnetInstanceResponse()
        model._deserialize(response)
        return model

    def AssociateVpcSubnet(self, request):
        response = self._api_call("AssociateVpcSubnet", request)

        model = models.AssociateVpcSubnetResponse()
        model._deserialize(response)
        return model

    def DescribeSubnetAvailableResources(self, request):
        response = self._api_call("DescribeSubnetAvailableResources", request)

        model = models.DescribeSubnetAvailableResourcesResponse()
        model._deserialize(response)
        return model


