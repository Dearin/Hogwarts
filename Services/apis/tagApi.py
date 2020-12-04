from datetime import datetime

import requests
from jsonpath import jsonpath


class Tag:
    """封装关于企业用户标签的接口
    1、新增标签接口
    2、删除标签接口
    3、编辑标签接口
    4、查询标签接口等
    """

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        """
        获取客户联系的token权限
        :return: token字符串
        """
        corpid = 'ww527f8b180913ddef'
        corpsecret = 'L80RbDtBJdOvSCxYQO77YK_ag0ZKg6_8Nm-ZjtRIyV8'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        res = requests.get(url=url, params=params)
        assert res.status_code == 200
        token = res.json()['access_token']
        return token

    def get_corp_tag_list(self):
        """
        企业可通过此接口获取所有企业客户标签详情。
        :returns tag_list
        """
        # 获取token
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        params = {
            "access_token": self.token
        }
        res = requests.post(url=url, params=params)
        return res

    def add_corp_tag(self, group_name, tag_name):
        """
        如果要向指定的标签组下添加标签，需要填写group_id参数；
        :return:
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag'
        params = {
            'access_token': self.token
        }
        json = {
            "group_name": group_name,
            "tag": [{
                "name": tag_name
            }
            ]
        }
        res = requests.post(url=url, params=params, json=json)
        return res.json()

    def edit_corp_tag(self, id, tag_name):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag"
        params = {
            "access_token": self.token
        }
        json = {
            "id": id,
            "name": tag_name,
        }
        res = requests.post(url=url, params=params, json=json)
        return res.json()

    def del_corp_tag(self, tag_id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
        params = {
            "access_token": self.token
        }
        json = {
            "tag_id": tag_id
        }
        res = requests.post(url=url, params=params, json=json)
        assert res.status_code == 200
        assert res.json()['errcode'] == 0
        assert res.json()['errmsg'] == 'ok'

    def get_groups_names(self):
        """
        获取当前所有的标签组
        :return: groups 便签组列表
        """
        result = self.get_corp_tag_list()
        groups = jsonpath(result.json(), '$.tag_group..group_name')
        return groups

    def get_tags_name(self, group_name):
        """根据组名来查询对应的标签
        :returns tags 标签列表
        """
        result = self.get_corp_tag_list()
        group = jsonpath(result.json(), f'$.tag_group[?(@.group_name=="{group_name}")]')[0]
        tags = jsonpath(group, '$.tag..name')
        return tags

    def get_tag_id(self, group_name):
        result = self.get_corp_tag_list()
        result = result.json()['tag_group']
        tag_id = []
        for i in result:
            if i['group_name'] == group_name:
                tag = i['tag']
                for i in tag:
                    tag_id.append(i['id'])
        return tag_id
