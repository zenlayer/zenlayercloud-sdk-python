#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.vm.v20230313 import models
from zenlayercloud.common.abstract_client import AbstractClient


class VmClient(AbstractClient):
    _api_version = "2023-03-13"
    _service = "vm"

    def DescribeZones(self, request):
        response = self._api_call("DescribeZones", request)

        model = models.DescribeZonesResponse()
        model._deserialize(response)
        return model

    def DescribeZoneInstanceConfigInfos(self, request):
        response = self._api_call("DescribeZoneInstanceConfigInfos", request)

        model = models.DescribeZoneInstanceConfigInfosResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateInstance(self, request):
        response = self._api_call("InquiryPriceCreateInstance", request)

        model = models.InquiryPriceCreateInstanceResponse()
        model._deserialize(response)
        return model

    def CreateInstances(self, request):
        response = self._api_call("CreateInstances", request)

        model = models.CreateInstancesResponse()
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

    def ResetInstancesPassword(self, request):
        response = self._api_call("ResetInstancesPassword", request)

        model = models.ResetInstancesPasswordResponse()
        model._deserialize(response)
        return model

    def ResetInstance(self, request):
        response = self._api_call("ResetInstance", request)

        model = models.ResetInstanceResponse()
        model._deserialize(response)
        return model

    def TerminateInstance(self, request):
        response = self._api_call("TerminateInstance", request)

        model = models.TerminateInstanceResponse()
        model._deserialize(response)
        return model

    def ReleaseInstances(self, request):
        response = self._api_call("ReleaseInstances", request)

        model = models.ReleaseInstancesResponse()
        model._deserialize(response)
        return model

    def ModifyInstancesAttribute(self, request):
        response = self._api_call("ModifyInstancesAttribute", request)

        model = models.ModifyInstancesAttributeResponse()
        model._deserialize(response)
        return model

    def InquiryPriceInstanceBandwidth(self, request):
        response = self._api_call("InquiryPriceInstanceBandwidth", request)

        model = models.InquiryPriceInstanceBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceBandwidth(self, request):
        response = self._api_call("ModifyInstanceBandwidth", request)

        model = models.ModifyInstanceBandwidthResponse()
        model._deserialize(response)
        return model

    def CancelInstanceBandwidthDowngrade(self, request):
        response = self._api_call("CancelInstanceBandwidthDowngrade", request)

        model = models.CancelInstanceBandwidthDowngradeResponse()
        model._deserialize(response)
        return model

    def InquiryPriceInstanceTrafficPackage(self, request):
        response = self._api_call("InquiryPriceInstanceTrafficPackage", request)

        model = models.InquiryPriceInstanceTrafficPackageResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceTrafficPackage(self, request):
        response = self._api_call("ModifyInstanceTrafficPackage", request)

        model = models.ModifyInstanceTrafficPackageResponse()
        model._deserialize(response)
        return model

    def CancelInstanceTrafficPackageDowngrade(self, request):
        response = self._api_call("CancelInstanceTrafficPackageDowngrade", request)

        model = models.CancelInstanceTrafficPackageDowngradeResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceInternetStatus(self, request):
        response = self._api_call("DescribeInstanceInternetStatus", request)

        model = models.DescribeInstanceInternetStatusResponse()
        model._deserialize(response)
        return model


    def ModifyInstancesResourceGroup(self, request):
        response = self._api_call("ModifyInstancesResourceGroup", request)

        model = models.ModifyInstancesResourceGroupResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceTraffic(self, request):
        response = self._api_call("DescribeInstanceTraffic", request)

        model = models.DescribeInstanceTrafficResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceCpuMonitor(self, request):
        response = self._api_call("DescribeInstanceCpuMonitor", request)

        model = models.DescribeInstanceCpuMonitorResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceType(self, request):
        response = self._api_call("ModifyInstanceType", request)

        model = models.ModifyInstanceTypeResponse()
        model._deserialize(response)
        return model

    def CancelInstanceDowngrade(self, request):
        response = self._api_call("CancelInstanceDowngrade", request)

        model = models.CancelInstanceDowngradeResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceTypeStatus(self, request):
        response = self._api_call("DescribeInstanceTypeStatus", request)

        model = models.DescribeInstanceTypeStatusResponse()
        model._deserialize(response)
        return model

    def CreateDisks(self, request):
        response = self._api_call("CreateDisks", request)

        model = models.CreateDisksResponse()
        model._deserialize(response)
        return model

    def ResizeDisk(self, request):
        response = self._api_call("ResizeDisk", request)
        model = models.ResizeDiskResponse()
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

    def DescribeDiskCategory(self, request):
        response = self._api_call("DescribeDiskCategory", request)

        model = models.DescribeDiskCategoryResponse()
        model._deserialize(response)
        return model

    def ModifyDisksResourceGroup(self, request):
        response = self._api_call("ModifyDisksResourceGroup", request)

        model = models.ModifyDisksResourceGroupResponse()
        model._deserialize(response)
        return model

    def DescribeImages(self, request):
        response = self._api_call("DescribeImages", request)

        model = models.DescribeImagesResponse()
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

    def CreateImage(self, request):
        response = self._api_call("CreateImage", request)

        model = models.CreateImageResponse()
        model._deserialize(response)
        return model

    def DescribeImageQuota(self, request):
        response = self._api_call("DescribeImageQuota", request)

        model = models.DescribeImageQuotaResponse()
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

    def DescribeInstanceAvailableSecurityGroupResources(self, request):
        response = self._api_call("DescribeInstanceAvailableSecurityGroupResources", request)

        model = models.DescribeInstanceAvailableSecurityGroupResourcesResponse()
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

    def AuthorizeSecurityGroupRules(self, request):
        response = self._api_call("AuthorizeSecurityGroupRules", request)

        model = models.AuthorizeSecurityGroupRulesResponse()
        model._deserialize(response)
        return model

    def ConfigureSecurityGroupRules(self, request):
        response = self._api_call("ConfigureSecurityGroupRules", request)

        model = models.ConfigureSecurityGroupRulesResponse()
        model._deserialize(response)
        return model

    def AuthorizeSecurityGroupRule(self, request):
        response = self._api_call("AuthorizeSecurityGroupRule", request)

        model = models.AuthorizeSecurityGroupRuleResponse()
        model._deserialize(response)
        return model

    def RevokeSecurityGroupRules(self, request):
        response = self._api_call("RevokeSecurityGroupRules", request)

        model = models.RevokeSecurityGroupRulesResponse()
        model._deserialize(response)
        return model

    def AssociateSecurityGroupInstance(self, request):
        response = self._api_call("AssociateSecurityGroupInstance", request)

        model = models.AssociateSecurityGroupInstanceResponse()
        model._deserialize(response)
        return model

    def UnAssociateSecurityGroupInstance(self, request):
        response = self._api_call("UnAssociateSecurityGroupInstance", request)

        model = models.UnAssociateSecurityGroupInstanceResponse()
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

    def CreateVpcSubnet(self, request):
        response = self._api_call("CreateVpcSubnet", request)

        model = models.CreateVpcSubnetResponse()
        model._deserialize(response)
        return model

    def DeleteVpcSubnet(self, request):
        response = self._api_call("DeleteVpcSubnet", request)

        model = models.DeleteVpcSubnetResponse()
        model._deserialize(response)
        return model

    def ModifyVpcSubnetsAttribute(self, request):
        response = self._api_call("ModifyVpcSubnetsAttribute", request)

        model = models.ModifyVpcSubnetsAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeVpcSubnets(self, request):
        response = self._api_call("DescribeVpcSubnets", request)

        model = models.DescribeVpcSubnetsResponse()
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

    def DescribeKeyPairs(self, request):
        response = self._api_call("DescribeKeyPairs", request)

        model = models.DescribeKeyPairsResponse()
        model._deserialize(response)
        return model


    def ModifyKeyPairAttribute(self, request):
        response = self._api_call("ModifyKeyPairAttribute", request)

        model = models.ModifyKeyPairAttributeResponse()
        model._deserialize(response)
        return model


    def DeleteKeyPairs(self, request):
        response = self._api_call("DeleteKeyPairs", request)

        model = models.DeleteKeyPairsResponse()
        model._deserialize(response)
        return model


    def ImportKeyPair(self, request):
        response = self._api_call("ImportKeyPair", request)

        model = models.ImportKeyPairResponse()
        model._deserialize(response)
        return model