#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.

DEFAULT_DOMAIN = "console.zenlayer.com"


class Config(object):

    def __init__(self, scheme=None, domain=None, request_timeout=60, proxy=None, keep_alive=False, debug=False,
                 certification=None):
        """config.

         :param scheme: http or https, default is https.
         :type scheme: str
         :param request_timeout: The http timeout in second.
         :type request_timeout: int
         :param domain: The domain to access, default is console.zenlayer.com.
         :type domain: str
         :param keep_alive: The http keep alive config.
         :type keep_alive: bool
         :param debug: open or close debug mode.
         :type debug: bool
         """

        self.scheme = scheme or "https"
        self.proxy = proxy
        self.domain = DEFAULT_DOMAIN if domain is None else domain
        self.keep_alive = keep_alive
        self.request_timeout = 60 if request_timeout is None else request_timeout
        self.debug = debug
        self.certification = certification

