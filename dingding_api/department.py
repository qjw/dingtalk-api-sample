"""
部门操作相关api
"""
import json

import requests

from dingding_api.base import DingBase


class DingDepartment(DingBase):
    def get_department_list(self):
        """
        获取部门列表
        :return:
        """
        urls = self.base_url + 'department/list'
        params = {
            'access_token': self.token
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['department']
        else:
            raise ValueError('获取部门列表失败, ' + data['errmsg'])


    def create_department(self, params):
        urls = self.base_url + 'department/create?access_token=%s'%self.token
        params = json.dumps(params)
        r = requests.post(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('创建部门失败, ' + data['errmsg'])

    def delete_department(self, id):
        urls = self.base_url + '/department/delete'
        params = {
            'access_token': self.token,
            'id': id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('删除部门失败, ' + data['errmsg'])

    def get_department_detail(self, id):
        urls = self.base_url + '/department/get'
        params = {
            'access_token': self.token,
            'id': id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取部门详情失败, ' + data['errmsg'])


    def get_department_subids(self, id):
        urls = self.base_url + '/department/list_ids'
        params = {
            'access_token': self.token,
            'id': id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取部门子部门ids失败, ' + data['errmsg'])


    def get_department_parent(self, id):
        urls = self.base_url + '/department/list_parent_depts_by_dept'
        params = {
            'access_token': self.token,
            'id': id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取部门父部门ids失败, ' + data['errmsg'])

    def get_org_user_count(self, active):
        urls = self.base_url + '/user/get_org_user_count'
        params = {
            'access_token': self.token,
            'onlyActive': active,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取集团人数失败, ' + data['errmsg'])

    def get_user_detail(self, id):
        urls = self.base_url + '/user/get'
        params = {
            'access_token': self.token,
            'userid': id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取人员详情, ' + data['errmsg'])

    def get_department_userids(self, id):
        urls = self.base_url + '/user/getDeptMember'
        params = {
            'access_token': self.token,
            'deptId': id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取部门人员id, ' + data['errmsg'])

    def get_department_users(self, department_id):
        """
        获取部门成员
        :param department_id:
        :return:
        """
        urls = self.base_url + 'user/simplelist'
        params = {
            'access_token': self.token,
            'department_id': department_id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['userlist']
        else:
            raise ValueError('获取部门成员失败, ' + data['errmsg'])

    def get_department_users_detail(self, department_id):
        """
        获取部门成员(详情)
        :param department_id:
        :return:
        """
        urls = self.base_url + 'user/list'
        params = {
            'access_token': self.token,
            'department_id': department_id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['userlist']
        else:
            raise ValueError('获取部门成员(详情)失败, ' + data['errmsg'])

    def get_admin_users(self):
        urls = self.base_url + 'user/get_admin'
        params = {
            'access_token': self.token
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取管理员列表失败, ' + data['errmsg'])


    def get_admin_user_scopes(self, id):
        urls = self.base_url + 'topapi/user/get_admin_scope'
        params = {
            'access_token': self.token,
            'userid': id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errcode'] == 0: # 没有errmsg
            return data
        else:
            raise ValueError('获取管理员通讯录权限范围失败, ' + data['errmsg'])

    def create_user(self, params):
        urls = self.base_url + 'user/create?access_token=%s'%self.token
        params = json.dumps(params)
        r = requests.post(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('创建用户失败, ' + data['errmsg'])


    def delete_user(self, id):
        urls = self.base_url + '/user/delete'
        params = {
            'access_token': self.token,
            'userid': id,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('删除用户失败, ' + data['errmsg'])


    def get_user_by_code(self, code):
        urls = self.base_url + '/user/getuserinfo'
        params = {
            'access_token': self.token,
            'code': code,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取人员详情, ' + data['errmsg'])
