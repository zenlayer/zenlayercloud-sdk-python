#  Zenlayer.com Inc.
#  Copyright (c) 2014-2023 All Rights Reserved.
import hashlib
import hmac
import sys


def hmac_sha256(key, msg):
    return hmac.new(key.encode('utf-8'), msg.encode('utf-8'), hashlib.sha256).hexdigest()


def sha256hex(s: str):
    if sys.version_info[0] == 3:
        s = s.encode("utf8")
    return hashlib.sha256(s).hexdigest()
