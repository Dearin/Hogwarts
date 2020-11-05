import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestChromeCookie:
    '''1/首先复用浏览器'''
    def setup_method(self, method):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_get_cookie(self):
        '''
        1- get_cookie()可以获取当前打开页面的cookie
        2 - add_cookie()可以注入需要打开的页面
        :return:
        '''
        # cookies = self.driver.get_cookies()
        # 将cookie注入到当前的driver后，停止复用浏览器
        cookies =[
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851102598061'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851102598061'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324941168277'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'u-sIu1a-7Bdspi-3-XFClWjJA7uH3VnsVsVoap18b_0lCBrZLAehZEwMJCbPANfr'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5226507'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'U7JvUxMkaqfZoP8qnN_EhUMdXkoyapY8vKIx03TVsL8e4MflH5D9i8rbpfBgl5T_8Xqlk0aaD7shNPZ9Pb_4Xv3YcXqAOc2R7j-kjnBWPwhHCnZ3U4YcQxJ9G2GgmAhy2YOUbMr-5YnMLlNfHyrE4O8hZAeu_G7uLahecbFFpWwvn18E7s9_nUkw278sLOnZAczXX81TKy1oEjcA0E6Jxoj9Uk74re-cVi6w0co2gOoMO5J6OrfSFr84WP1J2QHusKBad-2EbrY11zSxScQD-A'},
        {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '86be2e2234e0950effc2a19b13bcf8a2d6ea4a613f1e203d198d4721a08b0cfb'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},
        {'domain': '.work.weixin.qq.com', 'expiry': 1636097486, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603527144,1603609519,1604561487'},
        {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8777372332'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
        {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'UW6U4p12Eg'},
        {'domain': '.qq.com', 'expiry': 1606202139, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '987221507'},
        {'domain': '.qq.com', 'expiry': 1667633520, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2036018980.1603527152'},
        {'domain': '.work.weixin.qq.com', 'expiry': 1635063134, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
        {'domain': '.work.weixin.qq.com', 'expiry': 1607153727, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604561487'},
        {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '14653739181885304'},
        {'domain': '.qq.com', 'expiry': 1604647920, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1284970687.1604561491'},
        {'domain': 'work.weixin.qq.com', 'expiry': 1604593021, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '6kav36k'},
        {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5238845440'}
        ]
        # 添加cookie前进行访问
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                # 防止cookie过期
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 添加cookie前进行访问，查看不同的效果
        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)


    def test_shelve(self):
        '''
        shelve是一个简单的数据存储方案，类似key-value数据库，可以很方便的保存python对象，其内部是通过pickle协议来实现数据序列化。
        shelve只有一个open()函数，这个函数用于打开指定的文件（一个持久的字典），然后返回一个shelf对象。
        shelf是一种持久的、类似字典的对象

        格式为：shelve.open（filename，flag）
        filename：文件名；
        flag：打开数据存储文件的格式；
            'r'	以只读模式打开一个已经存在的数据存储文件
            'w'	以读写模式打开一个已经存在的数据存储文件
            'c'	以读写模式打开一个数据存储文件，如果不存在则创建
            'n'	总是创建一个新的、空数据存储文件，并以读写模式打开
        '''
        # 保存进入db后就暂时初始化shelve数据库这部分的代码了
        db = shelve.open('cookies')
        # 下面是初始化的操作
        # db['cookie']=cookies
        # db.close()

        # 打开页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = db['cookie']
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(3)


