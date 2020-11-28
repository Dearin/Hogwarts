"""
这里是尝试对数据进行一个批量的处理或者说数据清理
还是相同的理念：
1- 需要知道对应处理接口的数据返回形式
2- 需要知道想进行什么样子的处理
万变不离其宗，所有dict或者list复杂数据类型，or 是数字或者字符串或者布尔型的数据，后者都是递归后处理的核心部分
"""
import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 对进行处理的接口进行筛选
    if "quote.json" in flow.request.url and "x=" in flow.request.url:
        # 先接收到返回的数据
        data = json.loads(flow.response.content)

        # 对数据进行批量修改
        new_data = json_travel(data, num=0.1, text=1)
        ## 这步是为了方便打印
        data_mess = json.dumps(new_data, indent=2, ensure_ascii=False)
        print("=====================修改后的信息=======================================")
        print(data_mess)

        # 返回修改的数据
        flow.response.text = json.dumps(new_data)


def json_travel(data, array=None, text=1, num=1):
    # 如果接口返沪的参数是dict复杂数据类型，进行遍历：
    if isinstance(data, dict):
        data_new = dict()
        for k, v in data.items():
            # 对字典内部的数据再次进行一个递归，因为value还是一个复杂数据类型
            data_new[k] = json_travel(v, array, text, num)
            # 这个地方是name核心参数了,只对name核心参数进行变更，如果有其他的需要可以继续完善代码
            if k == "name":
                data_new[k] = json_travel(v, array, text=2, num=1)


    # 如果是列表，就对列表的每一项进行一个遍历,这里咩有对数组赋值因为目的只是修改已有的参数
    elif isinstance(data, list):
        data_new = list()
        for item in data:
            item_new = json_travel(item, array, text, num)
            if array is None:
                data_new.append(item_new)
            else:  # 如果对数组进行编辑，后续的数据处理操作
                pass
    # 如果传入的是字符串，则和传入的text参数进行相乘，实现对字符串的修改
    elif isinstance(data, str):
        data_new = data * text

    # 如果是int或者float的数据，就对数字做一个乘积
    elif isinstance(data, int) or isinstance(data, float):
        data_new = data * num

    else:
        data_new = data

    return data_new
