import hamcrest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest


class TestParam:
    def setup(self):
        # 进行一些初始化操作
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "com.xueqiu.android"
        desire_caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
        desire_caps["noReset"] = "true"  # 这里就避免来每次打开弹出的同意窗口
        desire_caps["skipDeviceInitialization"] = 'true'
        desire_caps["unicodeKeyBoard"] = "true"  # 输入中文字符
        # 初始化驱动
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        # 设置一个隐形等待，增加代码的健壮性
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 需要注意的事，由于参数化
        # 所以每次操作结束后需要清理测试环境，回到初始状态
        # 在这里只需要点击一次返回即可
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
        pass

    # parametrize = _ParametrizeMarkDecorator(Mark("parametrize", (), {}))
    @pytest.mark.parametrize('search_key,type,expected_price', [
        ('alibaba', 'BABA', 300),
        ('xiaomi', '01810', 22)
    ])
    def test_param(self,search_key,type,expected_price):
        '''
        !!! 注意，声明了参数化，就需要在
        1- 打开雪球app
        2- 点击搜索框
        3- 输入搜索词 alibaba/xiaomi -- 这个参数需要参数化
        4- 选择第一个搜索结果 --
        5- 判断股票价格  -- 各自价格的浮动需要参数化
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys(search_key)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        current_price = self.driver.find_element(MobileBy.XPATH,
                                                 f'//*[@resource-id="com.xueqiu.android:id/stockCode" and @text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        price = float(current_price)
        print(f"阿里巴巴香港的股价是：{price}")
        # 使用hamcrest进行断言
        # expect_price = 300
        hamcrest.close_to(price, expected_price * 0.1)
