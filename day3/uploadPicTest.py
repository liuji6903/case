#1.登录
#验证码:使用万能验证码或者屏蔽验证码,还可以通过读取cookie登录,勾选复选框免登陆,或者在登陆之前加时间等待
#网站开发设计模式:MVC
#万能验证码:1234  D:\phpfind\WWW\appliaction\Controller\Admin\PublicController.class.php
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(30)
#driver.maximize_window()
driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()

#2.商品管理
driver.find_element_by_link_text("商品管理").click()

#3.添加商品
driver.find_element_by_link_text("添加商品").click()

#4.商品名称
#特殊的网页(左边或者上边有一个导航条),在一个页面嵌套多个页面,"商品管理"和"添加商品"属于根节点网页,"商品名称"属于frame框架里的子网页,需要切换网页
driver.switch_to.frame("mainFrame")  #切换网页
driver.find_element_by_name("name").send_keys("xiaomi5")

#5.商品分类
#fenlei1 = driver .find_element_by_class_name("sl")
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
driver.find_element_by_id("7").click()
#driver.find_element_by_link_text("选择当前分类").click()
#driver.find_element_by_id("3").click()
#driver.find_element_by_link_text("选择当前分类").click()
#双击:被封装到ActionChains这个类中, 以perform结束
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()

#6.商品品牌
pinpai = driver.find_element_by_tag_name("select")
Select(pinpai).select_by_visible_text("苹果 (Apple)")
#driver.find_element_by_css_selector("value='1'").click()
#brand = driver.find_element_by_name("brand_id")
#Select(brand).select_by_index(1)

#7.点击商品图册,上传图片
driver.find_element_by_link_text("商品图册").click()
time.sleep(3)
# driver.find_element_by_css_selector("#filePicker label").click()  #定位父元素不行,找到父元素的上一级爷爷的ID,有些页面控件是在JS在页面加载之后生成的,需要加一个时间等待,需要time.sleep()提高程序的稳定性
#真正负责上传文件的页面元素是<input type="file"...所以直接操作这个控件

driver.find_element_by_name("file").send_keys("D:/upload.png")
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()  #通过三个class进行定位
time.sleep(3)
driver.switch_to.alert.accept()
driver.find_element_by_class_name("button_search").click()

#操作滚动条
#range 是区间,默认从0开始到9结束
# ac = ActionChains(driver)
# for i in range(10):
#     ac.send_keys(Keys.ARROW_DOWN)
# ac.perform()
driver.execute_script("window.scrollTo(200,100)")

#8.点击提交
#driver.find_element_by_class_name("button_search").click()

