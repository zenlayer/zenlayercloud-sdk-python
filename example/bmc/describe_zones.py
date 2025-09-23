#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
import logging

from zenlayercloud.zec.v20240401 import zec_client, models
from zenlayercloud.zec.v20240401.models import ChargePrepaid
from zenlayercloud.common.config import Config
from zenlayercloud.common.credential import Credential
from zenlayercloud.common.excpetion.zenlayer_cloud_sdk_exception import ZenlayerCloudSdkException

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(funcName)s:%(message)s', level=logging.DEBUG)

    try:
        credential = Credential("JiMecGdearGYk9U8", "ScytmG960HFPQPJY647mkb9Q6l2uI1")
        config = Config(debug=True)
        config.domain = "portal.hzk8s.com"
        client = zec_client.ZecClient(credential=credential, config=config)

        # print(ChargePrepaid({"period": 1}).serialize())
        request = models.ChangeEipBindTypeRequest()
        request.eipId = "1477325976185746012"
        request.bindType = "FullNat"
        response = client.ChangeEipBindType(request)
        print(response)
    except ZenlayerCloudSdkException as err:
        print(err)
