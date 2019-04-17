import json
import requests
from dingding_api.base import DingBase
from dingding_api.config import AGENT_ID


class DingMessage(DingBase):
    """
    钉钉消息相关api
    """

    def send(self, msg, user_list, dept_list, agent_id=AGENT_ID):
        urls = self.base_url + '/topapi/message/corpconversation/asyncsend_v2?access_token=' + self.token
        params = {
            'agent_id': agent_id,
            'msg': msg,
        }
        if user_list:
            params['userid_list'] = user_list
        if dept_list:
            params['dept_id_list'] = dept_list
        params = json.dumps(params)
        r = requests.post(urls, params, headers=self.headers)
        data = json.loads(r.text, encoding="utf-8")
        return data

    def send_msg(self, msg, user_list, dept_list, agent_id=AGENT_ID, msg_type='text'):
        """
        发送企业会话消息(工作通知):应用名称会展示在工作通知中
        :param msg: 消息内容
        :param user_list: 用户userid列表,字符串,以|分割 钉钉userid
        :param dept_list: 部门id列表,与用户列表必须有一个填写 字符串 以|分割
        :param agent_id: 企业应用id，这个值代表以哪个应用的名义发送消息
        :param msg_type: 消息格式
        :return:
        """
        urls = self.base_url + 'message/send?access_token=' + self.token
        params = {
            'agentid': agent_id,
            'msgtype': msg_type,
            msg_type: {
                'content': msg,
            }
        }
        if user_list:
            params['touser'] = user_list
        if dept_list:
            params['toparty'] = dept_list
        params = json.dumps(params)
        r = requests.post(urls, params, headers=self.headers)
        data = json.loads(r.text, encoding="utf-8")
        return data

    def upload_media(self, image_obj, upload_type='image'):
        """
        上传媒体文件
        :param image_obj: Django媒体对象或图片路径
        :param upload_type:
        :return:
        """
        urls = self.base_url + 'media/upload?access_token={}&type={}'.format(self.token, upload_type)
        if isinstance(image_obj, str):
            params = {
                'media': open(image_obj, 'rb'),
            }
        else:
            params = {
                'media': image_obj,
            }
        r = requests.post(urls, files=params)
        data = json.loads(r.text, encoding="utf-8")
        return data

    def send_image(self, media_id, user_list, agent_id=AGENT_ID, msg_type='image'):
        """
        发送图片
        :param media_id: 上传图片到钉钉后回传的图片id
        :param user_list:
        :param agent_id:
        :param msg_type:
        :return:
        """
        urls = self.base_url + 'message/send?access_token=' + self.token
        params = {
            'touser': user_list,
            'agentid': agent_id,
            'msgtype': msg_type,
            msg_type: {
                "media_id": media_id,
            }
        }
        params = json.dumps(params)
        r = requests.post(urls, params, headers=self.headers)
        data = json.loads(r.text, encoding="utf-8")
        return data
