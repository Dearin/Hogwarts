
from appium import webdriver
from time import sleep
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import hamcrest

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
        desire_caps["automatorName"] = "automator2"  # 输入中文字符
        # 初始化驱动
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)
        # 设置一个隐形等待，增加代码的健壮性
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
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

    @pytest.mark.skip
    def test_attr(self):
        '''
        1 - 进入首页
        2 - 定位首页的搜索框
        3 - 判断搜索框是是否可用，并检查它的name值
        4 - 打印这个搜索框的size
        5 - 向搜索框输入alibaba
        6 - 判断阿里巴巴是否可见
        7 - 可见，则打印搜索成功；否则打印搜索失败
        :return:
        '''

        ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(ele.size)
        print(ele.location)
        print(ele.size)
        search_enable = ele.is_enabled()
        if search_enable == True:
            ele.click()
            alibaba_ele = self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("alibaba")
            displayed_ele = alibaba_ele.get_attribute("displayed")
            if displayed_ele == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    @pytest.mark.skip
    def test_touchaction(self):
        window_rect = self.driver.get_window_rect()
        print(window_rect)
        x_width = window_rect['width']
        y_height = window_rect['height']
        x_start = int(x_width/2)
        y_start = int(y_height * 4/5)
        y_end = int(y_height * 1/5)
        print(x_start,y_start,y_end)
        action = TouchAction(self.driver)
        action.press(x=x_start,y=y_start).wait(200).move_to(x=x_start,y=y_end).wait(200).release().perform()
        sleep(2)
        # 看不见页面滑动，但是用例执行通过了

    def test_locate_senior(self):
        print("测试搜索用例")
        '''
        1-打开雪球app
        2-点击搜索框
        3-向搜索框中输入"阿里巴巴"
        4-获取香港阿里巴巴的股价
        5-获取阿里巴巴的股价，并判断该股价是否大于200  - 这里需要解决的是下面的那个问题
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        # 选中第一个代选项
        # 这里有个疑问，当两个地方的resourceid完全一致但是又没有别的属性作为协助来区分该如何处理呢？
        # 在之前的用例里，是通过点击进去更深的一层获取，这里则修改了操作，通过子节点去定位父节点的方式来获取股价
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/name" and @text ="阿里巴巴"]').click()
        current_price = self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/stockCode" and @text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        price = float(current_price)
        print(f"阿里巴巴香港的股价是：{price}")
        # 使用hamcrest进行断言
        expect_price = 300
        hamcrest.close_to(price,expect_price * 0.1)

    def test_myinfo(self):
        '''
        1 - 点击我的，进入到个人信息
        2 - 点击登陆，进入登陆页面
        3 - 输入用户名和密码
        4 -点击登陆
        注意：以上全部是Uiselector来进行定位联系
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("username")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()



    def test_scroll(self):
        # 通过多属性查找
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("热门").className("android.widget.TextView")').click()
        # 通过父查子关系查找，子查兄弟是.fromParent()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("关注"))').click()
        # 滚动，查找A股罗雷锋
        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("投基行动派").'
                                                        'instance(0));').click()
        sleep(3)



