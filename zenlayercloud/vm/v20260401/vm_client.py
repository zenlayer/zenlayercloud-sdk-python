#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.vm.v20260401 import models
from zenlayercloud.common.abstract_client import AbstractClient


class VmClient(AbstractClient):
    _api_version = "2026-04-01"
    _service = "vm"

    def CreateVpc(self, request):
        """
        创建VPC。
        """
        response = self._api_call("CreateVpc", request)
        model = models.CreateVpcResponse()
        model._deserialize(response)
        return model

    def CreateVpcSubnet(self, request):
        """
        创建VPC的子网。
        """
        response = self._api_call("CreateVpcSubnet", request)
        model = models.CreateVpcSubnetResponse()
        model._deserialize(response)
        return model

    def DeleteVpcSubnet(self, request):
        """
        删除一个VPC子网。
        """
        response = self._api_call("DeleteVpcSubnet", request)
        model = models.DeleteVpcSubnetResponse()
        model._deserialize(response)
        return model

    def ModifyVpcSubnetsAttribute(self, request):
        """
        修改VPC子网的属性（目前只支持修改VPC子网的名称）。
        """
        response = self._api_call("ModifyVpcSubnetsAttribute", request)
        model = models.ModifyVpcSubnetsAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeVpcSubnets(self, request):
        """
        查询一台或多台指定子网的信息。用户可以根据Subnet ID、VPC ID、Subnet名称等信息来搜索Subnet信息。
        """
        response = self._api_call("DescribeVpcSubnets", request)
        model = models.DescribeVpcSubnetsResponse()
        model._deserialize(response)
        return model

    def ModifyVpcsAttribute(self, request):
        """
        修改VPC的属性（目前只支持修改VPC的名称）。
        """
        response = self._api_call("ModifyVpcsAttribute", request)
        model = models.ModifyVpcsAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeVpcs(self, request):
        """
        查询一台或多台指定子网的信息。用户可以根据VPC ID、VPC名称等信息来搜索VPC信息。
        """
        response = self._api_call("DescribeVpcs", request)
        model = models.DescribeVpcsResponse()
        model._deserialize(response)
        return model

    def DeleteVpc(self, request):
        """
        删除一个VPC。
        """
        response = self._api_call("DeleteVpc", request)
        model = models.DeleteVpcResponse()
        model._deserialize(response)
        return model

    def ConfigureSecurityGroupRules(self, request):
        """
        配置安全组的规则。
        """
        response = self._api_call("ConfigureSecurityGroupRules", request)
        model = models.ConfigureSecurityGroupRulesResponse()
        model._deserialize(response)
        return model

    def RevokeSecurityGroupRules(self, request):
        """
        移除安全组的规则。
        """
        response = self._api_call("RevokeSecurityGroupRules", request)
        model = models.RevokeSecurityGroupRulesResponse()
        model._deserialize(response)
        return model

    def AssociateSecurityGroupInstance(self, request):
        """
        为安全组绑定实例。
        """
        response = self._api_call("AssociateSecurityGroupInstance", request)
        model = models.AssociateSecurityGroupInstanceResponse()
        model._deserialize(response)
        return model

    def UnAssociateSecurityGroupInstance(self, request):
        """
        为安全组解绑实例。
        """
        response = self._api_call("UnAssociateSecurityGroupInstance", request)
        model = models.UnAssociateSecurityGroupInstanceResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceAvailableSecurityGroupResources(self, request):
        """
        获取实例可绑定的安全组。
        """
        response = self._api_call("DescribeInstanceAvailableSecurityGroupResources", request)
        model = models.DescribeInstanceAvailableSecurityGroupResourcesResponse()
        model._deserialize(response)
        return model

    def CreateSecurityGroup(self, request):
        """
        创建安全组。
        """
        response = self._api_call("CreateSecurityGroup", request)
        model = models.CreateSecurityGroupResponse()
        model._deserialize(response)
        return model

    def DeleteSecurityGroup(self, request):
        """
        删除安全组。
        """
        response = self._api_call("DeleteSecurityGroup", request)
        model = models.DeleteSecurityGroupResponse()
        model._deserialize(response)
        return model

    def AuthorizeSecurityGroupRule(self, request):
        """
        新增安全组单条规则。
        """
        response = self._api_call("AuthorizeSecurityGroupRule", request)
        model = models.AuthorizeSecurityGroupRuleResponse()
        model._deserialize(response)
        return model

    def AuthorizeSecurityGroupRules(self, request):
        """
        新增安全组的规则。
        """
        response = self._api_call("AuthorizeSecurityGroupRules", request)
        model = models.AuthorizeSecurityGroupRulesResponse()
        model._deserialize(response)
        return model

    def DescribeSecurityGroups(self, request):
        """
        查询一个或多个指定安全组的信息。用户可以根据安全组ID、安全组名称等信息来搜索安全组信息。
        """
        response = self._api_call("DescribeSecurityGroups", request)
        model = models.DescribeSecurityGroupsResponse()
        model._deserialize(response)
        return model

    def ModifySecurityGroupsAttribute(self, request):
        """
        修改安全组的属性（目前只支持修改安全组的名称）。
        """
        response = self._api_call("ModifySecurityGroupsAttribute", request)
        model = models.ModifySecurityGroupsAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteSubnet(self, request):
        """
        删除一个子网。
        """
        response = self._api_call("DeleteSubnet", request)
        model = models.DeleteSubnetResponse()
        model._deserialize(response)
        return model

    def ModifySubnetsAttribute(self, request):
        """
        修改子网的属性（目前只支持修改子网的名称）。
        """
        response = self._api_call("ModifySubnetsAttribute", request)
        model = models.ModifySubnetsAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeSubnets(self, request):
        """
        查询一台或多台指定子网的信息。用户可以根据Subnet ID、区域、Subnet名称等信息来搜索Subnet信息。
        """
        response = self._api_call("DescribeSubnets", request)
        model = models.DescribeSubnetsResponse()
        model._deserialize(response)
        return model

    def CreateSubnet(self, request):
        """
        创建子网。
        """
        response = self._api_call("CreateSubnet", request)
        model = models.CreateSubnetResponse()
        model._deserialize(response)
        return model

    def DeleteImages(self, request):
        """
        删除一个或多个镜像。
        """
        response = self._api_call("DeleteImages", request)
        model = models.DeleteImagesResponse()
        model._deserialize(response)
        return model

    def CreateImage(self, request):
        """
        创建自定义镜像。
        """
        response = self._api_call("CreateImage", request)
        model = models.CreateImageResponse()
        model._deserialize(response)
        return model

    def DescribeImages(self, request):
        """
        查看镜像列表。
        """
        response = self._api_call("DescribeImages", request)
        model = models.DescribeImagesResponse()
        model._deserialize(response)
        return model

    def ModifyImagesAttributes(self, request):
        """
        修改镜像属性。
        """
        response = self._api_call("ModifyImagesAttributes", request)
        model = models.ModifyImagesAttributesResponse()
        model._deserialize(response)
        return model

    def DescribeImageQuota(self, request):
        """
        查询可创建镜像的配额。
        """
        response = self._api_call("DescribeImageQuota", request)
        model = models.DescribeImageQuotaResponse()
        model._deserialize(response)
        return model

    def DescribeZones(self, request):
        """
        查询可用地区。
        """
        response = self._api_call("DescribeZones", request)
        model = models.DescribeZonesResponse()
        model._deserialize(response)
        return model

    def ResetInstancesPassword(self, request):
        """
        将虚拟机实例操作系统的密码重置为用户指定的密码。
        """
        response = self._api_call("ResetInstancesPassword", request)
        model = models.ResetInstancesPasswordResponse()
        model._deserialize(response)
        return model

    def ResetInstance(self, request):
        """
        重装一台虚拟机实例上的操作系统。
        """
        response = self._api_call("ResetInstance", request)
        model = models.ResetInstanceResponse()
        model._deserialize(response)
        return model

    def TerminateInstance(self, request):
        """
        退还一个虚拟机实例。
        """
        response = self._api_call("TerminateInstance", request)
        model = models.TerminateInstanceResponse()
        model._deserialize(response)
        return model

    def ReleaseInstances(self, request):
        """
        释放一个或多个虚拟机实例。
        """
        response = self._api_call("ReleaseInstances", request)
        model = models.ReleaseInstancesResponse()
        model._deserialize(response)
        return model

    def ModifyInstancesResourceGroup(self, request):
        """
        修改虚拟机实例所属的资源组。
        """
        response = self._api_call("ModifyInstancesResourceGroup", request)
        model = models.ModifyInstancesResourceGroupResponse()
        model._deserialize(response)
        return model

    def CancelInstanceTrafficPackageDowngrade(self, request):
        """
        取消虚拟机实例流量包降配订单。
        """
        response = self._api_call("CancelInstanceTrafficPackageDowngrade", request)
        model = models.CancelInstanceTrafficPackageDowngradeResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceTrafficPackage(self, request):
        """
        修改虚拟机实例流量包大小。
        """
        response = self._api_call("ModifyInstanceTrafficPackage", request)
        model = models.ModifyInstanceTrafficPackageResponse()
        model._deserialize(response)
        return model

    def InquiryPriceInstanceTrafficPackage(self, request):
        """
        虚拟机实例修改流量包询价。
        """
        response = self._api_call("InquiryPriceInstanceTrafficPackage", request)
        model = models.InquiryPriceInstanceTrafficPackageResponse()
        model._deserialize(response)
        return model

    def DescribeVncUrl(self, request):
        """
        获取实例VNC地址。
        """
        response = self._api_call("DescribeVncUrl", request)
        model = models.DescribeVncUrlResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceTraffic(self, request):
        """
        查询实例指定时间段内的流量信息。
        """
        response = self._api_call("DescribeInstanceTraffic", request)
        model = models.DescribeInstanceTrafficResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceCpuMonitor(self, request):
        """
        查询实例指定时间段内的CPU使用率。
        """
        response = self._api_call("DescribeInstanceCpuMonitor", request)
        model = models.DescribeInstanceCpuMonitorResponse()
        model._deserialize(response)
        return model

    def StartInstances(self, request):
        """
        启动一个或多个虚拟机实例。
        """
        response = self._api_call("StartInstances", request)
        model = models.StartInstancesResponse()
        model._deserialize(response)
        return model

    def CreateInstances(self, request):
        """
        创建一个或多个指定配置的虚拟机实例。
        """
        response = self._api_call("CreateInstances", request)
        model = models.CreateInstancesResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateInstance(self, request):
        """
        创建一台虚拟机实例询价。
        """
        response = self._api_call("InquiryPriceCreateInstance", request)
        model = models.InquiryPriceCreateInstanceResponse()
        model._deserialize(response)
        return model

    def DescribeInstancesStatus(self, request):
        """
        查询一台或多台虚拟机实例的状态。
        """
        response = self._api_call("DescribeInstancesStatus", request)
        model = models.DescribeInstancesStatusResponse()
        model._deserialize(response)
        return model

    def ModifyInstancesAttribute(self, request):
        """
        修改虚拟机实例的属性（目前只支持修改实例的显示名称）。
        """
        response = self._api_call("ModifyInstancesAttribute", request)
        model = models.ModifyInstancesAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeInstances(self, request):
        """
        查询一台或多台虚拟机实例的信息。用户可以根据实例ID、实例名称或者实例计费模式等条件来查询实例的详细信息。
        """
        response = self._api_call("DescribeInstances", request)
        model = models.DescribeInstancesResponse()
        model._deserialize(response)
        return model

    def StopInstances(self, request):
        """
        关闭一个或多个虚拟机实例。
        """
        response = self._api_call("StopInstances", request)
        model = models.StopInstancesResponse()
        model._deserialize(response)
        return model

    def RebootInstances(self, request):
        """
        重启一个或多个虚拟机实例。
        """
        response = self._api_call("RebootInstances", request)
        model = models.RebootInstancesResponse()
        model._deserialize(response)
        return model

    def DescribeZoneInstanceConfigInfos(self, request):
        """
        查询售卖可用区的机型信息。
        """
        response = self._api_call("DescribeZoneInstanceConfigInfos", request)
        model = models.DescribeZoneInstanceConfigInfosResponse()
        model._deserialize(response)
        return model

    def CancelInstanceBandwidthDowngrade(self, request):
        """
        取消虚拟机实例带宽降配订单。
        """
        response = self._api_call("CancelInstanceBandwidthDowngrade", request)
        model = models.CancelInstanceBandwidthDowngradeResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceBandwidth(self, request):
        """
        修改虚拟机实例的公网出口带宽。
        """
        response = self._api_call("ModifyInstanceBandwidth", request)
        model = models.ModifyInstanceBandwidthResponse()
        model._deserialize(response)
        return model

    def InquiryPriceInstanceBandwidth(self, request):
        """
        虚拟机实例修改带宽询价。
        """
        response = self._api_call("InquiryPriceInstanceBandwidth", request)
        model = models.InquiryPriceInstanceBandwidthResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceInternetStatus(self, request):
        """
        查询实例带宽、流量包状态。
        """
        response = self._api_call("DescribeInstanceInternetStatus", request)
        model = models.DescribeInstanceInternetStatusResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceType(self, request):
        """
        修改一台虚拟机实例的机型。
        """
        response = self._api_call("ModifyInstanceType", request)
        model = models.ModifyInstanceTypeResponse()
        model._deserialize(response)
        return model

    def CancelInstanceDowngrade(self, request):
        """
        取消虚拟机实例降配订单。
        """
        response = self._api_call("CancelInstanceDowngrade", request)
        model = models.CancelInstanceDowngradeResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceTypeStatus(self, request):
        """
        查询实例变配后的机型状态。
        """
        response = self._api_call("DescribeInstanceTypeStatus", request)
        model = models.DescribeInstanceTypeStatusResponse()
        model._deserialize(response)
        return model

    def DetachDisks(self, request):
        """
        从云主机实例上卸载云硬盘。
        """
        response = self._api_call("DetachDisks", request)
        model = models.DetachDisksResponse()
        model._deserialize(response)
        return model

    def ModifyDisksAttributes(self, request):
        """
        修改一个或多个云硬盘属性。
        """
        response = self._api_call("ModifyDisksAttributes", request)
        model = models.ModifyDisksAttributesResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateDisks(self, request):
        """
        创建云硬盘询价。
        """
        response = self._api_call("InquiryPriceCreateDisks", request)
        model = models.InquiryPriceCreateDisksResponse()
        model._deserialize(response)
        return model

    def TerminateDisk(self, request):
        """
        终止云硬盘。
        """
        response = self._api_call("TerminateDisk", request)
        model = models.TerminateDiskResponse()
        model._deserialize(response)
        return model

    def CreateDisks(self, request):
        """
        创建一个或多个云硬盘。
        """
        response = self._api_call("CreateDisks", request)
        model = models.CreateDisksResponse()
        model._deserialize(response)
        return model

    def AttachDisks(self, request):
        """
        挂载云硬盘到云主机实例。
        """
        response = self._api_call("AttachDisks", request)
        model = models.AttachDisksResponse()
        model._deserialize(response)
        return model

    def DescribeDisks(self, request):
        """
        查询云硬盘列表。
        """
        response = self._api_call("DescribeDisks", request)
        model = models.DescribeDisksResponse()
        model._deserialize(response)
        return model

    def ModifyDisksResourceGroup(self, request):
        """
        修改云硬盘所属的资源组。
        """
        response = self._api_call("ModifyDisksResourceGroup", request)
        model = models.ModifyDisksResourceGroupResponse()
        model._deserialize(response)
        return model

    def DescribeDiskCategory(self, request):
        """
        查询云硬盘支持的类型。
        """
        response = self._api_call("DescribeDiskCategory", request)
        model = models.DescribeDiskCategoryResponse()
        model._deserialize(response)
        return model

    def ResizeDisk(self, request):
        """
        将一个云硬盘扩容到指定大小。
        """
        response = self._api_call("ResizeDisk", request)
        model = models.ResizeDiskResponse()
        model._deserialize(response)
        return model

    def ReleaseDisk(self, request):
        """
        释放云硬盘。
        """
        response = self._api_call("ReleaseDisk", request)
        model = models.ReleaseDiskResponse()
        model._deserialize(response)
        return model

    def RenewDisk(self, request):
        """
        续费云硬盘。
        """
        response = self._api_call("RenewDisk", request)
        model = models.RenewDiskResponse()
        model._deserialize(response)
        return model

    def ChangeDisksAttach(self, request):
        """
        将一个或多个已经挂载到一台实例的云硬盘挂载到另外一台实例上。
        """
        response = self._api_call("ChangeDisksAttach", request)
        model = models.ChangeDisksAttachResponse()
        model._deserialize(response)
        return model

