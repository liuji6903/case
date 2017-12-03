#JavaScript是一门独立的语言
#学好selenium: (1)元素的定位(ID ,Name,Class,link text,css selector,Xpath,partial_link_text,tag_name),Link text 必须是链接必须是<a>标签必须是文本,partial_link_text使用链接的一部分文本定位,css selector可以用元素的任何属性定位
#               (2)元素的操作(左键单击Click,发送按键send_keys等)
#                (3)第九种定位元素的方式JavaScript(实现窗口切换)( 删除target属性)(不会跳转到新页)


#1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()  #窗口最大化
driver.get("http://localhost/index.php")

#怎么在python执行JavaScript语言 ,删除属性,实现当前页面执行,代替for循环实现窗口切换
js = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)


#2.点击登录链接
driver.find_element_by_link_text("登录").click()

#3.输入用户名和密码
driver.find_element_by_id("username").send_keys("liu")
driver.find_element_by_id("password").send_keys("@WSX3edc")


#定位css selector
#username_input = "#username"
#driver.find_element_by_css_selector(username_input).send_keys("liu")


#4.点击登录按钮
driver.find_element_by_class_name("login_btn").click()

#5.退出浏览器
driver.quit()
