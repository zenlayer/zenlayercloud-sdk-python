#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
import logging

from zenlayercloud.bmc.v20221120 import bmc_client, models
from zenlayercloud.bmc.v20221120.models import ChargePrepaid
from zenlayercloud.common.config import Config
from zenlayercloud.common.credential import Credential
from zenlayercloud.common.excpetion.zenlayer_cloud_sdk_exception import ZenlayerCloudSdkException

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(funcName)s:%(message)s', level=logging.DEBUG)

    try:
        credential = Credential("< Your AccessKeyId >", "< Your AccessKeyPassword >")
        config = Config(debug=True)

        client = bmc_client.BmcClient(credential=credential, config=config)

        print(ChargePrepaid({"period": 1}).serialize())
        request = models.DescribeZonesRequest()
        request.acceptLanguage = "zh-CN"
        response = client.DescribeZones(request)

    except ZenlayerCloudSdkException as err:
        print(err)
