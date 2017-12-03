import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):

    # 这个测试用例维护起来比较困难,可读性比较差
    # def test_login(self):
    #
    #     # 1.打开网页
    #     driver = self.driver
    #     driver.get("http://localhost/index.php?m=user&c=public&a=login")
    #
    #     # 2.输入用户名
    #     driver.find_element(By.ID,"username").send_keys("liuji")
    #
    #     # 3.输入密码
    #     driver.find_element(By.ID,"password").send_keys("@WSX3edc")
    #
    #     # 4.点击登录按钮
    #     driver.find_element(By.CLASS_NAME,"login_btn").click()
    #
    #     # 5.验证是否跳转到管理中心页面
    #     expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
    #     time.sleep(5)
    #     actual = driver.title
    #     self.assertIn(expected,actual)

    def test_login(self):
        lp = LoginPage(self.driver)  # 实例化一个登录页面的类
        lp.open()

        lp.input_username("liuji")

        lp.input_password("@WSX3edc")

        lp.click_login_button()

        pcp = PersonalCenterPage(self.driver)  # 实例化一个会员中心页面的类
        time.sleep(5)
        self.assertEqual(pcp.title,self.driver.title)



        # 元素的定位是属性,元素的操作是方法
