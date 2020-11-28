"""
进行数据rewrite的主要思想是：
1- 先接收到接口返回的信息
2- 针对信息作出修改
3- 返回修改的信息
"""
import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.url and "x=" in flow.request.url:
        # 接收到返回的数据,数据是存放在response的content体中的，抓包可以看见
        # 把数据转换为json格式
        data = json.loads(flow.response.content)
        print("=======================修改前的数据=======================")
        print(data)

        # 针对数据做一些修改
        data["data"]["items"][0]["quote"]["name"] = data["data"]["items"][0]["quote"]["name"] + "test_rewrite"
        data["data"]["items"][1]["quote"]["name"] = data["data"]["items"][1]["quote"]["name"] + "test_rewrite"
        data["data"]["items"][2]["quote"]["name"] = data["data"]["items"][2]["quote"]["name"] + "test_rewrite"
        print("+++++++++++++++++++++修改后的数据+++++++++++++++++++++++")
        print(data)

        # 返回修改的数据，将json格式的数据再转换成其他
        """
            flow.response.content = json.dumps(data)
            raise TypeError(
            TypeError: Message content must be bytes, not str. Please use .text if you want to assign a str.
            为什么只能修改response的text内容，而不能修改content呢？上面说的是，content只能是字节
        """
        flow.response.text = json.dumps(data)