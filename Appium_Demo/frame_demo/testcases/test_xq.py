import allure
from Appium_Demo.frame_demo.Pages.MainPage import MainPage


@allure.feature("黑名单处理模块")
class TestBlackList:

    @allure.story('这个测试雪球的异常处理情况')
    def test_goto_search(self):
        self.main = MainPage()
        result = self.main.goto_market().goto_search().search()
        assert '阿里巴巴' in result


@allure.feature('登陆模块')
class TestLogin:
    @allure.story('登陆方法')
    def test_login(self):
        print('this is login')

# 调用feature的方法
#