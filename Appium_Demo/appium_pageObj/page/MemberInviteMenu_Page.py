'''
添加成员页面
'''
from appium.webdriver.common.mobileby import MobileBy
from Appium_Demo.appium_pageObj.page.BasePage import BasePage


class MemberInviteMenuPage(BasePage):

    def addMember_Manual(self):
        # 点击手动邀请成员：
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")

        from Appium_Demo.appium_pageObj.page.ContactAdd_Page import ContactAdd
        return ContactAdd(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result