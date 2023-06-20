#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
import logging

from zenlayercloud.common.excpetion.zenlayer_cloud_sdk_exception import ZenlayerCloudSdkException
from zenlayercloud.vm.v20230313 import vm_client, models
from zenlayercloud.common.config import Config
from zenlayercloud.common.credential import Credential

if __name__ == '__main__':

    logging.basicConfig(format='%(levelname)s:%(funcName)s:%(message)s', level=logging.DEBUG)

    try:
        credential = Credential("< Your AccessKeyId >", "< Your AccessKeyPassword >")
        config = Config(debug=True)

        client = vm_client.VmClient(credential=credential, config=config)

        request = models.DescribeZonesRequest()
        response = client.DescribeZones(request)
        print(response)
    except ZenlayerCloudSdkException as err:
        print(err)
