from selenium.webdriver import ActionChains

from Selenium.test_selenium_file.base import Base
from time import sleep


class TestAlert(Base):

    def test_alert(self):
        url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
        self.driver.get(url)

        #需要触发页面的alert事件，所以需要drag_and_drop
        self.driver.switch_to.frame('iframeResult')
        drag_ele = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        drop_ele = self.driver.find_element_by_xpath('//*[@id="droppable"]')

        #拖动契合
        print(drag_ele.text)
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_ele,drop_ele).perform()
        sleep(2)

        #出现弹窗，进行操作
          # 切换到alert组件上,accept表示点击确认，接收弹窗的数据
          # dismiss则为解散alert
        self.driver.switch_to.alert.accept()
        sleep(2)

        # 解除弹窗后，由拖拽部分的iframe切换出来
        self.driver.switch_to.default_content()
        # 点击运行 - 这里通过js的命令来获取一下
        print(self.driver.execute_script("return document.getElementById('submitBTN')"))

        # 点击
        self.driver.find_element_by_xpath('//*[@id="submitBTN"]').click()
        sleep(2)




