import unittest

from Unittest.utils.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    # '''# 执行方法一：直接跑这个文件中的全部测试用例
    # # unittest.main()
    # #执行方法二： 通过suite
    # '''
    # suite = unittest.TestSuite()
    # suite.addTest(TestUnittest("test_unittest1"))
    # unittest.TextTestRunner().run(suite)

    report_title = 'Unittest用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'data/Deng-Unittest-Report.html'

    test_dir = "./testcases"
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)