import unittest
import time
from day5.myTestCase import MyTestCase
from day6.data_base.connectDB import connDb


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("aaaa")
        driver.find_element_by_name("password").send_keys("@WSX3edc")
        driver.find_element_by_name("userpassword2").send_keys("@WSX3edc")
        driver.find_element_by_name("mobile_phone").send_keys("13516224562")
        driver.find_element_by_name("email").send_keys("aaaa@126.com")
        driver.find_element_by_class_name("reg_btn").click()


        # 检查数据库中的新注册的用户名和我们输入的是否一致
        expected = "aaaa"
        time.sleep(3)
        actual = connDb()[1]  # 返回结果是一个元组,需要用索引找到想要的
        self.assertEqual(expected,actual)
        print(connDb()[1])