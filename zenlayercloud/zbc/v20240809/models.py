#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel

class DescribeMonthlyBillSummaryRequest(AbstractModel):
    def __init__(self):
        self.summaryType = None
        self.billMonthly = None

    def _deserialize(self, params):
        self.summaryType = params.get("summaryType")
        self.billMonthly = params.get("billMonthly")


class DescribeMonthlyBillSummaryResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.billMonthly = None
        self.totalSpend = None
        self.totalCash = None
        self.totalRefund = None
        self.totalVoucher = None
        self.summaryInfoList = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.billMonthly = params.get("billMonthly")
        self.totalSpend = params.get("totalSpend")
        self.totalCash = params.get("totalCash")
        self.totalRefund = params.get("totalRefund")
        self.totalVoucher = params.get("totalVoucher")
        if params.get("summaryInfoList") is not None:
            self.summaryInfoList = []
            for item in params.get("summaryInfoList"):
                obj = MonthlyBillSummary(item)
                self.summaryInfoList.append(obj)


class MonthlyBillSummary(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.product = None
        self.resourceGroupName = None
        self.spend = None
        self.voucher = None
        self.cash = None
        self.resourceGroupId = None
        self.refund = None

    def _deserialize(self, params):
        self.product = params.get("product")
        self.resourceGroupName = params.get("resourceGroupName")
        self.spend = params.get("spend")
        self.voucher = params.get("voucher")
        self.cash = params.get("cash")
        self.resourceGroupId = params.get("resourceGroupId")
        self.refund = params.get("refund")


class DescribeBillDetailRequest(AbstractModel):
    def __init__(self):
        self.pageNum = None
        self.pageSize = None
        self.billMonthly = None
        self.orderSn = None
        self.resourceId = None

    def _deserialize(self, params):
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.billMonthly = params.get("billMonthly")
        self.orderSn = params.get("orderSn")
        self.resourceId = params.get("resourceId")


class DescribeBillDetailResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.totalVoucher = None
        self.totalSpend = None
        self.totalCash = None
        self.totalRefund = None
        self.totalCount = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalVoucher = params.get("totalVoucher")
        self.totalSpend = params.get("totalSpend")
        self.totalCash = params.get("totalCash")
        self.totalRefund = params.get("totalRefund")
        self.totalCount = params.get("totalCount")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = BillingDetailInfo(item)
                self.dataSet.append(obj)


class BillingDetailInfo(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.resourceId = None
        self.productSubitem = None
        self.product = None
        self.amount = None
        self.voucher = None
        self.cash = None
        self.billingMode = None
        self.orderSn = None
        self.deductionTime = None
        self.label = None
        self.location = None
        self.billMonthly = None
        self.resourceGroupId = None
        self.resourceGroupName = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.resourceId = params.get("resourceId")
        self.productSubitem = params.get("productSubitem")
        self.product = params.get("product")
        self.amount = params.get("amount")
        self.voucher = params.get("voucher")
        self.cash = params.get("cash")
        self.billingMode = params.get("billingMode")
        self.orderSn = params.get("orderSn")
        self.deductionTime = params.get("deductionTime")
        self.label = params.get("label")
        self.location = params.get("location")
        self.billMonthly = params.get("billMonthly")
        self.resourceGroupId = params.get("resourceGroupId")
        self.resourceGroupName = params.get("resourceGroupName")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")



class DescribeCustomerBalanceRequest(AbstractModel):
    pass

class DescribeCustomerBalanceResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.accountUid = None
        self.cashBalance = None
        self.creditValue = None
        self.purchasingPower = None
        self.orderFrozenAmount = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.accountUid = params.get("accountUid")
        self.cashBalance = params.get("cashBalance")
        self.creditValue = params.get("creditValue")
        self.purchasingPower = params.get("purchasingPower")
        self.orderFrozenAmount = params.get("orderFrozenAmount")


class DescribeRechargeRefundHistoryRequest(AbstractModel):
    def __init__(self):
        self.pageNum = None
        self.pageSize = None
        self.state = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.state = params.get("state")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeRechargeRefundHistoryResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.totalCount = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.totalCount = params.get("totalCount")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = RechargeRefundHistory(item)
                self.dataSet.append(obj)


class RechargeRefundHistory(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.transactionType = None
        self.amount = None
        self.paymentMethod = None
        self.transactionId = None
        self.state = None
        self.transactionTime = None
        self.accountUid = None

    def _deserialize(self, params):
        self.transactionType = params.get("transactionType")
        self.amount = params.get("amount")
        self.paymentMethod = params.get("paymentMethod")
        self.transactionId = params.get("transactionId")
        self.state = params.get("state")
        self.transactionTime = params.get("transactionTime")
        self.accountUid = params.get("accountUid")



class DescribeTransactionHistoryRequest(AbstractModel):
    def __init__(self):
        self.pageNum = None
        self.pageSize = None
        self.transactionType = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.pageNum = params.get("pageNum")
        self.pageSize = params.get("pageSize")
        self.transactionType = params.get("transactionType")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeTransactionHistoryResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.incomeSum = None
        self.expenditureSum = None
        self.totalCount = None
        self.dataSet = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.incomeSum = params.get("incomeSum")
        self.expenditureSum = params.get("expenditureSum")
        self.totalCount = params.get("totalCount")
        if params.get("dataSet") is not None:
            self.dataSet = []
            for item in params.get("dataSet"):
                obj = TransactionHistory(item)
                self.dataSet.append(obj)


class TransactionHistory(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.accountUid = None
        self.uid = None
        self.transactionTime = None
        self.orderSn = None
        self.description = None
        self.transactionType = None
        self.paymentMethod = None
        self.amount = None
        self.cashBalance = None
        self.tradeType = None
        self.tradeNo = None

    def _deserialize(self, params):
        self.accountUid = params.get("accountUid")
        self.uid = params.get("uid")
        self.transactionTime = params.get("transactionTime")
        self.orderSn = params.get("orderSn")
        self.description = params.get("description")
        self.transactionType = params.get("transactionType")
        self.paymentMethod = params.get("paymentMethod")
        self.amount = params.get("amount")
        self.cashBalance = params.get("cashBalance")
        self.tradeType = params.get("tradeType")
        self.tradeNo = params.get("tradeNo")
