import pytest
class Test001:

    @pytest.fixture
    def login(self):
        print('this is a login_method')
        return ('tom','123456')

    @pytest.fixture
    def operate(self):
        print('登陆后的操作')

    #以下为测试用例
    def test_case1(self,login,operate):
        print(login)
        print('依赖于login()方法')

    def test_case2(self):
        print('test2,不需要login')

    def test_case3(self,login):
        print('test3,需要login')
