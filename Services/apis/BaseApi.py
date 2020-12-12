import json

import requests


class BaseApi:
    """
    封装一些通用方法
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

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        res = self.send(data)
        assert res.status_code == 200
        token = res.json()['access_token']
        return token

    def send(self, kwargs):
        """
        封装request方法
        """
        res = requests.request(**kwargs)
        json.dumps(res.json(), indent=2, ensure_ascii=False)
        return res
