import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Web.wework_demo.Pages.BasePage import BasePage


class MemberList_Add(BasePage):

    def goto_add_member(self):
        '''点击人员添加按钮：
        1- 首先设置一个显性等待，检查页面的元素是否加载完成
        2- 元素加载完成后，进行点击跳转
        '''
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        from Web.wework_demo.Pages.AddMember_Page import AddMember
        return AddMember(self.driver)

    def get_member(self, value):
        '''新增用户后需要查询到是否新增成功
           由于企业当前的人数过多，在web上会产生分页，所以需要处理分页查询（不通过接口）
        '''
        # 验证联系人添加成功 - 未产生分页
        # self.driver.refresh()
        # total_list = []
        # # while True:
        #     # 第一个td是列表中的复选框，第二个td才是用户名
        # contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # # title属性中存放的是用户的名字全部取出来
        # titlelist = [element.get_attribute("title") for element in contactlist]
        # total_list = total_list + titlelist
        # return total_list

        '''产生分页的处理如下'''
        # 第一步；首先处理当前页的数据以及定义数组
        total_list = []

        # 获取当前页面的用户姓名,需要去循环操作
        while True:
            # 这里存的只是每一个查询出来的对象！
            memberlist =   self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
            # 需要去针对上一步的对象，去获取它的title属性,并存放在list中
            titlelist = [element.get_attribute("title") for element in memberlist]
            total_list = total_list + titlelist
            # 判断一下当前的集合中是否存在需要查找的用户名
            print(f'当前的列表是：{total_list}')
            if value in titlelist:
                break
            # 如果当前的列表中不存在，则将titlelist 合并到totallist中：
            # 并开始处理下一页的数据：
            # 获取分页信息
            result: str = self.driver.find_element(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            # 第二个参数为 1，代表分割1次
            num, total = result.split('/',1)
            print(f'总页数是：{total},当前页数为：{num}')
            if int(num) == int(total):
                print("我看看我跳出来循环没有")
                break  # 不在点击下一页
            else:
                # 点击下一页
                self.driver.find_element(By.CSS_SELECTOR,'.ww_commonImg_PageNavArrowRightNormal').click()
        # 跳出循环则直接返回total_list

        return total_list

