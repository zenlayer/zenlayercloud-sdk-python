#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
import logging
import os
from urllib.parse import urlparse

import certifi
import requests

logger = logging.getLogger("zenlayercloud_sdk_common")


class ApiProxyClient(object):

    def __init__(self, host, timeout=60, proxy=None, certification=None, is_http=False, debug=False, keep_alive=False):
        self.host = host
        url = urlparse(host)
        if not url.hostname:
            if is_http:
                host = "http://" + host
            else:
                host = "https://" + host
        self.request_host = host
        self.certification = certification
        if certification is None:
            self.certification = certifi.where()
        self.timeout = timeout
        self.proxy = None
        self.debug = debug
        self.keep_alive = keep_alive
        if is_http:
            proxy = proxy or _get_proxy_from_env(host, varname="HTTP_PROXY")
        else:
            proxy = proxy or _get_proxy_from_env(host, varname="HTTPS_PROXY")
        if proxy:
            self.proxy = {"http": proxy, "https": proxy}

    def request(self, req):
        if self.keep_alive:
            req.header["Connection"] = "Keep-Alive"
        if self.debug:
            logger.debug("Send request = %s" % req)

        url = '%s%s' % (self.request_host, req.uri)
        response = requests.request(method=req.method,
                                    url=url,
                                    data=req.data,
                                    headers=req.header,
                                    timeout=self.timeout,
                                    verify=self.certification,
                                    proxies=self.proxy)
        if self.debug:
            logger.debug("Http response = %s" % response)

        return response


def _get_proxy_from_env(host, varname="HTTPS_PROXY"):
    no_proxy = os.environ.get("NO_PROXY") or os.environ.get("no_proxy")
    if no_proxy and host in no_proxy:
        return None
    return os.environ.get(varname.lower()) or os.environ.get(varname.upper())


class BaseRequest(object):

    def __init__(self, host="", uri="", method="", header=None, data=""):
        self.header = {} if header is None else header
        self.method = method
        self.host = host
        self.uri = uri
        self.data = data

    def __str__(self):
        headers = "\n".join("%s: %s" % (k, v) for k, v in self.header.items())
        return ("Host: %s\nMethod: %s\nUri: %s\nHeader: %s\nData: %s\n"
                % (self.host, self.method, self.uri, headers, self.data))

    def get_content_type(self):
        return self.header["Content-Type"]

    def get_host(self):
        return self.header["host"]

    def set_host(self, host):
        self.header["host"] = host

    def set_content_type(self, content_type: str):
        self.header["Content-Type"] = content_type
