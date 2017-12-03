from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/index.php")
driver.find_element_by_link_text("登录").click()
newWindow = driver.current_window_handle  #浏览器当前窗口的句柄(第一次打开的窗口)
allWindow = driver.window_handles  #浏览器中所有额窗口句柄
for item in allWindow :
    if item == newWindow:
        pass
        #driver.close()
    else :
        driver.switch_to.window(item)

driver.find_element_by_id("username").send_keys("liu")
driver.find_element_by_id("password").send_keys("@WSX3edc")
driver.find_element_by_class_name("login_btn").click()
