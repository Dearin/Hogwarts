from Selenium.test_selenium_file.base import Base
from time import sleep

class TestFile(Base):

    def test_file(self):
        url = "https://image.baidu.com/"
        self.driver.get(url)
        sleep(2)

        # 获取上传图片的元素定位，并点击跳转
        pic_ele = self.driver.find_element_by_xpath('//*[@id="sttb"]')
        pic_ele.click()

        # 出现上传图片的标签，使用send_keys发送图片位置到input框中
        input_ele = self.driver.find_element_by_xpath('//*[@id="stuurl"]')
        input_ele.send_keys("/Users/deng/Hogwarts/test_selenium_file/data/SBK40fdKbAg.jpg")
        sleep(3)
