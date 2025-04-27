#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.zbc.v20240809 import models
from zenlayercloud.common.abstract_client import AbstractClient


class ZbcClient(AbstractClient):
    _api_version = "2024-08-09"
    _service = "zbc"

    def DescribeMonthlyBillSummary(self, request):
        response = self._api_call("DescribeMonthlyBillSummary", request)

        model = models.DescribeMonthlyBillSummaryResponse()
        model._deserialize(response)
        return model


    def DescribeBillDetail(self, request):
        response = self._api_call("DescribeBillDetail", request)

        model = models.DescribeBillDetailResponse()
        model._deserialize(response)
        return model

    def DescribeCustomerBalance(self, request):
        response = self._api_call("DescribeCustomerBalance", request)

        model = models.DescribeCustomerBalanceResponse()
        model._deserialize(response)
        return model

    def DescribeRechargeRefundHistory(self, request):
        response = self._api_call("DescribeRechargeRefundHistory", request)

        model = models.DescribeRechargeRefundHistoryResponse()
        model._deserialize(response)
        return model

    def DescribeTransactionHistory(self, request):
        response = self._api_call("DescribeTransactionHistory", request)

        model = models.DescribeTransactionHistoryResponse()
        model._deserialize(response)
        return model

