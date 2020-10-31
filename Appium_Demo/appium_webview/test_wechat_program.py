from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestWechatProgram:

    def setup(self):
        # 进行一些初始化操作
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "com.tencent.mm"
        desire_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        desire_caps["noReset"] = "true"  # 这里就避免来每次打开弹出的同意窗口
        desire_caps["skipDeviceInitialization"] = 'true'
        desire_caps["skipDriverInstallation"] = 'true'
        desire_caps["unicodeKeyBoard"] = "true"  # 输入中文字符
        desire_caps["resetKeyBoard"] = "true"  # 输入中文字符
        desire_caps["browser"] = "Chrome"  # 输入中文字符
        desire_caps["ShowChromedriverLog"] = "true"  # 输入中文字符
        # desire_caps["chromedriverExecutableDir"] = "/Users/deng/Documents/driver/chromedriver"  # 输入中文字符

        # 将chromeoption传递给chromedriver
        desire_caps["chromeOptions"] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }
        # 这里的端口不能设置成5038
        desire_caps["adbPort"] = 5037
        # 初始化驱动
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)

        # self.enter_micro_program()
        # print(self.driver.contexts)

    def teardown(self):
        self.driver.quit()

    def test_wechat_scroll(self):
        # 原生测试：滑动页面，展示出小程序搜索位置
        # 输入需要查询的小程序名称进行查找
        # 点击所需要的小程序，进入程序页面
        size = self.driver.get_window_size()
        print(self.driver.contexts)
        # self.driver.swipe(size['width'] * 0.3,size['height'] * 0.5,size['width'] * 0.3,size['height'] * 0.9)
        action = TouchAction(self.driver)
        action.press(x =size['width'] * 0.3,y =size['height'] * 0.3).wait(100).move_to(x=size['width'] * 0.3,y=size['height'] * 0.9).wait(100).release().perform()
        sleep(3)
        print(self.driver.contexts)
        sleep(2)

        # 切换都最顶部的页面
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tencent.mm:id/lj']").click()


