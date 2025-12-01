#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.zlb.v20250401 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZLBClient(AbstractClient):
    _api_version = "2025-04-01"
    _service = "zlb"

    def DescribeListeners(self, request):
        response = self._api_call("DescribeListeners", request)
        model = models.DescribeListenersResponse()
        model._deserialize(response)
        return model

    def CreateListener(self, request):
        response = self._api_call("CreateListener", request)
        model = models.CreateListenerResponse()
        model._deserialize(response)
        return model

    def DeleteListener(self, request):
        response = self._api_call("DeleteListener", request)
        model = models.DeleteListenerResponse()
        model._deserialize(response)
        return model

    def ModifyListener(self, request):
        response = self._api_call("ModifyListener", request)
        model = models.ModifyListenerResponse()
        model._deserialize(response)
        return model

    def DescribeLoadBalancerRegions(self, request):
        response = self._api_call("DescribeLoadBalancerRegions", request)
        model = models.DescribeLoadBalancerRegionsResponse()
        model._deserialize(response)
        return model

    def RegisterBackend(self, request):
        response = self._api_call("RegisterBackend", request)
        model = models.RegisterBackendResponse()
        model._deserialize(response)
        return model

    def DeregisterBackend(self, request):
        response = self._api_call("DeregisterBackend", request)
        model = models.DeregisterBackendResponse()
        model._deserialize(response)
        return model

    def ModifyBackend(self, request):
        response = self._api_call("ModifyBackend", request)
        model = models.ModifyBackendResponse()
        model._deserialize(response)
        return model

    def DescribeBackends(self, request):
        response = self._api_call("DescribeBackends", request)
        model = models.DescribeBackendsResponse()
        model._deserialize(response)
        return model

    def DescribeBackendHealth(self, request):
        response = self._api_call("DescribeBackendHealth", request)
        model = models.DescribeBackendHealthResponse()
        model._deserialize(response)
        return model

    def ModifyLoadBalancersAttribute(self, request):
        response = self._api_call("ModifyLoadBalancersAttribute", request)
        model = models.ModifyLoadBalancersAttributeResponse()
        model._deserialize(response)
        return model

    def DescribeLoadBalancers(self, request):
        response = self._api_call("DescribeLoadBalancers", request)
        model = models.DescribeLoadBalancersResponse()
        model._deserialize(response)
        return model

    def RestoreLoadBalancer(self, request):
        response = self._api_call("RestoreLoadBalancer", request)
        model = models.RestoreLoadBalancerResponse()
        model._deserialize(response)
        return model

    def TerminateLoadBalancer(self, request):
        response = self._api_call("TerminateLoadBalancer", request)
        model = models.TerminateLoadBalancerResponse()
        model._deserialize(response)
        return model

    def CreateLoadBalancer(self, request):
        response = self._api_call("CreateLoadBalancer", request)
        model = models.CreateLoadBalancerResponse()
        model._deserialize(response)
        return model

    def InquiryPriceCreateLoadBalancer(self, request):
        response = self._api_call("InquiryPriceCreateLoadBalancer", request)
        model = models.InquiryPriceCreateLoadBalancerResponse()
        model._deserialize(response)
        return model

    def DescribeLoadBalancerMonitorData(self, request):
        response = self._api_call("DescribeLoadBalancerMonitorData", request)
        model = models.DescribeLoadBalancerMonitorDataResponse()
        model._deserialize(response)
        return model

    def SetSecurityGroupForLoadBalancers(self, request):
        response = self._api_call("SetSecurityGroupForLoadBalancers", request)
        model = models.SetSecurityGroupForLoadBalancersResponse()
        model._deserialize(response)
        return model

    def AddLoadBalancersPrivateIps(self, request):
        response = self._api_call("AddLoadBalancersPrivateIps", request)
        model = models.AddLoadBalancersPrivateIpsResponse()
        model._deserialize(response)
        return model

    def DeleteLoadBalancersPrivateIps(self, request):
        response = self._api_call("DeleteLoadBalancersPrivateIps", request)
        model = models.DeleteLoadBalancersPrivateIpsResponse()
        model._deserialize(response)
        return model

