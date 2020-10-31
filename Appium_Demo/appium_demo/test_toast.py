from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "io.appium.android.apis"
        desire_caps["appActivity"] = ".view.PopupMenu1"
        desire_caps["noReset"] = "true"  # 这里就避免来每次打开弹出的同意窗口
        desire_caps["skipDeviceInitialization"] = 'true'
        # desire_caps["unicodeKeyBoard"] = "true"  # 输入中文字符
        # 初始化驱动
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        # 设置一个隐形等待，增加代码的健壮性
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast_bar(self):
        '''
        1 - 点击make a pop
        2 - 点击搜索
        3 - 识别toast并判断提示内容是否包含某些文字
        '''

        self.driver.find_element(MobileBy.XPATH,'//android.widget.Button[@content-desc="Make a Popup!"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Search"]').click()
        # toast 无法在页面上被定位，所以这里我们打印page_source来
        # 就可以根据此时此刻的page_source定位出toast来
        print(self.driver.page_source)
        # toast的定位只能通过着两种方法来找
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'Clicked popup')]")