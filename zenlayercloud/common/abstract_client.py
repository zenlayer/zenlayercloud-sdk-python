#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
import json
import time

import zenlayercloud
from zenlayercloud.common.abstract_model import AbstractModel
from zenlayercloud.common.config import Config
from zenlayercloud.common.excpetion import error_code
from zenlayercloud.common.excpetion.zenlayer_cloud_sdk_exception import ZenlayerCloudSdkException
from zenlayercloud.common.request import BaseRequest, ApiProxyClient
from zenlayercloud.common.response import BaseResponse
from zenlayercloud.common.utils import sha256hex, hmac_sha256

_json_content_type = 'application/json'


class AbstractClient(object):
    _api_version = ''
    _service = ''
    _sdk_version = 'SDK_PYTHON_%s' % zenlayercloud.__version__
    _signature_method = "ZC2-HMAC-SHA256"

    def __init__(self, credential, config=None):
        """base client interactive with zenlayer cloud

        :param credential: the zenlayer cloud credential
        :type credential: zenlayercloud.common.credential.Credential
        :param config: the additional config for client
        :type config: zenlayercloud.common.config.Config
        """
        self.credential = credential
        self.config = Config() if config is None else config
        is_http = True if self.config.scheme == "http" else False

        self.proxy = ApiProxyClient(host=self.config.domain,
                                    timeout=self.config.request_timeout,
                                    proxy=self.config.proxy, certification=self.config.certification,
                                    is_http=is_http, debug=self.config.debug, keep_alive=self.config.keep_alive)
        return

    def _api_call(self, action, request, method="POST", headers=None) -> dict:
        if not isinstance(request, AbstractModel):
            raise ZenlayerCloudSdkException(
                code=error_code.SDK_INVALID_REQUEST,
                message="Request must be AbstractModel"
            )
        uri = "/api/v2/%s" % self._service
        req = BaseRequest(host=self.config.domain, method=method, uri=uri, header=headers)

        header = req.header
        timestamp = int(time.time())
        header["x-zc-version"] = self._api_version
        header["x-zc-signature-method"] = self._signature_method
        header["x-zc-timestamp"] = str(timestamp)
        header["x-zc-service"] = self._service
        header["x-zc-action"] = action
        header["x-zc-sdk-version"] = self._sdk_version
        header["x-zc-sdk-lang"] = "Python"
        req.set_host(self._get_endpoint())
        req.set_content_type(_json_content_type)
        req.data = json.dumps(request.serialize())

        authorization = self._build_zc2_authorization(req)
        req.header["Authorization"] = authorization

        resp = self._send_request(req)
        return self._handle_response(resp)

    def _build_zc2_authorization(self, req):
        canonical_querystring = ""
        canonical_uri = "/"
        request_payload = req.data
        http_request_method = req.method

        canonical_headers = "content-type:%s\nhost:%s\n" % (
            req.get_content_type(),
            req.get_host()
        )
        signed_headers = "content-type;host"
        hashed_request_payload = sha256hex(request_payload)

        canonical_request = '%s\n%s\n%s\n%s\n%s\n%s' % (http_request_method,
                                                        canonical_uri,
                                                        canonical_querystring,
                                                        canonical_headers,
                                                        signed_headers,
                                                        hashed_request_payload)
        hashed_canonical_request = sha256hex(canonical_request)

        timestamp = req.header["x-zc-timestamp"]
        string2sign = '%s\n%s\n%s' % (self._signature_method,
                                      timestamp,
                                      hashed_canonical_request)
        access_key_id = self.credential.access_key_id
        access_key_password = self.credential.access_key_password

        signature = hmac_sha256(access_key_password, string2sign)

        return "%s Credential=%s, SignedHeaders=%s, Signature=%s" % (
            self._signature_method, access_key_id, signed_headers, signature)

    def _get_endpoint(self):
        return self.config.domain

    def _send_request(self, req):
        try:
            http_resp = self.proxy.request(req)
            headers = dict(http_resp.headers)

            response = BaseResponse(status=http_resp.status_code,
                                    header=headers,
                                    data=http_resp.text)
            return response
        except Exception as e:
            raise ZenlayerCloudSdkException("NETWORK_ERROR", str(e))

    @staticmethod
    def _handle_response(resp):
        resp_data = json.loads(resp.data)
        if resp.status != 200:
            code = resp_data["code"]
            message = resp_data["message"]
            request_id = resp_data["requestId"]
            raise ZenlayerCloudSdkException(code, message, request_id)
        return resp_data['response']
