import logging

from selenium.webdriver.common.by import By

from Web.wework_demo.Pages.BasePage import BasePage


class AddMember(BasePage):
    '''进行添加联系人的实际操作'''

    def add_member(self, name, account, phonenum):
       # 设置用户名
       self.find(By.XPATH,'//*[@id="username"]').send_keys(name)
       # 设置账号，和name保持一直
       self.find(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys(account)
       # 设置电话号码
       self.find(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys(phonenum)
       # 点击保存按钮
       self.find(By.CSS_SELECTOR, ".js_btn_save").click()

       checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
       self.wait_for_click(checkbox)
       from Web.wework_demo.Pages.MemberList_Add_Page import MemberList_Add
       return MemberList_Add(self.driver)





