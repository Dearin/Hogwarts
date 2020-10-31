from appium import webdriver

class TestBrowser:

    def setup(self):
        desire_cap = {}
        desire_cap["platformName"] = "android"
        desire_cap["deviceName"] = "emulator-5554"
        desire_cap["noReset"] = "true"
        desire_cap["browser"] = "Chrome"
        desire_cap["appWaitForLaunch"]="false"
        desire_cap["appPackage"] = "com.android.chrome"
        desire_cap["appActivity"] = "org.chromium.chrome.browser.ChromeTabbedActivity"
    # 不知道为什么，无法向老师视频里那样直接发送get请求去获取网站信息？这里就只有去通过之前的方法了

    # 初始化driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()


    def test_browser(self):
        self.driver.get("http://m.baidu.com")
