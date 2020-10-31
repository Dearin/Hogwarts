from appium import webdriver
from time import sleep
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MobileBY(object):
    pass


class TestWebGy:

        def setup(self):
            desire_cap = {}
            desire_cap["platformName"] = "android"
            desire_cap["deviceName"] = "192.168.56.103:5555"
            desire_cap["noReset"] = "true"
            desire_cap["browser"] = "Browser"
            desire_cap["appPackage"] = "io.appium.android.apis"
            desire_cap["appActivity"] = ".ApiDemos"
            # 初始化driver，这里的地址和端口是和Appium服务端保持一致的！
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(5)

        def teardown(self):
            self.driver.quit()

        def test_browser(self):
            '''滚动找到Webview'''
            self.driver.find_element(MobileBy.XPATH,'//*[@content-desc="Views"]').click()
            # 打印当前
            context = self.driver.contexts
            print(self.driver.contexts)
            self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                            'new UiSelector().'
                                                            'scrollable(true).instance(0)).'
                                                            'scrollIntoView(new UiSelector().text("WebView").'
                                                            'instance(0));').click()
            # 设置一个显性等待,等待webView计划
            print(self.driver.contexts)
            contexts = self.driver.contexts
            # 进入嵌套的webview中
            self.driver.switch_to.context(contexts[-1])
            self.driver.find_element(MobileBy.XPATH,"//android.widget.EditText[@resource-id='i_am_a_textbox']").send_keys("  I solve some problems!")
            self.driver.find_element(MobileBy.XPATH,"i am a link").click()
            # WebDriverWait.until(expected_conditions.element_to_be_clickable((MobileBY.ID,"io.appium.android.apis:id/wv1")))
            print(self.driver.page_source)