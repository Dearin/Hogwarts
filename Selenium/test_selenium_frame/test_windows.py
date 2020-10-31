
from time import sleep

from Selenium.test_selenium_frame.base import Base

class TestWindows(Base):

    def test_windows(self):
        '''
        进入首页，点击右上角登陆，弹出登陆弹窗
        点击弹窗中的立即注册，跳转至注册页面，输入注册信息后
        返回上一页面，点击登陆 - 用户登陆

        '''
        url = "https://www.baidu.com"
        self.driver.get(url)
        sleep(1)
        login_ele = self.driver.find_element_by_xpath('//*[@id="u1"]/a')
        login_ele.click()
        print(self.driver.current_window_handle)
        sleep(2)

       # 定位到立即注册，并点击跳转
        register_ele = self.driver.find_element_by_link_text("立即注册")
        register_ele.click()
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        windows = self.driver.window_handles
        sleep(3)

       # 输入相关信息，强制等待3s
        self.driver.switch_to_window(windows[-1])
        name_ele = self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]')
        phonenum_ele = self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]')
        name_ele.send_keys("username")
        phonenum_ele.send_keys("13400000001")
        sleep(3)

        #返回首页
        self.driver.switch_to_window(windows[0])
        sleep(2)
        # 选择用户名登陆
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(2)








