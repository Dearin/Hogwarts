from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCheckin:

    def setup(self):
        # 进行一些初始化操作
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "com.tencent.wework"
        desire_caps["appActivity"] = ".launch.WwMainActivity"
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


    def test_wechat_checkin(self):
        # 找到工作台
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/dqn" and @text="工作台"]').click()
        # 滑动屏幕，找到打卡元素
        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        # 切换到"外出打卡"
        # WaitForIdleTimeout这个作用是哈？
        # ?
        self.driver.update_settings({"waitForIdleTimeout": 0})
        a_locator = (MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/ghc" and @text="外出打卡"]')
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(a_locator))
        self.driver.find_element(*a_locator).click()

        #点击外出打卡
        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click()
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)




