#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.abstract_model import AbstractModel


class CreateInstancesRequest(AbstractModel):
    """CreateInstances请求参数结构体
    """

    def __init__(self):
        self.zoneId = None
        self.instanceChargeType = None
        self.instanceChargePrepaid = None
        self.instanceTypeId = None
        self.imageId = None
        self.resourceGroupId = None
        self.instanceName = None
        self.hostname = None
        self.amount = None
        self.password = None
        self.sshKeys = None
        self.internetChargeType = None
        self.internetMaxBandwidthOut = None
        self.trafficPackageSize = None
        self.subnetId = None
        self.raidConfig = None
        self.partitions = None
        self.nic = None

    def _deserialize(self, params):
        self.zoneId = params.get("zoneId")
        self.instanceChargeType = params.get("instanceChargeType")
        if params.get("instanceChargePrepaid") is not None:
            self.instanceChargePrepaid = InstanceChargePrepaid(params.get("instanceChargePrepaid"))
        self.instanceTypeId = params.get("instanceTypeId")
        self.imageId = params.get("imageId")
        self.resourceGroupId = params.get("imageId")
        self.instanceName = params.get("instanceName")
        self.hostname = params.get("hostname")
        self.amount = params.get("amount")
        self.password = params.get("password")
        self.sshKeys = params.get("sshKeys")
        self.internetChargeType = params.get("internetChargeType")
        self.internetMaxBandwidthOut = params.get("internetMaxBandwidthOut")
        self.trafficPackageSize = params.get("trafficPackageSize")
        self.subnetId = params.get("subnetId")
        if params.get("raidConfig") is not None:
            self.raidConfig = RaidConfig(params.get("raidConfig"))
        if params.get("partitions") is not None:
            self.partitions = []
            for item in params.get("partitions"):
                obj = CustomRaid(item)
                self.partitions.append(obj)

        if params.get("nic") is not None:
            self.nic = Nic(params.get("nic"))


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回参数结构体
    """

    def __init__(self):
        self.InstanceIdSet = None
        self.RequestId = None

    def _deserialize(self, params):
        self.instanceIdSet = params.get("instanceIdSet")
        self.requestId = params.get("requestId")


class InstanceChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self, params={}):
        """
        :param period: 购买实例的时长，单位：月。
        :type period: int
        """
        if len(params) > 0:
            self._deserialize(params)
            return
        self.period = None

    def _deserialize(self, params):
        self.period = params.get("period")


class RaidConfig(AbstractModel):
    """描述了Raid的配置信息

    """

    def __init__(self, params={}):
        r"""
        :param raidType: Raid类型。
该配置进行快捷raid配置，支持0, 1, 5, 10。
raidType和customRaids只能指定其中一个参数。
        :type raidType: int
        :param customRaids: 自定义Raid配置。
自定义磁盘进行raid的配置。
raidType和customRaids只能指定其中一个参数。
        :type customRaids: list of CustomRaid
        """
        if len(params) > 0:
            self._deserialize(params)
            return
        self.raidType = None
        self.customRaids = None

    def _deserialize(self, params):
        self.raidType = params.get("raidType")
        if params.get("customRaids") is not None:
            self.customRaids = []
            for item in params.get("customRaids"):
                obj = CustomRaid(item)
                self.customRaids.append(obj)


class CustomRaid(AbstractModel):
    """进行自定义Raid配置时需要的raid级别和指定的磁盘序号。


    """

    def __init__(self, params={}):
        r"""
         :param raidType: Raid类型。
 支持0, 1, 5, 10。
         :type raidType: int
         :param diskSequence: 磁盘序号。
 根据机型里的磁盘从1开始顺序编号。如果是多个磁盘序号，则必须连续。
         :type diskSequence: list of int
         """
        if len(params) > 0:
            self._deserialize(params)
            return
        self.raidType = None
        self.diskSequence = None


def _deserialize(self, params):
    self.raidType = params.get("raidType")
    self.diskSequence = params.get("diskSequence")


class Partition(AbstractModel):
    """分区配置信息。包括文件类型, 分区大小等。


    """

    def __init__(self, params={}):
        r"""

        :param fsType: 分区的文件类型。
linux系统：支持的值ext2,ext3, ext4, ext类型必须要有。
windows系统: 只能为NTFS。
        :type fsType: int
        :param fsPath: 分区盘符。
linux系统：必须为/开头，且第一个为系统分区必须为/。
windows系统：支持C~H，第一个系统分区必须指定为C。
        :type fsPath: str
        :param size: 分区大小。
单位为GB。
        :type size: str
        """
        if len(params) > 0:
            self._deserialize(params)
            return
        self.fsType = None
        self.fsPath = None
        self.size = None

    def _deserialize(self, params):
        self.fsType = params.get("fsType")
        self.fsPath = params.get("fsPath")
        self.size = params.get("size")


class Nic(AbstractModel):
    """分区配置信息。包括文件类型, 分区大小等。


    """

    def __init__(self, params={}):
        r"""

        :param wanName: 公网网卡名称。
只能是数字和大小写字母，且必须以字母开头，长度限制为4-10。
非高可用机型，默认的公网网卡名称为wan0。且不能为lan开头。
高可用机型，默认的公网网卡名称为bond0。
公网名称和内网名称不能相同。
        :type wanName: str
        :param lanName: 内网网卡名称。
只能是数字和大小写字母，且必须以字母开头，长度限制为4-10。
非高可用机型，默认的内网网卡名称为lan0。且不能为wan开头。
高可用机型，默认的内网网卡名称为bond1。
公网名称和内网名称不能相同。
        :type lanName: str
        """
        if len(params) > 0:
            self._deserialize(params)
            return
        self.wanName = None
        self.lanName = None

    def _deserialize(self, params):
        self.wanName = params.get("wanName")
        self.lanName = params.get("lanName")
