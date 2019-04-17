import base64
import hashlib
import json
from urllib.parse import quote
from random import randint
from time import time

import requests

from dingding_api.config import AGENT_ID, APP_ID, APP_SECRET, BASE_URL, CORP_ID


def get_timestamp():
    return str(int(time()))


def sha1(s):
    return hashlib.sha1(s).hexdigest()

default_char_list='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456_'

def get_random_string(length=16, char_list=default_char_list):
    string = ''
    for i in range(length):
        string += char_list[randint(0, len(char_list) - 1)]
    return string


def sign(secret, message):
    import hmac
    import hashlib

    signature = hmac.new(
        bytes(secret, encoding='utf-8'),
        msg=bytes(message, encoding='utf-8'),
        digestmod=hashlib.sha256,
    ).digest()

    return quote(base64.b64encode(signature).decode('ascii'))

def sign_jsapi(parameters):
    if hasattr(parameters, "items"):
        keys = parameters.keys()
        keys = sorted(keys)
        parameters = "&".join(['%s=%s' % (key, parameters[key]) for key in keys])

    return sha1(bytes(parameters, encoding='utf-8'))


class DingBase(object):
    """
    钉钉api基础对象:获取并提供钉钉凭证token
    """

    def __init__(self):
        self.agent_id = AGENT_ID
        self.corp_id = APP_ID
        self.corp_secret = APP_SECRET
        self.base_url = BASE_URL
        self.headers = {'content-type': 'application/json'}

    # 只读属性装饰器,将方法变为对象属性
    @property
    def token(self):
        """
        钉钉token
        :return:
        """
        urls = self.base_url + 'gettoken'
        params = {
            'appkey': self.corp_id,
            'appsecret': self.corp_secret,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['access_token']
        else:
            raise ValueError('获取凭证失败, ' + data['errmsg'])

    @property
    def jsapi_token(self):
        urls = self.base_url + 'get_jsapi_ticket'
        params = {
            'access_token': self.token,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['ticket']
        else:
            raise ValueError('获取凭证失败, ' + data['errmsg'])


    def jsapi_config(self, url):
        timeStamp = get_timestamp()
        nonceStr = get_random_string(16)
        jsapi_ticket = self.jsapi_token
        return {
            "agentId": AGENT_ID,
            "corpId": CORP_ID,
            "timeStamp": timeStamp,
            "nonceStr": nonceStr,
            "signature": sign_jsapi({
                "jsapi_ticket": jsapi_ticket,
                "noncestr": nonceStr,
                "timestamp": timeStamp,
                "url": url,
            })
        }
