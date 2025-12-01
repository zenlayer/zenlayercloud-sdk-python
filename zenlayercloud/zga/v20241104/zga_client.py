#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_client import AbstractClient
from zenlayercloud.zga.v20241104 import models


class ZgaClient(AbstractClient):
    _api_version = "2024-11-04"
    _service = "zga"

    def DescribeOriginRegions(self):
        response = self._api_call(
            "DescribeOriginRegions", models.DescribeOriginRegionsRequest()
        )

        model = models.DescribeOriginRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeAccelerateRegions(self, request):
        response = self._api_call("DescribeAccelerateRegions", request)

        model = models.DescribeAccelerateRegionsResponse()
        model._deserialize(response)
        return model

    def DescribeCertificates(self, request):
        response = self._api_call("DescribeCertificates", request)

        model = models.DescribeCertificatesResponse()
        model._deserialize(response)
        return model

    def CreateCertificate(self, request):
        response = self._api_call("CreateCertificate", request)

        model = models.CreateCertificateResponse()
        model._deserialize(response)
        return model

    def ModifyCertificate(self, request):
        response = self._api_call("ModifyCertificate", request)

        model = models.ModifyCertificateResponse()
        model._deserialize(response)
        return model

    def DeleteCertificate(self, request):
        response = self._api_call("DeleteCertificate", request)

        model = models.DeleteCertificateResponse()
        model._deserialize(response)
        return model

    def DescribeAccelerators(self, request):
        response = self._api_call("DescribeAccelerators", request)

        model = models.DescribeAcceleratorsResponse()
        model._deserialize(response)
        return model

    def CreateAccelerator(self, request):
        response = self._api_call("CreateAccelerator", request)

        model = models.CreateAcceleratorResponse()
        model._deserialize(response)
        return model

    def DeleteAccelerator(self, request):
        response = self._api_call("DeleteAccelerator", request)

        model = models.DeleteAcceleratorResponse()
        model._deserialize(response)
        return model

    def StartAccelerator(self, request):
        response = self._api_call("StartAccelerator", request)

        model = models.StartAcceleratorResponse()
        model._deserialize(response)
        return model

    def RedeployAccelerator(self, request):
        response = self._api_call("RedeployAccelerator", request)

        model = models.RedeployAcceleratorResponse()
        model._deserialize(response)
        return model

    def PauseAccelerator(self, request):
        response = self._api_call("PauseAccelerator", request)

        model = models.PauseAcceleratorResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorDomain(self, request):
        response = self._api_call("ModifyAcceleratorDomain", request)

        model = models.ModifyAcceleratorDomainResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorName(self, request):
        response = self._api_call("ModifyAcceleratorName", request)

        model = models.ModifyAcceleratorNameResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorOrigin(self, request):
        response = self._api_call("ModifyAcceleratorOrigin", request)

        model = models.ModifyAcceleratorOriginResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorAccRegion(self, request):
        response = self._api_call("ModifyAcceleratorAccRegion", request)

        model = models.ModifyAcceleratorAccRegionResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorRule(self, request):
        response = self._api_call("ModifyAcceleratorRule", request)

        model = models.ModifyAcceleratorRuleResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorProtocolOpts(self, request):
        response = self._api_call("ModifyAcceleratorProtocolOpts", request)

        model = models.ModifyAcceleratorProtocolOptsResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorCertificate(self, request):
        response = self._api_call("ModifyAcceleratorCertificate", request)

        model = models.ModifyAcceleratorCertificateResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorHealthCheck(self, request):
        response = self._api_call("ModifyAcceleratorHealthCheck", request)

        model = models.ModifyAcceleratorHealthCheckResponse()
        model._deserialize(response)
        return model

    def ModifyAcceleratorAccessControl(self, request):
        response = self._api_call("ModifyAcceleratorAccessControl", request)

        model = models.ModifyAcceleratorAccessControlResponse()
        model._deserialize(response)
        return model

    def OpenAcceleratorAccessControl(self, request):
        response = self._api_call("OpenAcceleratorAccessControl", request)

        model = models.OpenAcceleratorAccessControlResponse()
        model._deserialize(response)
        return model

    def CloseAcceleratorAccessControl(self, request):
        response = self._api_call("CloseAcceleratorAccessControl", request)

        model = models.CloseAcceleratorAccessControlResponse()
        model._deserialize(response)
        return model

    def DescribeAcceleratorsAlerts(self, request):
        response = self._api_call("DescribeAcceleratorsAlerts", request)

        model = models.DescribeAcceleratorsAlertsResponse()
        model._deserialize(response)
        return model

    def DescribeAcceleratorLogs(self, request):
        response = self._api_call("DescribeAcceleratorLogs", request)

        model = models.DescribeAcceleratorLogsResponse()
        model._deserialize(response)
        return model

    def DescribeAcceleratorTraffic(self, request):
        response = self._api_call("DescribeAcceleratorTraffic", request)

        model = models.DescribeAcceleratorTrafficResponse()
        model._deserialize(response)
        return model

    def DescribeAcceleratorMetrics(self, request):
        response = self._api_call("DescribeAcceleratorMetrics", request)

        model = models.DescribeAcceleratorMetricsResponse()
        model._deserialize(response)
        return model

    def DescribeResourceGroupsBandwidthLimit(self, request):
        response = self._api_call("DescribeResourceGroupsBandwidthLimit", request)

        model = models.DescribeResourceGroupsBandwidthLimitResponse()
        model._deserialize(response)
        return model

    def ModifyResourceGroupBandwidthLimit(self, request):
        response = self._api_call("ModifyResourceGroupBandwidthLimit", request)

        model = models.ModifyResourceGroupBandwidthLimitResponse()
        model._deserialize(response)
        return model


    def DescribeTraffic(self, request):
        response = self._api_call("DescribeTraffic", request)

        model = models.DescribeTrafficResponse()
        model._deserialize(response)
        return model

    def DescribeStatusCode(self, request):
        response = self._api_call("DescribeStatusCode", request)

        model = models.DescribeStatusCodeResponse()
        model._deserialize(response)
        return model