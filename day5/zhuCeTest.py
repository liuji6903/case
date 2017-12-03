import os
from selenium import webdriver
from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    '''注册模块测试用例'''

    # 因为myTestCase已经实现了setUp和tearDown方法,以后不需要在写这两个方法了
    def test_Zhu_Ce(self):
        """打开注册页面的测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        # driver.current_url  # 用来获取当前浏览器的网址
        actual = driver.title  # 用来获取当前浏览器中的标签页的title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"
        base_path = os.path.dirname(__file__)
        path = base_path.replace('day5','report/image/')  #相对路径
        # path = r"C:\Users\51Testing\PycharmProjects\case\day5\report\image\ "
        driver.get_screenshot_as_file(path + "zhuce1.png")  # 截取整个浏览器图片,保存到path路径下
        self.assertEqual(actual,expected)

        print("测试页面打开成功")