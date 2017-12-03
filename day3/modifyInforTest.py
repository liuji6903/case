#1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")  #进入登录页面
driver.find_element_by_id("username").send_keys("liu")
ActionChains(driver).send_keys(Keys.TAB).send_keys("@WSX3edc").send_keys(Keys.ENTER).perform() #对浏览器按下tab键,也可以对username元素按下tab键,链表必须有明确的结束标志

#2.点击账号设置
driver.find_element_by_link_text("账号设置").click()

#3.点击个人资料
driver.find_element_by_partial_link_text("个人资料").click()

#4.修改个人资料
driver.find_element_by_id("true_name").clear()  #清空元素中原本的内容
driver.find_element_by_id("true_name").send_keys("哈哈哈哈")
driver.find_element_by_css_selector('#xb[value="2"]').click()  #单选按钮用click单击选择,value是唯一的,可以用selector选择value值,若是value不是唯一的,可以用几个属性组合定位,#后面表示ID

#document.getElementById("date").removeAttribute("readonly") JS删除属性
#js = 'document.getElementById("date").removeAttribute("readonly")'
#driver.execute_script(js)

date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")', date)

#driver.find_element_by_id("date").clear()
#driver.find_element_by_id("date").send_keys("2001-11-21")

date.clear()
date.send_keys("1992-01-27")

#用selenium调用JS有两个关键字:(1)arguments[0]
#                               (2)return

#date = driver.execute_script("return document.getElementById('date')")  #date = driver.find_element_by_id("date") 元素定位不到时用return

driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("326516122")
driver.find_element_by_class_name("btn4").click()
time.sleep(3)

#alert弹出框:右键检查不了,可以添加时间等待
# driver.switch_to.alert.dismiss()
driver.switch_to.alert.accept()


