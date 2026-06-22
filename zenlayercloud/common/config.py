#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.

DEFAULT_DOMAIN = "console.zenlayer.com"

DEFAULT_RATE_LIMIT_MAX_RETRIES = 3


def exponential_backoff(index):
    """Default backoff: 1s, 2s, 4s, 8s, ..."""
    return 2 ** index


class Config(object):

    def __init__(self, scheme=None, domain=None, request_timeout=60, proxy=None, keep_alive=False, debug=False,
                 certification=None, rate_limit_max_retries=DEFAULT_RATE_LIMIT_MAX_RETRIES,
                 rate_limit_retry_duration=None):
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
         :param rate_limit_max_retries: Max retries when REQUEST_LIMIT_EXCEEDED (HTTP 429)
            is returned. Defaults to 3. Set to 0 to disable.
         :type rate_limit_max_retries: int
         :param rate_limit_retry_duration: A callable ``f(index) -> seconds`` that returns
            the wait time before the next retry. Defaults to exponential backoff.
         :type rate_limit_retry_duration: callable
         """

        self.scheme = scheme or "https"
        self.proxy = proxy
        self.domain = DEFAULT_DOMAIN if domain is None else domain
        self.keep_alive = keep_alive
        self.request_timeout = 60 if request_timeout is None else request_timeout
        self.debug = debug
        self.certification = certification
        self.rate_limit_max_retries = rate_limit_max_retries
        self.rate_limit_retry_duration = rate_limit_retry_duration or exponential_backoff

