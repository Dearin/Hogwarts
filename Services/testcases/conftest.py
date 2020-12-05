from typing import List
import pytest


@pytest.fixture(scope='session', autouse=True)
def status():
    print("测试开始")
    yield
    print("测试结束")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf8').decode('unicode-escape')
        # 通过对items列表中的元素进行操作，就可以控制执行用例的顺序来
    print("收集到的用例：%s"% items)