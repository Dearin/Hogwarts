
import pytest
class TestModule:
    @pytest.fixture(scope='module')
    def open(self):
        print('打开浏览器')
        yield

        print('执行teardown')
        print('最后关闭浏览器')

    @pytest.mark.usefixtures("open")
    def test_search1(self):
        print('test_search1')
        raise NameError
        pass

    def test_search2(self):
        print('test_search2')
        pass


    def test_search3(self):
        print('test_search3')
        pass