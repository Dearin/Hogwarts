
from appium import webdriver
from time import sleep

class TestLocate:

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
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)
        # 设置一个隐形等待，增加代码的健壮性
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_locate_app(self):
        print("测试搜索用例")
        '''
        1-打开雪球app
        2-点击搜索框
        3-向搜索框中输入"阿里巴巴"
        4-点击搜索结果中的阿里巴巴
        5-获取阿里巴巴的股价，并判断该股价大于200 
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        # 选中第一个代选项
        # 这里有个疑问，当两个地方的resourceid完全一致但是又没有别的属性作为协助来区分该如何处理呢？
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/stockName" and @text="阿里巴巴"]').click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        print(current_price)
        assert current_price > 200
        print("测试结束啦")
        sleep(2)

