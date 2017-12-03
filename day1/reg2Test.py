#1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()

#2.打开商城主页
driver.get("http://localhost/index.php")

#3.点击注册链接
#  三种定位元素的方法: ID ,Name ,Class
#  第四种定位元素的方法:链接的文本信息
driver.find_element_by_link_text("注册").click()

#4.输入用户信息
#在搜索框里输入liu2
#driver.find_element_by_name("keyword").send_keys("liu2")
#窗口切换:把selenium 切换到新的窗口工作
newWindow = driver.current_window_handle  #浏览器当前窗口的句柄(第一次打开的窗口)
allWindow = driver.window_handles  #浏览器中所有额窗口句柄
#for关键字(类型名 变量名 : 数组) {} Java中的for循环
#item表示allWindow中的一个元素,每次循环取一个值,循环结束,allWindow中的每个元素都会遍历一次
for item in allWindow:
    if item == newWindow:
        #pass  不关闭窗口
        driver.close()  #关闭当前标签,关闭第一个窗口
    else:  #这种情况,item就是我们要找的窗口,切换到第二个窗口
        driver.switch_to.window(item)

driver.find_element_by_name("username").send_keys("liu3")
driver.find_element_by_name("password").send_keys("#EDC4rfv")
driver.find_element_by_name("userpassword2").send_keys("#EDC4rfv")
driver.find_element_by_name("mobile_phone").send_keys("18512511243")
driver.find_element_by_name("email").send_keys("000@163.com")

#5.点击提交按钮
driver.find_element_by_class_name("reg_btn").click()
