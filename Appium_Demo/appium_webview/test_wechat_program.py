from appium import webdriver
from time import sleep

from appium.webdriver.common.mobileby import MobileBy


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
        desire_caps["chromedriverExecutableDir"] = "/Users/deng/Documents/driver/chromedriver"  # 输入中文字符

       # 将chromeoption传递给chromedriver
        desire_caps["chromeOptions"] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }
        # 这里的端口不能设置成5038
        desire_caps["adbPort"] = 5037
        # 初始化驱动
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)
        # 设置一个隐形等待，增加代码的健壮性
        self.driver.implicitly_wait(5)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

        # self.enter_micro_program()
        # print(self.driver.contexts)

    def teardown(self):
        self.driver.quit()

    def test_wechat_xueqiu(self):
        # 原生测试：滑动页面，展示出小程序搜索位置
        # 输入需要查询的小程序名称进行查找
        # 点击所需要的小程序，进入程序页面
        # 小程序的测试：
        # 在小程序中进行搜索和跳转
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.3,size['height'] * 0.5,size['width'] * 0.3,size['height'] * 0.9)
        sleep(3)