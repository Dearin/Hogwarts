'''
通许录界面，进行一些用户编辑操作，比如：
1/添加成员
2/进入信息详情页面
'''
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Appium_Demo.appium_pageObj.page.BasePage import BasePage
from Appium_Demo.appium_pageObj.page.ContactDetailBriefInfoProfile_Page import ContactDetailBriefInfoProfile
from Appium_Demo.appium_pageObj.page.MemberInviteMenu_Page import MemberInviteMenuPage


class AdressListPage(BasePage):
    # add_memver_element =(MobileBy.XPATH,'//*[@text="添加成员"]')
    # 添加的人数较多时，会出现添加按钮不在一个页面上，所以要选择滚动页面查找元素
    def click_addMember(self):
        # 找到"添加成员"按钮并点击
        # self.find_and_click()
        self.find_by_scroll("添加成员").click()
        print("找到啦~")
        return MemberInviteMenuPage(self.driver)

    def scroll_to_find_member(self,name):
        # 滚动查找目标人员并点击进入详情页面
        try:
            self.find_by_scroll(name).click()
        except Exception:
            print("无法查找到该页面元素")
            return False
        return ContactDetailBriefInfoProfile(self.driver)

    def find_contact(self,name):
        locator = (MobileBy.XPATH,f'//*[@text="{name}"]')
        result = WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator))
        return result