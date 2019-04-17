import json
import os

import requests
from dingding_api.base import DingBase

class DingMedia(DingBase):
    def upload(self, storage, filename, tp):
        urls = self.base_url + '/media/upload?access_token=%s&type=%s'%(self.token, tp)
        files = {'media': (filename, storage)}
        r = requests.post(urls, files=files)
        data = json.loads(r.text, encoding="utf-8")
        return data