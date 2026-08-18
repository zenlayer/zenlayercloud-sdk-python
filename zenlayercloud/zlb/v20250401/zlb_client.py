#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zlb.v20250401 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZlbClient(AbstractClient):
    _api_version = "2025-04-01"
    _service = "zlb"

    def DescribeLoadBalancerRegions(self, request):
        """
        查询支持购买负载均衡的区域。
        """
        response = self._api_call("DescribeLoadBalancerRegions", request)
        model = models.DescribeLoadBalancerRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeLoadBalancers(self, request):
        """
        查询负载均衡实例列表。
        """
        response = self._api_call("DescribeLoadBalancers", request)
        model = models.DescribeLoadBalancersResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateLoadBalancer(self, request):
        """
        查询创建负载均衡的价格。
        """
        response = self._api_call("InquiryPriceCreateLoadBalancer", request)
        model = models.InquiryPriceCreateLoadBalancerResponse()
        model._deserialize(response)
        return model

    def CreateLoadBalancer(self, request):
        """
        创建负载均衡器实例。
        """
        response = self._api_call("CreateLoadBalancer", request)
        model = models.CreateLoadBalancerResponse()
        model._deserialize(response)
        return model

    def ModifyLoadBalancersAttribute(self, request):
        """
        修改负载均衡实例的属性。目前仅支持修改负载均衡实例的名称。
        """
        response = self._api_call("ModifyLoadBalancersAttribute", request)
        model = models.ModifyLoadBalancersAttributeResponse()
        model._deserialize(response)
        return model

    def AddLoadBalancersPrivateIps(self, request):
        """
        为负载均衡器实例添加内网IP。
        """
        response = self._api_call("AddLoadBalancersPrivateIps", request)
        model = models.AddLoadBalancersPrivateIpsResponse()
        model._deserialize(response)
        return model

    def DeleteLoadBalancersPrivateIps(self, request):
        """
        为负载均衡器实例删除内网IP。
        """
        response = self._api_call("DeleteLoadBalancersPrivateIps", request)
        model = models.DeleteLoadBalancersPrivateIpsResponse()
        model._deserialize(response)
        return model

    def TerminateLoadBalancer(self, request):
        """
        本接口用户删除一个指定的负载均衡器实例。
        """
        response = self._api_call("TerminateLoadBalancer", request)
        model = models.TerminateLoadBalancerResponse()
        model._deserialize(response)
        return model

    def RestoreLoadBalancer(self, request):
        """
        将在回收站的负载均衡实例进行恢复。
        """
        response = self._api_call("RestoreLoadBalancer", request)
        model = models.RestoreLoadBalancerResponse()
        model._deserialize(response)
        return model

    def DescribeLoadBalancerMonitorData(self, request):
        """
        查询负载均衡监控指标数据，包括并发连接数, 新建连接数以及网络带宽等指标数据。
        """
        response = self._api_call("DescribeLoadBalancerMonitorData", request)
        model = models.DescribeLoadBalancerMonitorDataResponse()
        model._deserialize(response)
        return model

    def SetSecurityGroupForLoadBalancers(self, request):
        """
        批量更换负载器均衡的安全组。
        """
        response = self._api_call("SetSecurityGroupForLoadBalancers", request)
        model = models.SetSecurityGroupForLoadBalancersResponse()
        model._deserialize(response)
        return model

    def UnbindSecurityGroupFromLoadBalancers(self, request):
        """
        批量解绑负载器均衡的安全组。
        """
        response = self._api_call("UnbindSecurityGroupFromLoadBalancers", request)
        model = models.UnbindSecurityGroupFromLoadBalancersResponse()
        model._deserialize(response)
        return model

    def DescribeListeners(self, request):
        """
        本接口接口可根据负载均衡器 ID、监听器的协议作为过滤条件获取监听器列表。如果不指定任何过滤条件，则返回指定负载均衡实例下的所有监听器。
        """
        response = self._api_call("DescribeListeners", request)
        model = models.DescribeListenersResponse()
        model._deserialize(response)
        return model

    def CreateListener(self, request):
        """
        查询创建负载均衡监听器。
        """
        response = self._api_call("CreateListener", request)
        model = models.CreateListenerResponse()
        model._deserialize(response)
        return model

    def ModifyListener(self, request):
        """
        修改负载均衡监听器的属性，包括监听器的名称、健康检查参数、转发方式等。不支持修改监听器的监听协议。
        """
        response = self._api_call("ModifyListener", request)
        model = models.ModifyListenerResponse()
        model._deserialize(response)
        return model

    def DeleteListener(self, request):
        """
        查询删除一个负载均衡监听器。
        """
        response = self._api_call("DeleteListener", request)
        model = models.DeleteListenerResponse()
        model._deserialize(response)
        return model

    def DescribeBackends(self, request):
        """
        查询负载均衡实例的绑定的后端服务列表。
        """
        response = self._api_call("DescribeBackends", request)
        model = models.DescribeBackendsResponse()
        model._deserialize(response)
        return model

    def RegisterBackend(self, request):
        """
        将一台或多台后端服务绑定到负载均衡的监听器。
        """
        response = self._api_call("RegisterBackend", request)
        model = models.RegisterBackendResponse()
        model._deserialize(response)
        return model

    def ModifyBackend(self, request):
        """
        修改一台或多台绑定在指定监听器上的后端服务的配置，包括权重和和后端服务器转发端口。
        """
        response = self._api_call("ModifyBackend", request)
        model = models.ModifyBackendResponse()
        model._deserialize(response)
        return model

    def DeregisterBackend(self, request):
        """
        将一台或多台绑定在指定监听器上的后端服务解绑。
        """
        response = self._api_call("DeregisterBackend", request)
        model = models.DeregisterBackendResponse()
        model._deserialize(response)
        return model

    def DescribeBackendHealth(self, request):
        """
        查询负载均衡实例的绑定的后端服务列表。
        """
        response = self._api_call("DescribeBackendHealth", request)
        model = models.DescribeBackendHealthResponse()
        model._deserialize(response)
        return model

