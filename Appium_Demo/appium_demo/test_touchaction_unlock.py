
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestUnlock:

    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "cn.kmob.screenfingermovelock"
        desire_caps["appActivity"] = "com.samsung.ui.MainActivity"
        desire_caps["noReset"] = "true"  # 这里就避免来每次打开弹出的同意窗口
        desire_caps["skipDeviceInitialization"] = 'true'
        desire_caps["unicodeKeyBoard"] = "true"  # 输入中文字符
        # 初始化驱动
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        # 设置一个隐形等待，增加代码的健壮性
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        action = TouchAction(self.driver)
        action.press(x=296,y=198).wait(100).move_to(x=596,y=198).wait(100).move_to(x=985,y=198).wait(100).move_to(x=985,y=683).wait(100).move_to(x=985,y=1087).wait(100).release().perform()
