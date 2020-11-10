
'''
1- 装饰器需要先传入需要增强的方法

'''
import allure


def handle_black(func):
    '''需要传递函数进来：
     def find(self, by, locator=None):
    '''
    def wrapper(*args, **kwargs):
        '''需要处理的逻辑就是异常捕捉和处理
           由于是self方法本身具备对应的方法，这里先讲self提取出来，是传递的第一个参数
        '''

        from Appium_Demo.frame_demo.Pages.BasePage import BasePage
        instance: BasePage = args[0]
        try:
            # 调用BasePage中的find函数
            result = func(*args, **kwargs)
            instance.error_num = 0
            return result
        except Exception as e:
            # 遇到异常，进行截图：
            instance.driver.save_screenshot('../Datas/error.png')
            # 读取文件，并传递到allure的日报中
            with open('../Datas/error.png','rb') as f:
                error_page_screenshot = f.read()
            allure.attach(error_page_screenshot,attachment_type=allure.attachment_type.PNG)
            # 设置一个最大的查找次数，避免一直查找
            if instance.error_num > instance.max_num:
                raise e
            instance.error_num += 1
            # 如果找不到元素，则遍历黑名单中的元素进行点击
            for black_ele in instance.black_list:
                # 对元素在页面中进行查找
                ele = instance.driver.find_elements(*black_ele)
                # 如果能查找出来元素，则对元素进行操作;注意ele存放的是一个数组[()]，数组第一个为对应的元素
                if len(ele) > 0:
                    ele[0].click()
                    # 关闭掉弹窗后，再次查找原先的元素,这里不应该return find函数来
                    # 其实这一步还没有很懂为啥？
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper



