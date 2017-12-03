import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class DengluTest(unittest.TestCase):
    '''登录模块测试用例'''  # 文档注释,单引号双引号都可以
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()

    def test_denglu(self):
        """登陆测试正常情况测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("liuji")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("@WSX3edc").send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        print("用户名:liuji 登陆成功")  # 可以打印在测试报告中

