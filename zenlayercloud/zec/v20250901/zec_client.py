#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zec.v20250901 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZecClient(AbstractClient):
    _api_version = "2025-09-01"
    _service = "zec"

    def DescribeZones(self, request):
        """
        查询可用区信息。包括名称，所属的节点等。
        """
        response = self._api_call("DescribeZones", request)
        model = models.DescribeZonesResponse()
        model._deserialize(response)
        return model

    def DescribeZoneInstanceConfigInfos(self, request):
        """
        查询可用区售卖的机型信息
        """
        response = self._api_call("DescribeZoneInstanceConfigInfos", request)
        model = models.DescribeZoneInstanceConfigInfosResponse()
        model._deserialize(response)
        return model

    def DescribeTimeZones(self, request):
        """
        查询时区信息
        """
        response = self._api_call("DescribeTimeZones", request)
        model = models.DescribeTimeZonesResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateInstance(self, request):
        """
        创建虚拟机实例询价。
        """
        response = self._api_call("InquiryPriceCreateInstance", request)
        model = models.InquiryPriceCreateInstanceResponse()
        model._deserialize(response)
        return model

    def CreateZecInstances(self, request):
        """
        创建一台或多台虚拟机实例。
        """
        response = self._api_call("CreateZecInstances", request)
        model = models.CreateZecInstancesResponse()
        model._deserialize(response)
        return model

    def DescribeInstances(self, request):
        """
        查询一台或多台虚拟机实例的信息。用户可以根据实例ID、实例名称等条件来查询实例的详细信息。
        """
        response = self._api_call("DescribeInstances", request)
        model = models.DescribeInstancesResponse()
        model._deserialize(response)
        return model

    def DescribeInstancesStatus(self, request):
        """
        查询实例的状态。
        """
        response = self._api_call("DescribeInstancesStatus", request)
        model = models.DescribeInstancesStatusResponse()
        model._deserialize(response)
        return model

    def ModifyInstancesAttribute(self, request):
        """
        修改实例属性（名称）。
        """
        response = self._api_call("ModifyInstancesAttribute", request)
        model = models.ModifyInstancesAttributeResponse()
        model._deserialize(response)
        return model

    def StartInstances(self, request):
        """
        启动一台或多台虚拟机实例。
        """
        response = self._api_call("StartInstances", request)
        model = models.StartInstancesResponse()
        model._deserialize(response)
        return model

    def StopInstances(self, request):
        """
        关闭一台或多台虚拟机实例。
        """
        response = self._api_call("StopInstances", request)
        model = models.StopInstancesResponse()
        model._deserialize(response)
        return model

    def RebootInstances(self, request):
        """
        重启虚拟机实例。
        """
        response = self._api_call("RebootInstances", request)
        model = models.RebootInstancesResponse()
        model._deserialize(response)
        return model

    def ResetInstancePassword(self, request):
        """
        重置一台虚拟机实例密码。
        """
        response = self._api_call("ResetInstancePassword", request)
        model = models.ResetInstancePasswordResponse()
        model._deserialize(response)
        return model

    def ResetInstance(self, request):
        """
        重装一台虚拟机实例操作系统。
        """
        response = self._api_call("ResetInstance", request)
        model = models.ResetInstanceResponse()
        model._deserialize(response)
        return model

    def ResetInstances(self, request):
        """
        重装多台虚拟机实例操作系统。
        """
        response = self._api_call("ResetInstances", request)
        model = models.ResetInstancesResponse()
        model._deserialize(response)
        return model

    def StartIpForward(self, request):
        """
        开启IP转发
        """
        response = self._api_call("StartIpForward", request)
        model = models.StartIpForwardResponse()
        model._deserialize(response)
        return model

    def StopIpForward(self, request):
        """
        关闭IP转发
        """
        response = self._api_call("StopIpForward", request)
        model = models.StopIpForwardResponse()
        model._deserialize(response)
        return model

    def StartAgentMonitor(self, request):
        """
        开启Agent监控采集。
        """
        response = self._api_call("StartAgentMonitor", request)
        model = models.StartAgentMonitorResponse()
        model._deserialize(response)
        return model

    def StopAgentMonitor(self, request):
        """
        关闭Agent监控采集。
        """
        response = self._api_call("StopAgentMonitor", request)
        model = models.StopAgentMonitorResponse()
        model._deserialize(response)
        return model

    def ModifyInstanceType(self, request):
        """
        变更实例的规格
        """
        response = self._api_call("ModifyInstanceType", request)
        model = models.ModifyInstanceTypeResponse()
        model._deserialize(response)
        return model

    def ChangeNicNetworkType(self, request):
        """
        更改实例的网卡模式。
        """
        response = self._api_call("ChangeNicNetworkType", request)
        model = models.ChangeNicNetworkTypeResponse()
        model._deserialize(response)
        return model

    def ReleaseInstances(self, request):
        """
        销毁一台或多台虚拟机实例。
        """
        response = self._api_call("ReleaseInstances", request)
        model = models.ReleaseInstancesResponse()
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

    def DescribeInstanceMonitorData(self, request):
        """
        查询一段时间的实例的监控指标数据。包括CPU,内存等相关指标数据。
        """
        response = self._api_call("DescribeInstanceMonitorData", request)
        model = models.DescribeInstanceMonitorDataResponse()
        model._deserialize(response)
        return model

    def DescribeImages(self, request):
        """
        查询某节点支持的镜像列表。
        """
        response = self._api_call("DescribeImages", request)
        model = models.DescribeImagesResponse()
        model._deserialize(response)
        return model

    def CreateImage(self, request):
        """
        用实例创建自定义镜像。
        """
        response = self._api_call("CreateImage", request)
        model = models.CreateImageResponse()
        model._deserialize(response)
        return model

    def ModifyImagesAttributes(self, request):
        """
        修改自定义镜像属性。
        """
        response = self._api_call("ModifyImagesAttributes", request)
        model = models.ModifyImagesAttributesResponse()
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

    def DescribeDiskRegions(self, request):
        """
        支持售卖云硬盘的节点。
        """
        response = self._api_call("DescribeDiskRegions", request)
        model = models.DescribeDiskRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeDiskCategory(self, request):
        """
        获取某个区域支持的云盘类型。
        """
        response = self._api_call("DescribeDiskCategory", request)
        model = models.DescribeDiskCategoryResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateDisks(self, request):
        """
        创建一块或多块云硬盘的询价。
        """
        response = self._api_call("InquiryPriceCreateDisks", request)
        model = models.InquiryPriceCreateDisksResponse()
        model._deserialize(response)
        return model

    def DescribeDisks(self, request):
        """
        查询云盘的列表信息。
        """
        response = self._api_call("DescribeDisks", request)
        model = models.DescribeDisksResponse()
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
        云硬盘挂载到实例上。
        """
        response = self._api_call("AttachDisks", request)
        model = models.AttachDisksResponse()
        model._deserialize(response)
        return model

    def DetachDisks(self, request):
        """
        将云硬盘从主机实例上卸载。
        """
        response = self._api_call("DetachDisks", request)
        model = models.DetachDisksResponse()
        model._deserialize(response)
        return model

    def ModifyDisksAttributes(self, request):
        """
        修改一块或多块云硬盘属性。当前接口只支持修改名称。
        """
        response = self._api_call("ModifyDisksAttributes", request)
        model = models.ModifyDisksAttributesResponse()
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
        删除释放一块云硬盘。
        """
        response = self._api_call("ReleaseDisk", request)
        model = models.ReleaseDiskResponse()
        model._deserialize(response)
        return model

    def RenewDisk(self, request):
        """
        恢复云硬盘
        """
        response = self._api_call("RenewDisk", request)
        model = models.RenewDiskResponse()
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

    def DescribeDiskMonitorData(self, request):
        """
        查询一段时间的云硬盘的监控指标数据。
        """
        response = self._api_call("DescribeDiskMonitorData", request)
        model = models.DescribeDiskMonitorDataResponse()
        model._deserialize(response)
        return model

    def DescribeSnapshots(self, request):
        """
        查询快照的详细信息。
        """
        response = self._api_call("DescribeSnapshots", request)
        model = models.DescribeSnapshotsResponse()
        model._deserialize(response)
        return model

    def CreateSnapshot(self, request):
        """
        对指定云盘创建快照。
        """
        response = self._api_call("CreateSnapshot", request)
        model = models.CreateSnapshotResponse()
        model._deserialize(response)
        return model

    def ModifySnapshotsAttribute(self, request):
        """
        修改指定快照的属性。
        """
        response = self._api_call("ModifySnapshotsAttribute", request)
        model = models.ModifySnapshotsAttributeResponse()
        model._deserialize(response)
        return model

    def ApplySnapshot(self, request):
        """
        回滚快照到原云盘。
        """
        response = self._api_call("ApplySnapshot", request)
        model = models.ApplySnapshotResponse()
        model._deserialize(response)
        return model

    def DeleteSnapshots(self, request):
        """
        删除指定快照集合。
        """
        response = self._api_call("DeleteSnapshots", request)
        model = models.DeleteSnapshotsResponse()
        model._deserialize(response)
        return model

    def CreateAutoSnapshotPolicy(self, request):
        """
        创建一个自动快照策略。
        """
        response = self._api_call("CreateAutoSnapshotPolicy", request)
        model = models.CreateAutoSnapshotPolicyResponse()
        model._deserialize(response)
        return model

    def DescribeAutoSnapshotPolicies(self, request):
        """
        查询自动快照策略的列表数据。
        """
        response = self._api_call("DescribeAutoSnapshotPolicies", request)
        model = models.DescribeAutoSnapshotPoliciesResponse()
        model._deserialize(response)
        return model

    def ApplyAutoSnapshotPolicy(self, request):
        """
        云硬盘添加到指定的自动快照策略。
        """
        response = self._api_call("ApplyAutoSnapshotPolicy", request)
        model = models.ApplyAutoSnapshotPolicyResponse()
        model._deserialize(response)
        return model

    def CancelAutoSnapshotPolicy(self, request):
        """
        云硬盘从指定的自动快照策略中移除。
        """
        response = self._api_call("CancelAutoSnapshotPolicy", request)
        model = models.CancelAutoSnapshotPolicyResponse()
        model._deserialize(response)
        return model

    def ModifyAutoSnapshotPolicy(self, request):
        """
        修改自动快照策略的基本信息。
        """
        response = self._api_call("ModifyAutoSnapshotPolicy", request)
        model = models.ModifyAutoSnapshotPolicyResponse()
        model._deserialize(response)
        return model

    def DeleteAutoSnapshotPolicies(self, request):
        """
        删除指定的自动快照策略。
        """
        response = self._api_call("DeleteAutoSnapshotPolicies", request)
        model = models.DeleteAutoSnapshotPoliciesResponse()
        model._deserialize(response)
        return model

    def DescribeNetworkInterfaceRegions(self, request):
        """
        支持售卖网卡的区域信息
        """
        response = self._api_call("DescribeNetworkInterfaceRegions", request)
        model = models.DescribeNetworkInterfaceRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeNetworkInterfaces(self, request):
        """
        查询一个或多个指定网卡的信息。用户可以根据 网卡ID、网卡名称等信息来搜索网卡信息。
        """
        response = self._api_call("DescribeNetworkInterfaces", request)
        model = models.DescribeNetworkInterfacesResponse()
        model._deserialize(response)
        return model

    def ModifyNetworkInterfaceAttribute(self, request):
        """
        修改一张网卡的属性。
        """
        response = self._api_call("ModifyNetworkInterfaceAttribute", request)
        model = models.ModifyNetworkInterfaceAttributeResponse()
        model._deserialize(response)
        return model

    def ModifyNetworkInterfacesAttribute(self, request):
        """
        修改网卡的属性，目前只支持修改网卡的名称。
        """
        response = self._api_call("ModifyNetworkInterfacesAttribute", request)
        model = models.ModifyNetworkInterfacesAttributeResponse()
        model._deserialize(response)
        return model

    def CreateNetworkInterface(self, request):
        """
        创建一张辅助网卡。
        """
        response = self._api_call("CreateNetworkInterface", request)
        model = models.CreateNetworkInterfaceResponse()
        model._deserialize(response)
        return model

    def DeleteNetworkInterface(self, request):
        """
        删除一张辅助网卡。
        """
        response = self._api_call("DeleteNetworkInterface", request)
        model = models.DeleteNetworkInterfaceResponse()
        model._deserialize(response)
        return model

    def AttachNetworkInterface(self, request):
        """
        网卡绑定实例。
        """
        response = self._api_call("AttachNetworkInterface", request)
        model = models.AttachNetworkInterfaceResponse()
        model._deserialize(response)
        return model

    def DetachNetworkInterface(self, request):
        """
        将一张网卡从实例上解绑。
        """
        response = self._api_call("DetachNetworkInterface", request)
        model = models.DetachNetworkInterfaceResponse()
        model._deserialize(response)
        return model

    def AssignNetworkInterfaceIpv4(self, request):
        """
        网卡绑定内网IPv4
        """
        response = self._api_call("AssignNetworkInterfaceIpv4", request)
        model = models.AssignNetworkInterfaceIpv4Response()
        model._deserialize(response)
        return model

    def BatchAssignNetworkInterfaceIpv4(self, request):
        """
        将一张网卡额外添加内网IPv4地址。
        """
        response = self._api_call("BatchAssignNetworkInterfaceIpv4", request)
        model = models.BatchAssignNetworkInterfaceIpv4Response()
        model._deserialize(response)
        return model

    def UnassignNetworkInterfaceIpv4(self, request):
        """
        将网卡上的内网IPv4地址解绑。
        """
        response = self._api_call("UnassignNetworkInterfaceIpv4", request)
        model = models.UnassignNetworkInterfaceIpv4Response()
        model._deserialize(response)
        return model

    def DescribeNetworkInterfacePublicIPv6(self, request):
        """
        查询网卡的公网IPv6信息。
        """
        response = self._api_call("DescribeNetworkInterfacePublicIPv6", request)
        model = models.DescribeNetworkInterfacePublicIPv6Response()
        model._deserialize(response)
        return model

    def InquiryPricePublicIpv6(self, request):
        """
        公网Ipv6流量包或固定带宽询价。
        """
        response = self._api_call("InquiryPricePublicIpv6", request)
        model = models.InquiryPricePublicIpv6Response()
        model._deserialize(response)
        return model

    def AssignNetworkInterfaceIpv6(self, request):
        """
        给网卡添加IPv6。
        """
        response = self._api_call("AssignNetworkInterfaceIpv6", request)
        model = models.AssignNetworkInterfaceIpv6Response()
        model._deserialize(response)
        return model

    def DescribePools(self, request):
        """
        查询公网IP池列表。
        """
        response = self._api_call("DescribePools", request)
        model = models.DescribePoolsResponse()
        model._deserialize(response)
        return model

    def DescribeCidrRegions(self, request):
        """
        支持售卖CIDR的节点信息。
        """
        response = self._api_call("DescribeCidrRegions", request)
        model = models.DescribeCidrRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeCidrPrice(self, request):
        """
        查询IPv4 CIDR地址块售卖价格。
        """
        response = self._api_call("DescribeCidrPrice", request)
        model = models.DescribeCidrPriceResponse()
        model._deserialize(response)
        return model

    def DescribeCidrs(self, request):
        """
        查询IPv4 CIDR地址块列表
        """
        response = self._api_call("DescribeCidrs", request)
        model = models.DescribeCidrsResponse()
        model._deserialize(response)
        return model

    def CreateCidr(self, request):
        """
        创建IPv4 CIDR地址段。
        """
        response = self._api_call("CreateCidr", request)
        model = models.CreateCidrResponse()
        model._deserialize(response)
        return model

    def ModifyCidrAttribute(self, request):
        """
        修改IPv4 CIDR地址段的属性。 目前只能修改名称。
        """
        response = self._api_call("ModifyCidrAttribute", request)
        model = models.ModifyCidrAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteCidr(self, request):
        """
        删除IPv4 CIDR地址段。
        """
        response = self._api_call("DeleteCidr", request)
        model = models.DeleteCidrResponse()
        model._deserialize(response)
        return model

    def DeleteCidrs(self, request):
        """
        删除一个或多个IPv4 CIDR地址块。
        """
        response = self._api_call("DeleteCidrs", request)
        model = models.DeleteCidrsResponse()
        model._deserialize(response)
        return model

    def RenewIpv6Cidr(self, request):
        """
        将一个处于回收站的IPv6 CIDR地址段恢复回正常。
        """
        response = self._api_call("RenewIpv6Cidr", request)
        model = models.RenewIpv6CidrResponse()
        model._deserialize(response)
        return model

    def DescribeIpv6Cidrs(self, request):
        """
        查询IPV6 CIDR地址块列表。
        """
        response = self._api_call("DescribeIpv6Cidrs", request)
        model = models.DescribeIpv6CidrsResponse()
        model._deserialize(response)
        return model

    def DeleteIpv6Cidr(self, request):
        """
        删除IPv6 CIDR地址块。
        """
        response = self._api_call("DeleteIpv6Cidr", request)
        model = models.DeleteIpv6CidrResponse()
        model._deserialize(response)
        return model

    def RenewCidr(self, request):
        """
        将一个处于回收站的IPv4 CIDR地址段恢复回正常。
        """
        response = self._api_call("RenewCidr", request)
        model = models.RenewCidrResponse()
        model._deserialize(response)
        return model

    def CreateByoip(self, request):
        """
        提交自带 IP 段（BYOIP）创建 CIDR。返回 RPKI/IRR 校验失败列表。
        """
        response = self._api_call("CreateByoip", request)
        model = models.CreateByoipResponse()
        model._deserialize(response)
        return model

    def DescribeByoipRegions(self, request):
        """
        返回支持售卖 BYOIP 的区域及对应网段、网络类型等信息。
        """
        response = self._api_call("DescribeByoipRegions", request)
        model = models.DescribeByoipRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeByoipPrice(self, request):
        """
        根据宣告 IP 段、区域、线路类型等查询 BYOIP 价格。
        """
        response = self._api_call("DescribeByoipPrice", request)
        model = models.DescribeByoipPriceResponse()
        model._deserialize(response)
        return model

    def DescribeEipRegions(self, request):
        """
        查询支持售卖EIP的区域信息。
        """
        response = self._api_call("DescribeEipRegions", request)
        model = models.DescribeEipRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeEipInternetChargeTypes(self, request):
        """
        查询EIP支持的网络计费模式。
        """
        response = self._api_call("DescribeEipInternetChargeTypes", request)
        model = models.DescribeEipInternetChargeTypesResponse()
        model._deserialize(response)
        return model

    def DescribeEipRemoteRegions(self, request):
        """
        查询EIP支持的远程指向的节点信息。
        """
        response = self._api_call("DescribeEipRemoteRegions", request)
        model = models.DescribeEipRemoteRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeEipPrice(self, request):
        """
        创建公网弹性IP询价。
        """
        response = self._api_call("DescribeEipPrice", request)
        model = models.DescribeEipPriceResponse()
        model._deserialize(response)
        return model

    def DescribeEips(self, request):
        """
        指定条件查询已创建的弹性IPv4的信息。用户可以根据ID、名称等信息来搜索。
        """
        response = self._api_call("DescribeEips", request)
        model = models.DescribeEipsResponse()
        model._deserialize(response)
        return model

    def CreateEips(self, request):
        """
        创建弹性公网IP。
        """
        response = self._api_call("CreateEips", request)
        model = models.CreateEipsResponse()
        model._deserialize(response)
        return model

    def ModifyEipAttribute(self, request):
        """
        修改弹性公网IP属性。
        """
        response = self._api_call("ModifyEipAttribute", request)
        model = models.ModifyEipAttributeResponse()
        model._deserialize(response)
        return model

    def AvailableLanIp(self, request):
        """
        查询可供弹性公网IP绑定的网卡及内网IP信息。
        """
        response = self._api_call("AvailableLanIp", request)
        model = models.AvailableLanIpResponse()
        model._deserialize(response)
        return model

    def AssociateEipAddress(self, request):
        """
        批量将弹性公网IP（EIP）绑定到同地域的云产品实例上。
        """
        response = self._api_call("AssociateEipAddress", request)
        model = models.AssociateEipAddressResponse()
        model._deserialize(response)
        return model

    def UnassociateEipAddress(self, request):
        """
        将弹性公网IP（EIP）从绑定的云产品上解绑。
        """
        response = self._api_call("UnassociateEipAddress", request)
        model = models.UnassociateEipAddressResponse()
        model._deserialize(response)
        return model

    def ReplaceEipAddress(self, request):
        """
        替换一个或者多个弹性公网IP地址。
        """
        response = self._api_call("ReplaceEipAddress", request)
        model = models.ReplaceEipAddressResponse()
        model._deserialize(response)
        return model

    def ChangeEipInternetChargeType(self, request):
        """
        变更弹性公网IP更网络计费模式。
        """
        response = self._api_call("ChangeEipInternetChargeType", request)
        model = models.ChangeEipInternetChargeTypeResponse()
        model._deserialize(response)
        return model

    def ModifyEipBandwidth(self, request):
        """
        调整弹性公网IP的带宽限速。
        """
        response = self._api_call("ModifyEipBandwidth", request)
        model = models.ModifyEipBandwidthResponse()
        model._deserialize(response)
        return model

    def ChangeEipBindType(self, request):
        """
        弹性公网IP（EIP）更换绑定模式。
        """
        response = self._api_call("ChangeEipBindType", request)
        model = models.ChangeEipBindTypeResponse()
        model._deserialize(response)
        return model

    def ConfigEipProbe(self, request):
        """
        弹性公网IP（EIP）探测配置。
        """
        response = self._api_call("ConfigEipProbe", request)
        model = models.ConfigEipProbeResponse()
        model._deserialize(response)
        return model

    def ConfigEipEgressIp(self, request):
        """
        指定IP作为出口IP。
        """
        response = self._api_call("ConfigEipEgressIp", request)
        model = models.ConfigEipEgressIpResponse()
        model._deserialize(response)
        return model

    def DeleteEip(self, request):
        """
        删除指定的弹性公网IP。
        """
        response = self._api_call("DeleteEip", request)
        model = models.DeleteEipResponse()
        model._deserialize(response)
        return model

    def RenewEip(self, request):
        """
        恢复弹性公网IP
        """
        response = self._api_call("RenewEip", request)
        model = models.RenewEipResponse()
        model._deserialize(response)
        return model

    def DescribeEipTraffic(self, request):
        """
        查询弹性公网IP指定时间段内的流量信息。
        """
        response = self._api_call("DescribeEipTraffic", request)
        model = models.DescribeEipTrafficResponse()
        model._deserialize(response)
        return model

    def DescribeEipMonitorData(self, request):
        """
        查询一段时间的弹性公网IP监控指标数据。
        """
        response = self._api_call("DescribeEipMonitorData", request)
        model = models.DescribeEipMonitorDataResponse()
        model._deserialize(response)
        return model

    def DescribeRoutes(self, request):
        """
        查询路由列表。用户可以根据ID、名称等信息来搜索Route信息。路由列表包括系统生成的以及用户创建的路由。
        """
        response = self._api_call("DescribeRoutes", request)
        model = models.DescribeRoutesResponse()
        model._deserialize(response)
        return model

    def CreateRoute(self, request):
        """
        创建一个自定义路由。
        """
        response = self._api_call("CreateRoute", request)
        model = models.CreateRouteResponse()
        model._deserialize(response)
        return model

    def ModifyRouteAttribute(self, request):
        """
        修改路由的基本信息，目前只允许修改路由的名称。
        """
        response = self._api_call("ModifyRouteAttribute", request)
        model = models.ModifyRouteAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteRoute(self, request):
        """
        删除一条自定义路由。
        """
        response = self._api_call("DeleteRoute", request)
        model = models.DeleteRouteResponse()
        model._deserialize(response)
        return model

    def DescribeCrossRegionBandwidthRegions(self, request):
        """
        查询支持售卖内网跨区域带宽的区域信息。
        """
        response = self._api_call("DescribeCrossRegionBandwidthRegions", request)
        model = models.DescribeCrossRegionBandwidthRegionsResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateCrossRegionBandwidth(self, request):
        """
        创建内网跨区域带宽询价。
        """
        response = self._api_call("InquiryPriceCreateCrossRegionBandwidth", request)
        model = models.InquiryPriceCreateCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def CreateCrossRegionBandwidth(self, request):
        """
        创建内网跨区域带宽。
        """
        response = self._api_call("CreateCrossRegionBandwidth", request)
        model = models.CreateCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def DescribeCrossRegionBandwidth(self, request):
        """
        查询内网跨区域带宽列表。
        """
        response = self._api_call("DescribeCrossRegionBandwidth", request)
        model = models.DescribeCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def InquiryPriceModifyCrossRegionBandwidth(self, request):
        """
        调整内网跨区域带宽询价。
        """
        response = self._api_call("InquiryPriceModifyCrossRegionBandwidth", request)
        model = models.InquiryPriceModifyCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def ModifyCrossRegionBandwidthAttribute(self, request):
        """
        修改内网跨区域带宽属性（名称）。
        """
        response = self._api_call("ModifyCrossRegionBandwidthAttribute", request)
        model = models.ModifyCrossRegionBandwidthAttributeResponse()
        model._deserialize(response)
        return model

    def ModifyCrossRegionBandwidth(self, request):
        """
        调整内网跨区域带宽。
        """
        response = self._api_call("ModifyCrossRegionBandwidth", request)
        model = models.ModifyCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def DeleteCrossRegionBandwidth(self, request):
        """
        删除内网跨区域带宽。
        """
        response = self._api_call("DeleteCrossRegionBandwidth", request)
        model = models.DeleteCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def RenewCrossRegionBandwidth(self, request):
        """
        恢复内网跨区域带宽。
        """
        response = self._api_call("RenewCrossRegionBandwidth", request)
        model = models.RenewCrossRegionBandwidthResponse()
        model._deserialize(response)
        return model

    def DescribeCrossRegionBandwidthMonitorData(self, request):
        """
        查询内网跨区域带宽监控指标数据。
        """
        response = self._api_call("DescribeCrossRegionBandwidthMonitorData", request)
        model = models.DescribeCrossRegionBandwidthMonitorDataResponse()
        model._deserialize(response)
        return model

    def DescribeDhcpOptionsSets(self, request):
        """
        查询已创建的DHCP选项集列表。
        """
        response = self._api_call("DescribeDhcpOptionsSets", request)
        model = models.DescribeDhcpOptionsSetsResponse()
        model._deserialize(response)
        return model

    def CreateDhcpOptionsSet(self, request):
        """
        创建DHCP选项集。
        """
        response = self._api_call("CreateDhcpOptionsSet", request)
        model = models.CreateDhcpOptionsSetResponse()
        model._deserialize(response)
        return model

    def ModifyDhcpOptionsSetAttributes(self, request):
        """
        修改DHCP选项集配置信息。
        """
        response = self._api_call("ModifyDhcpOptionsSetAttributes", request)
        model = models.ModifyDhcpOptionsSetAttributesResponse()
        model._deserialize(response)
        return model

    def AttachDhcpOptionsSetToSubnet(self, request):
        """
        将DHCP选项集关联到Subnet。
        """
        response = self._api_call("AttachDhcpOptionsSetToSubnet", request)
        model = models.AttachDhcpOptionsSetToSubnetResponse()
        model._deserialize(response)
        return model

    def DetachDhcpOptionsSetFromSubnet(self, request):
        """
        将DHCP选项集与Subnet取消关联。
        """
        response = self._api_call("DetachDhcpOptionsSetFromSubnet", request)
        model = models.DetachDhcpOptionsSetFromSubnetResponse()
        model._deserialize(response)
        return model

    def DeleteDhcpOptionsSet(self, request):
        """
        删除DHCP选项集。
        """
        response = self._api_call("DeleteDhcpOptionsSet", request)
        model = models.DeleteDhcpOptionsSetResponse()
        model._deserialize(response)
        return model

    def CreateBorderGateway(self, request):
        """
        在某节点为VPC创建一个边界网关。
        """
        response = self._api_call("CreateBorderGateway", request)
        model = models.CreateBorderGatewayResponse()
        model._deserialize(response)
        return model

    def DescribeBorderGateways(self, request):
        """
        查询边界网关列表。
        """
        response = self._api_call("DescribeBorderGateways", request)
        model = models.DescribeBorderGatewaysResponse()
        model._deserialize(response)
        return model

    def ModifyBorderGatewayAsn(self, request):
        """
        修改边界网关的ASN。
        """
        response = self._api_call("ModifyBorderGatewayAsn", request)
        model = models.ModifyBorderGatewayAsnResponse()
        model._deserialize(response)
        return model

    def ModifyBorderGatewaysAttribute(self, request):
        """
        修改边界网关的属性，包括名称，路由级别，子网宣告控制等。
        """
        response = self._api_call("ModifyBorderGatewaysAttribute", request)
        model = models.ModifyBorderGatewaysAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeAvailableNats(self, request):
        """
        获取可绑定边界网关的NAT网关列表。
        """
        response = self._api_call("DescribeAvailableNats", request)
        model = models.DescribeAvailableNatsResponse()
        model._deserialize(response)
        return model

    def AssignBorderGateway(self, request):
        """
        边界网关绑定NAT网关。
        """
        response = self._api_call("AssignBorderGateway", request)
        model = models.AssignBorderGatewayResponse()
        model._deserialize(response)
        return model

    def UnassignBorderGateway(self, request):
        """
        解绑边界网关
        """
        response = self._api_call("UnassignBorderGateway", request)
        model = models.UnassignBorderGatewayResponse()
        model._deserialize(response)
        return model

    def AssignBorderGatewayRoute(self, request):
        """
        边界网关绑定自定义路由。即自定义路由发布到zbg网关。
        """
        response = self._api_call("AssignBorderGatewayRoute", request)
        model = models.AssignBorderGatewayRouteResponse()
        model._deserialize(response)
        return model

    def UnassignBorderGatewayRoute(self, request):
        """
        边界网关路由宣告中移除指定的自定义路由。
        """
        response = self._api_call("UnassignBorderGatewayRoute", request)
        model = models.UnassignBorderGatewayRouteResponse()
        model._deserialize(response)
        return model

    def DeleteBorderGateway(self, request):
        """
        删除一个指定的边界网关。
        """
        response = self._api_call("DeleteBorderGateway", request)
        model = models.DeleteBorderGatewayResponse()
        model._deserialize(response)
        return model

    def DescribeVpcs(self, request):
        """
        查询私有网络（VPC）列表，用户可以根据 VPC ID、VPC 名称等信息来筛选过滤VPC信息。
        """
        response = self._api_call("DescribeVpcs", request)
        model = models.DescribeVpcsResponse()
        model._deserialize(response)
        return model

    def CreateVpc(self, request):
        """
        创建全球VPC。
        """
        response = self._api_call("CreateVpc", request)
        model = models.CreateVpcResponse()
        model._deserialize(response)
        return model

    def ModifyVpcAttribute(self, request):
        """
        修改私有网络（VPC）的相关属性。
        """
        response = self._api_call("ModifyVpcAttribute", request)
        model = models.ModifyVpcAttributeResponse()
        model._deserialize(response)
        return model

    def ModifyVpcsAttribute(self, request):
        """
        修改一个或多个VPC的属性。该接口只支持修改VPC的名称。
        """
        response = self._api_call("ModifyVpcsAttribute", request)
        model = models.ModifyVpcsAttributeResponse()
        model._deserialize(response)
        return model

    def DeleteVpc(self, request):
        """
        删除VPC
        """
        response = self._api_call("DeleteVpc", request)
        model = models.DeleteVpcResponse()
        model._deserialize(response)
        return model

    def DescribeSubnetRegions(self, request):
        """
        查询支持创建子网区域以及是否IPv6。
        """
        response = self._api_call("DescribeSubnetRegions", request)
        model = models.DescribeSubnetRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeSubnets(self, request):
        """
        查询子网列表信息。可以根据子网ID, 名称等信息筛选查询子网。
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

    def ModifySubnetAttribute(self, request):
        """
        修改子网属性。包括名称，CIDR等。
        """
        response = self._api_call("ModifySubnetAttribute", request)
        model = models.ModifySubnetAttributeResponse()
        model._deserialize(response)
        return model

    def ModifySubnetsAttribute(self, request):
        """
        批量修改子网的属性。
        """
        response = self._api_call("ModifySubnetsAttribute", request)
        model = models.ModifySubnetsAttributeResponse()
        model._deserialize(response)
        return model

    def ModifySubnetStackType(self, request):
        """
        修改子网堆栈类型
        """
        response = self._api_call("ModifySubnetStackType", request)
        model = models.ModifySubnetStackTypeResponse()
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

    def DescribeNatGatewayRegions(self, request):
        """
        支持售卖NAT网关的区域信息。
        """
        response = self._api_call("DescribeNatGatewayRegions", request)
        model = models.DescribeNatGatewayRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeAvailableBorderGateway(self, request):
        """
        获取可绑定NAT的边界网关。
        """
        response = self._api_call("DescribeAvailableBorderGateway", request)
        model = models.DescribeAvailableBorderGatewayResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateNatGateway(self, request):
        """
        查询创建NAT网关的价格。
        """
        response = self._api_call("InquiryPriceCreateNatGateway", request)
        model = models.InquiryPriceCreateNatGatewayResponse()
        model._deserialize(response)
        return model

    def CreateNatGateway(self, request):
        """
        创建NAT网关。
        """
        response = self._api_call("CreateNatGateway", request)
        model = models.CreateNatGatewayResponse()
        model._deserialize(response)
        return model

    def DescribeNatGateways(self, request):
        """
        查询NAT网关列表。
        """
        response = self._api_call("DescribeNatGateways", request)
        model = models.DescribeNatGatewaysResponse()
        model._deserialize(response)
        return model

    def DescribeNatGatewayDetail(self, request):
        """
        查询NAT网关详情规则表。
        """
        response = self._api_call("DescribeNatGatewayDetail", request)
        model = models.DescribeNatGatewayDetailResponse()
        model._deserialize(response)
        return model

    def ModifyNatGatewayAttribute(self, request):
        """
        修改NAT网关的属性。
        """
        response = self._api_call("ModifyNatGatewayAttribute", request)
        model = models.ModifyNatGatewayAttributeResponse()
        model._deserialize(response)
        return model

    def RenewNatGateway(self, request):
        """
        续费一个指定的NAT网关。
        """
        response = self._api_call("RenewNatGateway", request)
        model = models.RenewNatGatewayResponse()
        model._deserialize(response)
        return model

    def DeleteNatGateway(self, request):
        """
        删除一个指定的NAT网关。
        """
        response = self._api_call("DeleteNatGateway", request)
        model = models.DeleteNatGatewayResponse()
        model._deserialize(response)
        return model

    def CreateSnatEntry(self, request):
        """
        创建SNAT规则。
        """
        response = self._api_call("CreateSnatEntry", request)
        model = models.CreateSnatEntryResponse()
        model._deserialize(response)
        return model

    def ModifySnatEntry(self, request):
        """
        修改SNAT规则。
        """
        response = self._api_call("ModifySnatEntry", request)
        model = models.ModifySnatEntryResponse()
        model._deserialize(response)
        return model

    def DeleteSnatEntry(self, request):
        """
        删除SNAT规则。
        """
        response = self._api_call("DeleteSnatEntry", request)
        model = models.DeleteSnatEntryResponse()
        model._deserialize(response)
        return model

    def CreateDnatEntry(self, request):
        """
        创建DNAT规则。
        """
        response = self._api_call("CreateDnatEntry", request)
        model = models.CreateDnatEntryResponse()
        model._deserialize(response)
        return model

    def ModifyDnatEntry(self, request):
        """
        修改DNAT规则。
        """
        response = self._api_call("ModifyDnatEntry", request)
        model = models.ModifyDnatEntryResponse()
        model._deserialize(response)
        return model

    def DeleteDnatEntry(self, request):
        """
        删除DNAT规则。
        """
        response = self._api_call("DeleteDnatEntry", request)
        model = models.DeleteDnatEntryResponse()
        model._deserialize(response)
        return model

    def CreatePolicy(self, request):
        """
        创建防护策略
        """
        response = self._api_call("CreatePolicy", request)
        model = models.CreatePolicyResponse()
        model._deserialize(response)
        return model

    def DescribePolicys(self, request):
        """
        获取防护策略列表
        """
        response = self._api_call("DescribePolicys", request)
        model = models.DescribePolicysResponse()
        model._deserialize(response)
        return model

    def DescribePolicyDetail(self, request):
        """
        获取防护策略详情
        """
        response = self._api_call("DescribePolicyDetail", request)
        model = models.DescribePolicyDetailResponse()
        model._deserialize(response)
        return model

    def ModifyPolicy(self, request):
        """
        修改防护策略
        """
        response = self._api_call("ModifyPolicy", request)
        model = models.ModifyPolicyResponse()
        model._deserialize(response)
        return model

    def AttachToPolicy(self, request):
        """
        防护对象关联防护策略
        """
        response = self._api_call("AttachToPolicy", request)
        model = models.AttachToPolicyResponse()
        model._deserialize(response)
        return model

    def DetachFromPolicy(self, request):
        """
        防护对象取消关联防护策略
        """
        response = self._api_call("DetachFromPolicy", request)
        model = models.DetachFromPolicyResponse()
        model._deserialize(response)
        return model

    def DescribePolicyRegions(self, request):
        """
        获取区域封禁可选区域列表
        """
        response = self._api_call("DescribePolicyRegions", request)
        model = models.DescribePolicyRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeReflectUdpPortOptions(self, request):
        """
        获取默认UDP反射源端口列表
        """
        response = self._api_call("DescribeReflectUdpPortOptions", request)
        model = models.DescribeReflectUdpPortOptionsResponse()
        model._deserialize(response)
        return model

    def DeletePolicy(self, request):
        """
        删除防护策略
        """
        response = self._api_call("DeletePolicy", request)
        model = models.DeletePolicyResponse()
        model._deserialize(response)
        return model

    def DescribeDDosEventDetail(self, request):
        """
        获取攻击事件详情
        """
        response = self._api_call("DescribeDDosEventDetail", request)
        model = models.DescribeDDosEventDetailResponse()
        model._deserialize(response)
        return model

    def DescribeDDosAllEventList(self, request):
        """
        获取攻击事件列表
        """
        response = self._api_call("DescribeDDosAllEventList", request)
        model = models.DescribeDDosAllEventListResponse()
        model._deserialize(response)
        return model

    def DescribeSecurityGroups(self, request):
        """
        查询安全组列表。
        """
        response = self._api_call("DescribeSecurityGroups", request)
        model = models.DescribeSecurityGroupsResponse()
        model._deserialize(response)
        return model

    def CreateSecurityGroup(self, request):
        """
        创建一个安全组。
        """
        response = self._api_call("CreateSecurityGroup", request)
        model = models.CreateSecurityGroupResponse()
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

    def DeleteSecurityGroup(self, request):
        """
        删除一个安全组。
        """
        response = self._api_call("DeleteSecurityGroup", request)
        model = models.DeleteSecurityGroupResponse()
        model._deserialize(response)
        return model

    def DescribeSecurityGroupRule(self, request):
        """
        查询指定安全组内的规则。
        """
        response = self._api_call("DescribeSecurityGroupRule", request)
        model = models.DescribeSecurityGroupRuleResponse()
        model._deserialize(response)
        return model

    def ConfigureSecurityGroupRules(self, request):
        """
        配置安全组规则。
        """
        response = self._api_call("ConfigureSecurityGroupRules", request)
        model = models.ConfigureSecurityGroupRulesResponse()
        model._deserialize(response)
        return model

    def AssignSecurityGroupVpc(self, request):
        """
        VPC更换绑定安全组。
        """
        response = self._api_call("AssignSecurityGroupVpc", request)
        model = models.AssignSecurityGroupVpcResponse()
        model._deserialize(response)
        return model

    def UnAssignSecurityGroupVpc(self, request):
        """
        VPC解绑安全组。
        """
        response = self._api_call("UnAssignSecurityGroupVpc", request)
        model = models.UnAssignSecurityGroupVpcResponse()
        model._deserialize(response)
        return model

