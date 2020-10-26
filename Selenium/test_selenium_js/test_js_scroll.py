from Selenium.test_selenium_js.base import Base
from time import sleep
import pytest

class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        url = "https://www.baidu.com"
        self.driver.get(url)

        # 首先进行搜索，在input中输入关键词并点击查询
        input_ele = self.driver.find_element_by_xpath('//*[@id="kw"]')

        input_ele.send_keys("Selenium测试")
        sleep(1)
        search_ele = self.driver.execute_script('return document.getElementById("su")')
        # search_ele = self.driver.find_element_by_xpath('//*[@id="su"]')
        search_ele.click()
        sleep(2)

        # 展示查询结果，使用js脚本滑动页面底部
        self.driver.execute_script('document.documentElement.scrollTop=100000')
        sleep(2)
        # 获取下一页定位,并点击
        next_ele = self.driver.find_element_by_xpath('//*[@id="page"]//a[10]')
        next_ele.click()
        sleep(2)

        # # 我们可以合并命令
        # for code in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))

        # 或者组合在一起

        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))



    def test_datettime(self):
        url = "https://www.12306.cn/index/"
        self.driver.get(url)

        #获得时间控件所在的位置
        self.driver.execute_script("date=document.getElementById('train_date');date.removeAttribute('readonly')")
        #给value赋值
        self.driver.execute_script("document.getElementById('train_date').value = ('2020-11-01')")
        #检查时间控件是否修改
        print(self.driver.execute_script('return document.getElementById("train_date").value'))

        sleep(3)


