#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
from zenlayercloud.common.excpetion.error_code import CREDENTIAL_MISSING_ERROR
from zenlayercloud.common.excpetion.zenlayer_cloud_sdk_exception import ZenlayerCloudSdkException


class Credential(object):

    def __init__(self, access_key_id, access_key_password):
        """Zenlayer Cloud Credential.

        Access https://console.zenlayer.com/accessKey to manage your
        credentials.

        :param access_key_id: The access key id of your credential.
        :type access_key_id: str
        :param access_key_password: The access key password of your credential.
        :type access_key_password: str
        """
        if access_key_id is None or access_key_id.strip() == "":
            raise ZenlayerCloudSdkException(CREDENTIAL_MISSING_ERROR, "access key id should not be none or empty")
        if access_key_password is None or access_key_password.strip() == "":
            raise ZenlayerCloudSdkException(CREDENTIAL_MISSING_ERROR, "access key password should not be none or empty")
        self.access_key_id = access_key_id.strip()
        self.access_key_password = access_key_password.strip()


class TokenCredential(object):

    def __init__(self, token):
        """Zenlayer Cloud Bearer Token Credential.

        Access https://console.zenlayer.com/accessToken to generate a personal access token and use it instead of HMAC-signed credentials.

        :param token: The personal access token.
        :type token: str
        """
        if token is None or token.strip() == "":
            raise ZenlayerCloudSdkException(CREDENTIAL_MISSING_ERROR, "token should not be none or empty")
        self.token = token.strip()
