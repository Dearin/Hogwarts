import yaml
from selenium.webdriver.common.by import By
from Appium_Demo.frame_demo.Pages.BasePage import BasePage
from Appium_Demo.frame_demo.Pages.MarketPage import MarketPage


class MainPage(BasePage):

    def goto_market(self):

        #第三版，封装来yaml的方法后，再来简介的调用
        path = '../yamls/main.yaml'
        func_name = 'goto_market'
        self.yaml_parse(path,func_name)
        return MarketPage(self.driver)

        # 第二版，增加yaml读取
        # 这里我们优化以下，使用yaml来进行测试步骤的驱动
        # with open('../yamls/main.yaml') as f:
        #     data = yaml.safe_load(f)
        # steps = data['goto_market']
        # print(steps)
        # for step in steps:
        #     if 'click' in step['action']:
        #         self.find(step['by'], step['locator']).click()
        # return MarketPage(self.driver)

        # 第一版没有进行任何驱动
        # # 这里我们来模拟一个黑名单：点击登陆的图标，就会产生弹窗，影响我们正常的流程
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # # 点击"行情"按钮，跳转值行情页面
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
