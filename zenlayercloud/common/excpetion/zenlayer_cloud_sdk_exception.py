#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
import sys


class ZenlayerCloudSdkException(Exception):
    """Exception class for Zenlayer Cloud Sdk"""

    def __init__(self, code: str = None, message: str = None, request_id: str = None) -> None:
        """

        :rtype: object
        """
        self.code = code
        self.message = message
        self.request_id = request_id

    def __str__(self):
        s = "[ZenlayerCloudSdkError] Code=%s Message=%s requestId:%s" % (
            self.code, self.message, self.request_id)
        if sys.version_info[0] < 3 and isinstance(s, unicode):
            return s.encode("utf8")
        else:
            return s

    def get_code(self):
        return self.code

    def get_message(self):
        return self.message

    def get_request_id(self):
        return self.request_id
