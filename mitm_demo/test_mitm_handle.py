"""
这里是尝试对数据进行一个批量的处理或者说数据清理
还是相同的理念：
1- 需要知道对应处理接口的数据返回形式
2- 需要知道想进行什么样子的处理
万变不离其宗，所有dict或者list复杂数据类型，or 是数字或者字符串或者布尔型的数据，后者都是递归后处理的核心部分
"""
import json
from mitmproxy import http

rules = [0, 1, 3, 5, 100]
url_index = dict()


# @pytest.mark.parametrize("rules", [0, 1, 3, 5, 100])
def response(flow: http.HTTPFlow):
    url = flow.request.url.split(".json")[0]
    # 针对对url的访问次数来实现不同的参数处理
    if url not in url_index.keys():
        url_index[url] = 0
    else:
        url_index[url] += 1
    seed = int(url_index[url] % len(rules))
    index = rules[seed]

    # 需要处理的接口中存在一个x=**
    if "quote.json" in flow.request.url and "x=" in flow.request.url:
        # 先接收到返回的数据
        data = json.loads(flow.response.content)
        # 对数据进行批量修改
        new_data = json_travel(data, array=2, text=index, num=index)
        print()
        # 打印
        data_mess = json.dumps(new_data, indent=2, ensure_ascii=False)
        print("=====================修改后的信息=======================================")
        print(data_mess)

        # 返回修改的数据
        flow.response.text = json.dumps(new_data)


def json_travel(data, array=None, text=1, num=1):
    """
    完成json数据的倍数操作
    :param data: 要修改的内容
    :param array: 列表的修改规则，为None默认不修改
    :param text: 字符串的修改规则，为1默认不修改
    :param num: 整数或者浮点数的修改规则，为1默认不修改
    :return: data_new
    """
    # 如果接口返回的参数是dict复杂数据类型，进行遍历：
    if isinstance(data, dict):
        data_new = dict()
        for k, v in data.items():
            # 对字典内部的数据再次进行一个递归，因为value还是一个复杂数据类型
            data_new[k] = json_travel(v, array, text, num)
            # 对应行情中每一只股票的名称，这里可以再进行处理，方便直接看出效果
            if k == "name":
                data_new[k] = json_travel(v, array, text=2, num=1)

    # 如果是列表，就对列表的每一项进行一个遍历，并进行数据处理
    elif isinstance(data, list):
        data_new = list()
        for item in data:
            item_new = json_travel(item, array, text, num)
            # 如果传入的array为空，则不进行处理
            if array is None:
                data_new.append(item_new)
            # 若array不为空，判断array修改规则
            else:
                if isinstance(array, int) and array >= 0:
                    for i in range(array):
                        data_new.append(item_new)
                else:
                    data_new = data

    # 如果传入的是字符串，则和传入的text参数进行相乘，实现对字符串的修改
    elif isinstance(data, str):
        if isinstance(text, int) and text >= 0:
            data_new = data * text
        else:
            data_new = data

    # 如果是int或者float的数据，就对数字做一个乘积
    elif isinstance(data, int) or isinstance(data, float):
        data_new = data * num

    else:
        data_new = data

    return data_new
