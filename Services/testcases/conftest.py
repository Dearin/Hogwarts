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
