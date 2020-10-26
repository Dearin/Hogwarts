import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChain:

    def  setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def  teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_action_click(self):
        url = "http://www.sahitest.com/demo/clicks.htm"
        self.driver.get(url)
        action = ActionChains(self.driver)
       # click_element = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        click_element = self.driver.find_element_by_xpath('//input[@value="click me"]')
        right_click_element = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        dbl_click_element = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        action.click(click_element)
        action.context_click(right_click_element)
        action.double_click(dbl_click_element)
        sleep(2)
        action.perform()
        sleep(2)

    @pytest.mark.skip
    def  test_movetoelement(self):
        url = "https://www.baidu.com/"
        self.driver.get(url)
        action = ActionChains(self.driver)
        move_to_element = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action.move_to_element(move_to_element)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_draganddrop(self):
        url = "http://www.sahitest.com/demo/dragDropMooTools.htm"
        self.driver.get(url)
        action = ActionChains(self.driver)

        drag_element = self.driver.find_element_by_xpath('//*[@id="dragger"]')
        drop_element = self.driver.find_element_by_xpath('/html/body/div[3]')
       # action.drag_and_drop(drag_element, drop_element)
       # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_keys(self):
        url = "http://www.sahitest.com/demo/label.htm"
        self.driver.get(url)
        action = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        # 在输入框中输入光标，才能输入数据
        element.click()
        element.send_keys("username")
        element.send_keys(Keys.SPACE)
        element.send_keys("test")
        element.send_keys(Keys.BACK_SPACE)
        sleep(3)





