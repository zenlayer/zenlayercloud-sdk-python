#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeBandwidthClustersRequest(AbstractModel):

    def __init__(self):
        self.bandwidthClusterIds = None
        self.bandwidthClusterName = None
        self.cityName = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.bandwidthClusterIds = params.get("bandwidthClusterIds")
        self.bandwidthClusterName = params.get("bandwidthClusterName")
        self.cityName = params.get("cityName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeBandwidthClustersResponse(AbstractModel):

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
                obj = BandwidthClusterInfo(item)
                self.dataSet.append(obj)


class BandwidthClusterInfo(AbstractModel):

    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.bandwidthClusterId = None
        self.bandwidthClusterName = None
        self.location = None
        self.createTime = None

    def _deserialize(self, params):
        self.bandwidthClusterId = params.get("bandwidthClusterId")
        self.bandwidthClusterName = params.get("bandwidthClusterName")
        self.location = params.get("location")
        self.createTime = params.get("createTime")


class DescribeBandwidthClusterTrafficRequest(AbstractModel):

    def __init__(self):
        self.bandwidthClusterId = None
        self.startTime = None
        self.endTime = None

    def _deserialize(self, params):
        self.bandwidthClusterId = params.get("bandwidthClusterId")
        self.startTime = params.get("startTime")
        self.endTime = params.get("endTime")


class DescribeBandwidthClusterTrafficResponse(AbstractModel):

    def __init__(self):
        self.requestId = None
        self.dataList = None
        self.in95 = None
        self.in95Time = None
        self.inAvg = None
        self.inMax = None
        self.inMin = None
        self.inTotal = None
        self.maxBandwidth95ValueMbps = None
        self.out95 = None
        self.out95Time = None
        self.outAvg = None
        self.outMax = None
        self.outMin = None
        self.outTotal = None
        self.totalUnit = None
        self.unit = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        if params.get("dataList") is not None:
            self.dataList = []
            for item in params.get("dataList"):
                obj = BandwidthClusterTrafficData(item)
                self.dataList.append(obj)
        self.in95 = params.get("in95")
        self.in95Time = params.get("in95Time")
        self.inAvg = params.get("inAvg")
        self.inMax = params.get("inMax")
        self.inMin = params.get("inMin")
        self.inTotal = params.get("inTotal")
        self.maxBandwidth95ValueMbps = params.get("maxBandwidth95ValueMbps")
        self.out95 = params.get("out95")
        self.out95Time = params.get("out95Time")
        self.outAvg = params.get("outAvg")
        self.outMax = params.get("outMax")
        self.outMin = params.get("outMin")
        self.outTotal = params.get("outTotal")
        self.totalUnit = params.get("totalUnit")
        self.unit = params.get("unit")


class BandwidthClusterTrafficData(AbstractModel):

    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.internetRX = None
        self.internetTX = None
        self.time = None

    def _deserialize(self, params):
        self.internetRX = params.get("internetRX")
        self.internetTX = params.get("internetTX")
        self.time = params.get("time")
