#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.maintenance.v20250310 import models
from zenlayercloud.common.abstract_client import AbstractClient


class AlarmClient(AbstractClient):
    _api_version = "2025-03-10"
    _service = "maintenance"

    def DescribeMaintenanceAlerts(self, request):
        response = self._api_call("DescribeMaintenanceAlerts", request)

        model = models.DescribeMaintenanceAlertsResponse()
        model._deserialize(response)
        return model

