from mitmproxy import http


def request(flow: http.HTTPFlow):
    """
    其实map_local的替换修改思想和charles是一致的
    1、找到需要替换的url地址或者说在url中有符合替换条件的名称
    2、进行json数据的替换
    :param flow:
    :return:
    """

    # 官方示例
    # # redirect to different host
    # if flow.request.pretty_host == "xueqiu.com":
    #     flow.request.host = "mitmproxy.org"
    # # answer from proxy
    # elif flow.request.path.endswith("/brew"):
    # 	flow.response = http.HTTPResponse.make(
    #         418, b"I'm a teapot",
    #     )

    # 进行条件筛选
    if "quote.json" in flow.request.url:
        # 进行map_local的替换
        with open("/Users/deng/tests/quote.json") as f:
            # 替换response中的json数据
            flow.response = http.HTTPResponse.make(
                status_code=200, content=f.read()
            )
