#  Zenlayer.com Inc.
#  Copyright (c) 2014-2024 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class DescribeKeyPairsRequest(AbstractModel):
    def __init__(self):
        self.keyIds = None
        self.keyName = None
        self.pageSize = None
        self.pageNum = None

    def _deserialize(self, params):
        self.keyIds = params.get("keyIds")
        self.keyName = params.get("keyName")
        self.pageSize = params.get("pageSize")
        self.pageNum = params.get("pageNum")


class DescribeKeyPairsResponse(AbstractModel):
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
                obj = KeyPair(item)
                self.dataSet.append(obj)


class KeyPair(AbstractModel):
    def __init__(self, params=None):
        if params is None:
            params = {}
        if len(params) > 0:
            self._deserialize(params)
            return
        self.keyId = None
        self.keyName = None
        self.publicKey = None
        self.keyDescription = None
        self.createTime = None

    def _deserialize(self, params):
        self.keyId = params.get("keyId")
        self.keyName = params.get("keyName")
        self.publicKey = params.get("publicKey")
        self.keyDescription = params.get("keyDescription")
        self.createTime = params.get("createTime")


class ImportKeyPairRequest(AbstractModel):
    def __init__(self):
        self.keyName = None
        self.keyDescription = None
        self.publicKey = None

    def _deserialize(self, params):
        self.keyName = params.get("keyName")
        self.keyDescription = params.get("keyDescription")
        self.publicKey = params.get("publicKey")


class ImportKeyPairResponse(AbstractModel):
    def __init__(self):
        self.requestId = None
        self.keyId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")
        self.keyId = params.get("keyId")


class ModifyKeyPairAttributeRequest(AbstractModel):
    def __init__(self):
        self.keyId = None
        self.keyDescription = None

    def _deserialize(self, params):
        self.keyId = params.get("keyId")
        self.keyDescription = params.get("keyDescription")


class ModifyKeyPairAttributeResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


class DeleteKeyPairsRequest(AbstractModel):
    def __init__(self):
        self.keyIds = None

    def _deserialize(self, params):
        self.keyIds = params.get("keyIds")


class DeleteKeyPairsResponse(AbstractModel):
    def __init__(self):
        self.requestId = None

    def _deserialize(self, params):
        self.requestId = params.get("requestId")


