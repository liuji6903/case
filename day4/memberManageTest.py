import unittest
import ddt
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from day4.readCsv2 import read

# 1.装饰这个类
@ddt.ddt
class MemberManageTest(unittest.TestCase):
    # 2.调用之前写好的read方法,获取配置文件中的数据
    member_info = read("member_info.csv")

    # 在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前,只执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("登录测试")
        driver = self.driver
        driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()

    # *表示把集合中的所有元素拆开一个一个写
    @ddt.data(*member_info) # 4.ddt.data 测试数据来源于read方法,再把数据表中的每一行传入方法,在方法中增加一个参数row
    def test_b_add_member(self,row):
        print("添加会员")
        driver = self.driver

        # 每组测试数据就是一条测试用例,每条测试用例都应该是独立的,不能因为上一条测试用例失败导致下一组数据不能被正常执行,所以不推荐for循环
        # 应该用ddt装饰器,去修饰这个方法,达到每条测试数据独立执行的目的
        # data driver test 数据驱动测试,将ddt解压到selenium解压的路径下

        # 3.注释掉for循环,改变代码的缩进,用快捷键shift+tab
        # for row in read("member_info.csv"):
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        iframe_css = "#mainFrame"
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        # driver.find_element_by_css_selector("[value='"+row[2]+"']").click()
        driver.find_element_by_css_selector("[value='{0}']".format(row[2])).click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()

        # 断言:assert,断言是框架提供的,要想调用断言,需要加上self. 因为测试用例类继承了框架中的TestCase类,也继承了这个类中的断言,执行测试用例之后页面上实际显示的结果与期望结果是否一致,类似于if... else... 语句,是用来做判断的
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        expected = row[0]
        # if actual == expected:
        #     print("测试通过")
        # else:
        #     print("测试失败")
        # 断言有几个特点:简短,只关注于错误的测试用例,只有断言出错的时候才会打印信息,断言报错时后面的代码将不会继续执行


       # driver.switch_to.parent_frame()  # 切换到父框架
        driver.switch_to.default_content()  #切换到根节点
        self.assertEqual(actual,expected)




if __name__ == '__main__':
    unittest.main()
