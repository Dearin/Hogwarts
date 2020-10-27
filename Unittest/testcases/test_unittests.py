import unittest

from Unittest.utils.HTMLTestRunner_PY3 import HTMLTestRunner

'''这是一个被测试的函数'''
class Search():
    def search_fun(self):
        print(" i'm a search")
        return True

'''定义一个测试类,必须要继承哦'''
class TestUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("-- 测试类执行开始前 --")
        print("-- 初始化search")
        cls.search = Search()

    def setUp(self) -> None:
        print(" -- start testcase -- ")

    def tearDown(self) -> None:
        print(" --  end testcase -- ")

    @classmethod
    def tearDownClass(cls) -> None:
        print("-- 测试类执行结束 --")

    def test_search1(self):
        '''search = Search ,这里可以考虑去setupclass中去处理'''
        print(" ++ search1 ++")
        assert True == self.search.search_fun()

    def test_unittest2(self):
        print(" ++ test2 ++")

    def test_unittest3(self):
        print(" ++ test3 ++")
