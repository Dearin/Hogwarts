
from appium import webdriver
from time import sleep
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLocate:

    def setup(self):
        # 进行一些初始化操作
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "com.xueqiu.android"
        desire_caps["appActivity"] = ".common.MainActivity"
        desire_caps["noReset"] = "true"  # 这里就避免来每次打开弹出的同意窗口
        desire_caps["skipDeviceInitialization"] = 'true'
        desire_caps["skipDriverInstallation"] = 'true'
        desire_caps["unicodeKeyBoard"] = "true"  # 输入中文字符
        desire_caps["browser"] = "Browser"  # 输入中文字符
        # 初始化驱动
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)
        # 设置一个隐形等待，增加代码的健壮性
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()


    def test_xueqiu_web(self):
        self.driver.find_element(MobileBy.XPATH,"//android.widget.TextView[@text='交易']").click()
        # 切换上下问
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        a_locator =(MobileBy.XPATH,"//android.view.View[@content-desc='A股开户']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(a_locator))
        self.driver.find_element(*a_locator).click()
        print(self.driver.contexts)
        # 后面这段代码有问题
        # 进入到输入手机号和验证码的layout页面
        # 在这里我等待一下，然后进入嵌套context
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.XPATH,"//android.widget.FrameLayout[@resource-id='com.xueqiu.android:id/container']").click()
        # # 开启显示等待framelayout中得到属性进行加载

        # 会报错：no such elemet
        # self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.EditText\").resourceId(\"phone-number\")').send_keys("12344445555")
        # self.driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.EditText\").resourceId(\"code\"))').send_keys("123456")
        # self.driver.find_element(MobileBy.ID, "phone-number").send_keys("13400000001")
        # self.driver.find_element(MobileBy.ID,"code").send_keys("123456")
        # self.driver.find_element(MobileBy.XPATH,"//android.view.View[@content-desc='立即开户']")
        sleep(2)

