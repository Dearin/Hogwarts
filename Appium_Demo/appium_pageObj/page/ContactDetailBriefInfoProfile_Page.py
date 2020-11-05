
'''
成员个人信息页，主要操作为：
1/编辑成员
2/发短信和通话
3/邀请进入企业
'''
from appium.webdriver.common.mobileby import MobileBy

from Appium_Demo.appium_pageObj.page.BasePage import BasePage
from Appium_Demo.appium_pageObj.page.ContactDetailSetting_Page import ContactDetailSetting


class ContactDetailBriefInfoProfile(BasePage):

    def enter_detail_setting(self):
        '''点击右上角编辑图标，进入用户编辑页'''
        self.find_and_click(MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.tencent.wework:id/guk"]')
        return ContactDetailSetting(self.driver)

    def set_Remarks(self):
        pass

    def invite_to_join(self):
        pass

    def send_message(self):
        pass
