import time  #导入time包

from selenium import webdriver
from selenium.webdriver.support.select import Select  #导入select

driver = webdriver.Chrome()

#隐式等待,一经设置,对后面所有的语句都有效果,所以在创建浏览器时设置一次就可以了
driver.implicitly_wait(30)  #隐式等待
driver.maximize_window()  #窗口最大化

#45版本以下的火狐不需要驱动文件,46开始的火狐需要驱动文件
#driver = webdriver.Ie()  IE需要驱动文件

driver.get("http://localhost/")

#登录之前删除target属性(用selenium 的定位方式替换Javascript 的定位方式,用arguments 关键字)
login = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login)
login.click()
driver.find_element_by_id("username").send_keys("liu")
driver.find_element_by_id("password").send_keys("@WSX3edc")

#提交submit():用于提交form表单,form是html中的一个元素,form 表单的任何子孙节点都可以调用submit()方法提交表单
driver.find_element_by_id("username").submit()

#设置time.sleep(),导入time包,按住Alt+Enter 自动导包
#time.sleep(5) 最好不用这个方法,几秒都不好
#应该用隐式等待,会自动判断网页是否加载完毕,当加载完毕立刻执行后续的操作
#设置一个最大时间,不能让程序无限等待,一般设置30秒

driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
#driver.find_element_by_name("keyword").submit()

iphoneLink= "div.shop_01-imgbox > a" # css selector 中的内容越短越好,方便维护,保证代码的健壮性,开发一旦修改页面的节点时,那么元素会定位失败
#iphoneLink = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a"
iphone = driver.find_element_by_css_selector(iphoneLink)

driver.execute_script("arguments[0].removeAttribute('target')",iphone)

iphone.click()

#用for循环实现页面转换
#newWindow = driver.current_window_handle  #浏览器当前窗口的句柄(第一次打开的窗口)
#allWindow = driver.window_handles  #浏览器中所有额窗口句柄
#for item in allWindow :
#    if item == newWindow:
#        driver.close()
#    else:
#        driver.switch_to.window(item)

driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()

driver.find_element_by_class_name("add-address").click()

driver.find_element_by_name("address[address_name]").send_keys("liu")
#driver.find_element_by_xpath('//*[@id="add-new-address"]/div[1]/input').send_keys("liu")   定位Xprth

driver.find_element_by_name("address[mobile]").send_keys("13516220000")

#(1)选择下拉框:css selector
#driver.find_element_by_id("add-new-area-select").find_element_by_css_selector("[value='230000']").click()  从父节点找到子节点,可以简写成下面的代码
#driver.find_element_by_css_selector("[value='230000']").click()
#driver.find_element_by_css_selector("[value='230500']").click()
#driver.find_element_by_css_selector("[value='230505']").click()

#(2)下拉框:select类,来自于网页中下拉框的标签名,select类里封装了针对下拉框的操作方法,只适用于select标签
#find element 用唯一条件查找页面上的一个元素;find elements 用一类条件查找页面上所有符合条件的元素(用来做爬虫的主要方法)
sheng = driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_value('230000')
#定位第二个下拉框
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)
#定位第三个下拉框
xian = driver.find_elements_by_tag_name("select")[2]
Select(xian).select_by_visible_text("昂昂溪区")  #select 是标签名


driver.find_element_by_name("address[address]").send_keys("ddddddd")
driver.find_element_by_name("address[zipcode]").send_keys("100000")
driver.find_element_by_class_name("aui_state_highlight").click()














