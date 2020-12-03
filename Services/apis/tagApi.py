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
        如果要创建一个全新的标签组以及标签，则需要通过group_name参数指定新标签组名称，如果填写的groupname已经存在，则会在此标签组下新建标签。
        如果填写了group_id参数，则group_name和标签组的order参数会被忽略。
        不支持创建空标签组。
        标签组内的标签不可同名，如果传入多个同名标签，则只会创建一个。
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

    def get_groups_names(self):
        result = self.get_corp_tag_list()
        groups = jsonpath(result, '$.tag_group..group_name')
        return groups

    def get_tags_name(self, group_name):
        result = self.get_corp_tag_list()
        tags = jsonpath(result, '$.tag_group.(?@group_name=="Hogwarts").tag..name')
        return tags
