import json

import requests

from dingding_api.base import get_timestamp, sign
from dingding_api.config import SCAN_APPID, BASE_URL, SCAN_APP_SECRET


def get_scan_login_url(callback):
    return "%sconnect/qrconnect?appid=%s&response_type=code&scope=snsapi_login&state=STATE&redirect_uri=%s"%(BASE_URL, SCAN_APPID, callback)


def getuserinfo_bycode(code):
    timestamp = get_timestamp()
    signature = sign(SCAN_APP_SECRET, timestamp)

    url = "%ssns/getuserinfo_bycode?signature=%s&timestamp=%s&accessKey=%s"%(
        BASE_URL, signature, timestamp, SCAN_APPID
    )

    params = {
        'tmp_auth_code': code,
    }
    params = json.dumps(params)
    r = requests.post(url, params)
    data = json.loads(r.text, encoding="utf-8")
    return data