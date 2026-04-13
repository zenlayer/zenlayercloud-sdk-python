#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.bmc.v20260201 import models
from zenlayercloud.common.abstract_client import AbstractClient


class BmcClient(AbstractClient):
    _api_version = "2026-02-01"
    _service = "bmc"

    def DescribeSubnetAvailableResources(self, request):
        """
        本接口用于查询可创建Subnet资源的可用区。
        """
        response = self._api_call("DescribeSubnetAvailableResources", request)
        model = models.DescribeSubnetAvailableResourcesResponse()
        model._deserialize(response)
        return model

    def ModifySubnetsAttribute(self, request):
        """
        本接口用于修改Subnet的属性（目前只支持修改Subnet的名称）。
        """
        response = self._api_call("ModifySubnetsAttribute", request)
        model = models.ModifySubnetsAttributeResponse()
        model._deserialize(response)
        return model

    def CreateSubnet(self, request):
        """
        本接口用于创建一个私有网络Subnet。
        """
        response = self._api_call("CreateSubnet", request)
        model = models.CreateSubnetResponse()
        model._deserialize(response)
        return model

    def DescribeSubnets(self, request):
        """
        本接口用于查询一台或多台指定Subnet的信息。用户可以根据Subnet ID、VPC ID、 区域、Subnet 名称等信息来搜索Subnet信息。
        """
        response = self._api_call("DescribeSubnets", request)
        model = models.DescribeSubnetsResponse()
        model._deserialize(response)
        return model

    def AssociateSubnetInstances(self, request):
        """
        本接口用于将一台或多台实例加入同一个子网并分配内网IP。
        """
        response = self._api_call("AssociateSubnetInstances", request)
        model = models.AssociateSubnetInstancesResponse()
        model._deserialize(response)
        return model

    def UnAssociateSubnetInstance(self, request):
        """
        本接口用于将某子网下一台实例从Subnet中解绑。
        """
        response = self._api_call("UnAssociateSubnetInstance", request)
        model = models.UnAssociateSubnetInstanceResponse()
        model._deserialize(response)
        return model

    def AssociateVpcSubnet(self, request):
        """
        本接口用于为VPC添加Subnet。
        """
        response = self._api_call("AssociateVpcSubnet", request)
        model = models.AssociateVpcSubnetResponse()
        model._deserialize(response)
        return model

    def DeleteSubnet(self, request):
        """
        本接口用于删除一个Subnet。
        """
        response = self._api_call("DeleteSubnet", request)
        model = models.DeleteSubnetResponse()
        model._deserialize(response)
        return model

    def DescribeZones(self, request):
        """
        查询可用区信息。​
        """
        response = self._api_call("DescribeZones", request)
        model = models.DescribeZonesResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceTypes(self, request):
        """
        查询实例机型配置。
        """
        response = self._api_call("DescribeInstanceTypes", request)
        model = models.DescribeInstanceTypesResponse()
        model._deserialize(response)
        return model

    def DescribeAvailableResources(self, request):
        """
        查询售卖实例和带宽的可用资源。
        """
        response = self._api_call("DescribeAvailableResources", request)
        model = models.DescribeAvailableResourcesResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateInstance(self, request):
        """
        创建一个实例询价。
        """
        response = self._api_call("InquiryPriceCreateInstance", request)
        model = models.InquiryPriceCreateInstanceResponse()
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

    def CreateInstances(self, request):
        """
        创建一个或多个指定配置的实例。
        """
        response = self._api_call("CreateInstances", request)
        model = models.CreateInstancesResponse()
        model._deserialize(response)
        return model

    def DescribeInstances(self, request):
        """
        查询一台或多台实例的信息。用户可以根据实例ID、实例名称或者实例计费模式等条件来查询实例的详细信息。
        """
        response = self._api_call("DescribeInstances", request)
        model = models.DescribeInstancesResponse()
        model._deserialize(response)
        return model

    def ModifyInstancesAttribute(self, request):
        """
        本接口用于修改实例的属性（目前只支持修改实例的显示名称）。
        """
        response = self._api_call("ModifyInstancesAttribute", request)
        model = models.ModifyInstancesAttributeResponse()
        model._deserialize(response)
        return model

    def StartInstances(self, request):
        """
        本接口用于启动一个或多个实例。
        """
        response = self._api_call("StartInstances", request)
        model = models.StartInstancesResponse()
        model._deserialize(response)
        return model

    def StopInstances(self, request):
        """
        本接口用于关闭一个或多个实例。
        """
        response = self._api_call("StopInstances", request)
        model = models.StopInstancesResponse()
        model._deserialize(response)
        return model

    def RebootInstances(self, request):
        """
        本接口用于重启一个或多个实例。
        """
        response = self._api_call("RebootInstances", request)
        model = models.RebootInstancesResponse()
        model._deserialize(response)
        return model

    def ReinstallInstance(self, request):
        """
        本接口用于重装一个实例。
        """
        response = self._api_call("ReinstallInstance", request)
        model = models.ReinstallInstanceResponse()
        model._deserialize(response)
        return model

    def ModifyInstancesResourceGroup(self, request):
        """
        修改实例所属的资源组。
        """
        response = self._api_call("ModifyInstancesResourceGroup", request)
        model = models.ModifyInstancesResourceGroupResponse()
        model._deserialize(response)
        return model

    def TerminateInstance(self, request):
        """
        本接口用于退还一个实例。
        """
        response = self._api_call("TerminateInstance", request)
        model = models.TerminateInstanceResponse()
        model._deserialize(response)
        return model

    def RenewInstance(self, request):
        """
        本接口用于续费一个实例。
        """
        response = self._api_call("RenewInstance", request)
        model = models.RenewInstanceResponse()
        model._deserialize(response)
        return model

    def ReleaseInstances(self, request):
        """
        本接口用于释放一个或多个实例。
        """
        response = self._api_call("ReleaseInstances", request)
        model = models.ReleaseInstancesResponse()
        model._deserialize(response)
        return model

    def InquiryPriceInstanceBandwidth(self, request):
        """
        实例修改带宽询价。
        """
        response = self._api_call("InquiryPriceInstanceBandwidth", request)
        model = models.InquiryPriceInstanceBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceBandwidth(self, request):
        """
        修改实例带宽。
        """
        response = self._api_call("ModifyInstanceBandwidth", request)
        model = models.ModifyInstanceBandwidthResponse()
        model._deserialize(response)
        return model

    def CancelInstanceBandwidthDowngrade(self, request):
        """
        取消带宽降配订单。
        """
        response = self._api_call("CancelInstanceBandwidthDowngrade", request)
        model = models.CancelInstanceBandwidthDowngradeResponse()
        model._deserialize(response)
        return model

    def InquiryPriceInstanceTrafficPackage(self, request):
        """
        实例修改流量包询价。
        """
        response = self._api_call("InquiryPriceInstanceTrafficPackage", request)
        model = models.InquiryPriceInstanceTrafficPackageResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceTrafficPackage(self, request):
        """
        修改实例流量包。
        """
        response = self._api_call("ModifyInstanceTrafficPackage", request)
        model = models.ModifyInstanceTrafficPackageResponse()
        model._deserialize(response)
        return model

    def CancelInstanceTrafficPackageDowngrade(self, request):
        """
        取消流量包降配订单。
        """
        response = self._api_call("CancelInstanceTrafficPackageDowngrade", request)
        model = models.CancelInstanceTrafficPackageDowngradeResponse()
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

    def DescribeInstanceTraffic(self, request):
        """
        查询实例指定时间段内的流量信息。
        """
        response = self._api_call("DescribeInstanceTraffic", request)
        model = models.DescribeInstanceTrafficResponse()
        model._deserialize(response)
        return model

    def DescribeInstancesMonitorHealth(self, request):
        """
        查询实例的硬件状态信息。
        """
        response = self._api_call("DescribeInstancesMonitorHealth", request)
        model = models.DescribeInstancesMonitorHealthResponse()
        model._deserialize(response)
        return model

    def DescribeAvailableIpv4Resources(self, request):
        """
        查询可售的Ipv4 Cidr Block资源。
        """
        response = self._api_call("DescribeAvailableIpv4Resources", request)
        model = models.DescribeAvailableIpv4ResourcesResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateIpv4Block(self, request):
        """
        创建Ipv4 CidrBlock询价。
        """
        response = self._api_call("InquiryPriceCreateIpv4Block", request)
        model = models.InquiryPriceCreateIpv4BlockResponse()
        model._deserialize(response)
        return model

    def CreateIpv4Block(self, request):
        """
        创建一个或多个Ipv4 Cidr Block。
        """
        response = self._api_call("CreateIpv4Block", request)
        model = models.CreateIpv4BlockResponse()
        model._deserialize(response)
        return model

    def DescribeAvailableIpv6Resources(self, request):
        """
        查询可售的Ipv6 Cidr Block资源。
        """
        response = self._api_call("DescribeAvailableIpv6Resources", request)
        model = models.DescribeAvailableIpv6ResourcesResponse()
        model._deserialize(response)
        return model

    def CreateIpv6Block(self, request):
        """
        创建一个或多个IPv6 Cidr Block。
        """
        response = self._api_call("CreateIpv6Block", request)
        model = models.CreateIpv6BlockResponse()
        model._deserialize(response)
        return model

    def DescribeCidrBlocks(self, request):
        """
        查询一个或多个Cidr Block的信息。
        """
        response = self._api_call("DescribeCidrBlocks", request)
        model = models.DescribeCidrBlocksResponse()
        model._deserialize(response)
        return model

    def ModifyCidrBlocksAttribute(self, request):
        """
        本接口用于修改一个或多个Cidr Block的属性（目前只支持修改名称）。
        """
        response = self._api_call("ModifyCidrBlocksAttribute", request)
        model = models.ModifyCidrBlocksAttributeResponse()
        model._deserialize(response)
        return model

    def RenewCidrBlock(self, request):
        """
        本接口用于续费一个Cidr Block。
        """
        response = self._api_call("RenewCidrBlock", request)
        model = models.RenewCidrBlockResponse()
        model._deserialize(response)
        return model

    def TerminateCidrBlock(self, request):
        """
        本接口用于退还一个Cidr Block。
        """
        response = self._api_call("TerminateCidrBlock", request)
        model = models.TerminateCidrBlockResponse()
        model._deserialize(response)
        return model

    def ReleaseCidrBlocks(self, request):
        """
        释放一个或多个Ipv4 Cidr Block。
        """
        response = self._api_call("ReleaseCidrBlocks", request)
        model = models.ReleaseCidrBlocksResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceAvailableCidrBlock(self, request):
        """
        查询实例可用的Cidr Block。
        """
        response = self._api_call("DescribeInstanceAvailableCidrBlock", request)
        model = models.DescribeInstanceAvailableCidrBlockResponse()
        model._deserialize(response)
        return model

    def DescribeCidrBlockIps(self, request):
        """
        查询一个Cidr Block的IP列表。
        """
        response = self._api_call("DescribeCidrBlockIps", request)
        model = models.DescribeCidrBlockIpsResponse()
        model._deserialize(response)
        return model

    def BindCidrBlockIps(self, request):
        """
        实例绑定一个或多个Cidr Block IP。
        """
        response = self._api_call("BindCidrBlockIps", request)
        model = models.BindCidrBlockIpsResponse()
        model._deserialize(response)
        return model

    def UnbindCidrBlockIps(self, request):
        """
        实例解绑一个或多个Cidr Block IP。
        """
        response = self._api_call("UnbindCidrBlockIps", request)
        model = models.UnbindCidrBlockIpsResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateEipAddress(self, request):
        """
        创建EIP询价。
        """
        response = self._api_call("InquiryPriceCreateEipAddress", request)
        model = models.InquiryPriceCreateEipAddressResponse()
        model._deserialize(response)
        return model

    def DescribeEipAddresses(self, request):
        """
        查询一台或多台指定EIP的信息。用户可以根据EIP ID、IP或者计费模式等信息来搜索EIP的信息。
        """
        response = self._api_call("DescribeEipAddresses", request)
        model = models.DescribeEipAddressesResponse()
        model._deserialize(response)
        return model

    def AllocateEipAddresses(self, request):
        """
        创建一个或多个EIP。
        """
        response = self._api_call("AllocateEipAddresses", request)
        model = models.AllocateEipAddressesResponse()
        model._deserialize(response)
        return model

    def ModifyEipAddressesResourceGroup(self, request):
        """
        修改弹性IP所属的资源组。
        """
        response = self._api_call("ModifyEipAddressesResourceGroup", request)
        model = models.ModifyEipAddressesResourceGroupResponse()
        model._deserialize(response)
        return model

    def DescribeInstanceAvailableEipResources(self, request):
        """
        查询实例可绑定的EIP列表。
        """
        response = self._api_call("DescribeInstanceAvailableEipResources", request)
        model = models.DescribeInstanceAvailableEipResourcesResponse()
        model._deserialize(response)
        return model

    def AssociateEipAddress(self, request):
        """
        将EIP绑定到同区域的机器实例上。
        """
        response = self._api_call("AssociateEipAddress", request)
        model = models.AssociateEipAddressResponse()
        model._deserialize(response)
        return model

    def UnAssociateEipAddress(self, request):
        """
        将EIP上已绑定的机器实例解绑。
        """
        response = self._api_call("UnAssociateEipAddress", request)
        model = models.UnAssociateEipAddressResponse()
        model._deserialize(response)
        return model

    def DescribeEipAvailableResources(self, request):
        """
        查询区域可购买EIP资源。
        """
        response = self._api_call("DescribeEipAvailableResources", request)
        model = models.DescribeEipAvailableResourcesResponse()
        model._deserialize(response)
        return model

    def TerminateEipAddress(self, request):
        """
        本接口用于退还一个EIP。
        """
        response = self._api_call("TerminateEipAddress", request)
        model = models.TerminateEipAddressResponse()
        model._deserialize(response)
        return model

    def RenewEipAddress(self, request):
        """
        本接口用于续费一个EIP。
        """
        response = self._api_call("RenewEipAddress", request)
        model = models.RenewEipAddressResponse()
        model._deserialize(response)
        return model

    def ReleaseEipAddresses(self, request):
        """
        释放一个或多个EIP。
        """
        response = self._api_call("ReleaseEipAddresses", request)
        model = models.ReleaseEipAddressesResponse()
        model._deserialize(response)
        return model

    def DescribeVpcAvailableRegions(self, request):
        """
        本接口用于查询支持VPC组网的节点区域信息。
        """
        response = self._api_call("DescribeVpcAvailableRegions", request)
        model = models.DescribeVpcAvailableRegionsResponse()
        model._deserialize(response)
        return model

    def CreateVpc(self, request):
        """
        本接口用于创建一个私有网络VPC。
        """
        response = self._api_call("CreateVpc", request)
        model = models.CreateVpcResponse()
        model._deserialize(response)
        return model

    def DescribeVpcs(self, request):
        """
        本接口用于查询一个或多个指定VPC的信息。用户可以根据VPC ID、Subnet ID、 VPC节点ID、VPC名称等信息来搜索VPC信息。
        """
        response = self._api_call("DescribeVpcs", request)
        model = models.DescribeVpcsResponse()
        model._deserialize(response)
        return model

    def ModifyVpcsAttribute(self, request):
        """
        本接口用于修改VPC的属性（目前只支持修改VPC的名称）。
        """
        response = self._api_call("ModifyVpcsAttribute", request)
        model = models.ModifyVpcsAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteVpc(self, request):
        """
        本接口用于删除一个Vpc。
        """
        response = self._api_call("DeleteVpc", request)
        model = models.DeleteVpcResponse()
        model._deserialize(response)
        return model

    def DescribeLoadBalancerZones(self, request):
        """
        查询支持创建负载均衡的区域。
        """
        response = self._api_call("DescribeLoadBalancerZones", request)
        model = models.DescribeLoadBalancerZonesResponse()
        model._deserialize(response)
        return model

    def DescribeLoadBalancerSpecs(self, request):
        """
        查询可用区节点下可用的负载均衡规格列表。
        """
        response = self._api_call("DescribeLoadBalancerSpecs", request)
        model = models.DescribeLoadBalancerSpecsResponse()
        model._deserialize(response)
        return model

    def CreateLoadBalancer(self, request):
        """
        创建负载均衡实例。
        """
        response = self._api_call("CreateLoadBalancer", request)
        model = models.CreateLoadBalancerResponse()
        model._deserialize(response)
        return model

    def DescribeLoadBalancers(self, request):
        """
        查询一台或多台指定负载均衡实例的信息。用户可以根据负载均衡实例的ID、可用区等信息来搜索负载均衡实例的信息。
        """
        response = self._api_call("DescribeLoadBalancers", request)
        model = models.DescribeLoadBalancersResponse()
        model._deserialize(response)
        return model

    def ModifyLoadBalancersName(self, request):
        """
        修改负载均衡实例的名称。
        """
        response = self._api_call("ModifyLoadBalancersName", request)
        model = models.ModifyLoadBalancersNameResponse()
        model._deserialize(response)
        return model

    def TerminateLoadBalancer(self, request):
        """
        终止负载均衡实例。
        """
        response = self._api_call("TerminateLoadBalancer", request)
        model = models.TerminateLoadBalancerResponse()
        model._deserialize(response)
        return model

    def RestoreLoadBalancer(self, request):
        """
        恢复被删除的负载均衡实例。
        """
        response = self._api_call("RestoreLoadBalancer", request)
        model = models.RestoreLoadBalancerResponse()
        model._deserialize(response)
        return model

    def ReleaseLoadBalancer(self, request):
        """
        释放负载均衡实例。
        """
        response = self._api_call("ReleaseLoadBalancer", request)
        model = models.ReleaseLoadBalancerResponse()
        model._deserialize(response)
        return model

    def CreateListener(self, request):
        """
        在网络型负载均衡实例中创建TCP、UDP或TCPSSL监听。
        """
        response = self._api_call("CreateListener", request)
        model = models.CreateListenerResponse()
        model._deserialize(response)
        return model

    def DescribeListeners(self, request):
        """
        查询一台或多台指定Listener的信息。用户可以根据负载均衡实例的ID、监听器的ID等信息来搜索监听器的信息。
        """
        response = self._api_call("DescribeListeners", request)
        model = models.DescribeListenersResponse()
        model._deserialize(response)
        return model

    def ModifyListenerAttribute(self, request):
        """
        修改监听器配置。
        """
        response = self._api_call("ModifyListenerAttribute", request)
        model = models.ModifyListenerAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteListener(self, request):
        """
        删除负载均衡监听器。
        """
        response = self._api_call("DeleteListener", request)
        model = models.DeleteListenerResponse()
        model._deserialize(response)
        return model

    def CreateLoadBalancerVIPs(self, request):
        """
        创建负载均衡的VIP。
        """
        response = self._api_call("CreateLoadBalancerVIPs", request)
        model = models.CreateLoadBalancerVIPsResponse()
        model._deserialize(response)
        return model

    def DeleteLoadBalancerVIP(self, request):
        """
        删除负载均衡的IP。
        """
        response = self._api_call("DeleteLoadBalancerVIP", request)
        model = models.DeleteLoadBalancerVIPResponse()
        model._deserialize(response)
        return model

    def DescribeBackends(self, request):
        """
        查询一台或多台指定后端配置服务器的信息。用户可以根据监听器的ID、后端配置服务器的ID等信息来搜索后端配置服务器的信息。
        """
        response = self._api_call("DescribeBackends", request)
        model = models.DescribeBackendsResponse()
        model._deserialize(response)
        return model

    def RegisterBackend(self, request):
        """
        创建将一台后端服务绑定到负载均衡的监听器。
        """
        response = self._api_call("RegisterBackend", request)
        model = models.RegisterBackendResponse()
        model._deserialize(response)
        return model

    def DeregisterBackend(self, request):
        """
        删除负载均衡后端配置服务器。
        """
        response = self._api_call("DeregisterBackend", request)
        model = models.DeregisterBackendResponse()
        model._deserialize(response)
        return model

    def DescribeManagedInstances(self, request):
        """
        本接口用于查询一台或多台实例的信息。用户可以根据实例ID、实例名称等条件来查询实例的详细信息。
        """
        response = self._api_call("DescribeManagedInstances", request)
        model = models.DescribeManagedInstancesResponse()
        model._deserialize(response)
        return model

    def DescribeManagedInstanceTraffic(self, request):
        """
        查询托管实例指定时间段内的流量信息。
        """
        response = self._api_call("DescribeManagedInstanceTraffic", request)
        model = models.DescribeManagedInstanceTrafficResponse()
        model._deserialize(response)
        return model

