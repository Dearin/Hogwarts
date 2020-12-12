import json
from datetime import datetime

import requests
from jsonpath import jsonpath

from Services.apis.BaseApi import BaseApi


class Tag(BaseApi):
    """封装关于企业用户标签的接口
    1、新增标签接口
    2、删除标签接口
    3、编辑标签接口
    4、查询标签接口等
    """

    # 被优化到base_api中去了
    # def __init__(self):
    #     self.token = self.get_token()
    #
    # def get_token(self):
    #     """
    #     获取客户联系的token权限
    #     :return: token字符串
    #     """
    #     corpid = 'ww527f8b180913ddef'
    #     corpsecret = 'L80RbDtBJdOvSCxYQO77YK_ag0ZKg6_8Nm-ZjtRIyV8'
    #     url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    #     params = {
    #         "corpid": corpid,
    #         "corpsecret": corpsecret
    #     }
    #     res = requests.get(url=url, params=params)
    #     assert res.status_code == 200
    #     token = res.json()['access_token']
    #     return token

    def get_corp_tag_list(self):
        """
        企业可通过此接口获取所有企业客户标签详情。
        :returns tag_list
        """
        # 获取token
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {
                "access_token": self.token
            }
        }
        res = self.send(data)
        return res

    def add_corp_tag(self, group_name, tag_name, **kwargs):
        """
        如果要向指定的标签组下添加标签，需要填写group_id参数；
        :return:
        """
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            "params": {
                'access_token': self.token
            },
            "json": {
                "group_name": group_name,
                "tag": tag_name,
                **kwargs
            }
        }

        res = self.send(data)
        return res

    def edit_corp_tag(self, tag_id, tag_name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": tag_id,
                "name": tag_name
            }
        }
        res = self.send(data)
        return res

    def del_corp_tag(self, tag_id):
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [tag_id]
            }
        }
        res = self.send(data)
        # print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        assert res.status_code == 200
        assert res.json()['errcode'] == 0
        assert res.json()['errmsg'] == 'ok'

    def del_corp_group(self, group_id):
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_id": group_id
            }
        }
        res = self.send(data)
        # print(res.json())
        return res

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
        return

    def get_tags_by_group_name(self, group_name):
        # 根据group_name获取到其对应的t标签信息
        result = self.get_corp_tag_list()
        group = jsonpath(result.json(), f'$.tag_group[?(@.group_name=="{group_name}")]')[0]
        tag_names = jsonpath(group, '$.tag..name')
        tag_ids = jsonpath(group, '$.tag..id')
        tags = {}
        for i, j in zip(tag_names, tag_ids):
            tags[i] = j
        return tags

    def get_ids_by_group_name(self, group_name):
        result = self.get_corp_tag_list()
        result = result.json()['tag_group']
        tag_id = []
        for i in result:
            if i['group_name'] == group_name:
                tag = i['tag']
                for i in tag:
                    tag_id.append(i['id'])
        return tag_id

    def get_group_id_by_name(self, group_name):
        # 查询元素是否存在，如果不存在，报错
        for group in self.get_corp_tag_list().json()["tag_group"]:
            if group_name in group["group_name"]:
                return group["group_id"]
        print("group name not in group")
        return ""

    def is_group_id_exist(self, group_id):
        """判断需要删除的id是是否存在"""
        # 查询元素是否存在，如果不存在，报错
        for group in self.get_corp_tag_list().json()["tag_group"]:
            if group_id in group["group_id"]:
                return True
        print("group_id not in group")
        return False

    def add_n_detect(self, group_name, tag_name, **kwargs):
        """进行添加方法的加固
        1、如果添加一个标签时报错，则进行处理
        """
        res = self.add_corp_tag(group_name, tag_name)
        # 报错信息为tag已经存在
        if res.json()["errcode"] == 40071:
            group_id = self.get_group_id_by_name(group_name)
            # 如果显示该id不存在
            if not group_id:
                # 元素不存在，则接口有问题
                return "接口异常"
            else:
                # 元素存在，则进行删除
                self.del_corp_group([group_id])
                self.add_corp_tag(group_name, tag_name, **kwargs)
        result = self.get_group_id_by_name(group_name)
        if not result:
            print("add_method is not success")
        return result

    def delete_n_detect(self, group_ids):
        """针对删除的方法做加固
        1、如果遇到删除的对象不存在,则新增一个对象，并将该对象存入一个已删除列表中方便查询管理
        2、如果遇到删除的对象存在时，则进行删除，并将该对象存入一个已删除列表
        """
        deleted_group_ids = []
        # 进行删除
        res = self.del_corp_group(group_ids)
        if res.json()["errcode"] == 40068:
            for group_id in group_ids:
                # invalid code
                if not self.is_group_id_exist(group_id):
                    group_tmp = self.add_n_detect(group_name="TMP00123",
                                                  tag_name=[{"name": "TAG1"}])
                    deleted_group_ids.append(group_tmp)
                # 如果标签存在，则存入标签组
                else:
                    deleted_group_ids.append(group_id)
            # 重新进行一次删除
            self.del_corp_group(deleted_group_ids)
