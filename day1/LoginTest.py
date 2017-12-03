#1.打开浏览器
from selenium import webdriver
#  导入  webdriver (网络驱动),用代码来操纵浏览器
#  (1)不需加分号,(2)chrome 后必须加括号,(3)settings - editor - color and font - font 修改字体大小
driver = webdriver.Chrome()
#  打开chrome浏览器

#2.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")

#3.输入用户名,首先寻找用户名的输入框,然后在输入框中输入liu
#  网页上所有可见的都属于element,比如,link ,按钮 ,下拉框 ...
#  在叫driver 的浏览器上,寻找一个网页元素,如果id=username,并且向页面元素中发送liu
driver.find_element_by_id("username").send_keys("liu")

#4.输入密码
driver.find_element_by_id("password").send_keys("@WSX3edc")

#5.点击登录按钮
driver.find_element_by_class_name("login_btn").click()


