from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from Web.wework_demo.Pages.BasePage import BasePage
from Web.wework_demo.Pages.MemberList_Add_Page import MemberList_Add


class MainPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_MemberListAdd(self):
        # 点击 【通讯录】，进入到通讯录页面
        self.find_and_click(By.CSS_SELECTOR, "#menu_contacts")
        return MemberList_Add(self.driver)


