from Selenium.test_selenium_frame import Base
from time import sleep

class TestFrame(Base):

    def test_frames(self):
        url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
        self.driver.get(url)

        # 首先要进入frame
        self.driver.switch_to.frame('iframeResult')
        drag_ele = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        drop_ele = self.driver.find_element_by_xpath('//*[@id="droppable"]')

        print(drag_ele.text)
        # 这里注释的话，测试页面会出现弹窗，导致最后一句失败被阻塞
        # action = ActionChains(self.driver)
        # action.drag_and_drop(drag_ele,drop_ele).perform()
        sleep(2)
        # 再回到正常的页面中

        self.driver.switch_to.default_content()
        # 打印正常页面中的
        print(self.driver.find_element_by_xpath('//*[@id="submitBTN"]').text)
        sleep(2)


