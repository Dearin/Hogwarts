
"""
app.py模块
主要的操作包括：
启动/停止app,重启app,进入到首页
"""
from appium import webdriver

from Appium_Demo.appium_pageObj.page.BasePage import BasePage
from Appium_Demo.appium_pageObj.page.Main_page import MainPage


class App_Index(BasePage):

      def start_app(self):
          if self.driver == None:
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
              self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
              # 设置一个隐形等待，增加代码的健壮性
              self.driver.implicitly_wait(5)
          else:
              self.driver.launch_app()
              # self.driver.start_activity(package,activity)

          return self

      def stop_app(self):
          self.driver.quit()

      def restart(self):
          self.driver.close_app()
          self.driver.launch_app()


      def goto_main(self)->MainPage:
          # 进入到首页
          return MainPage(self.driver)

