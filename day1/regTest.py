from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("liu1")
driver.find_element_by_name("password").send_keys("#EDC4rfv")
driver.find_element_by_name("userpassword2").send_keys("#EDC4rfv")
driver.find_element_by_name("mobile_phone").send_keys("18512511251")
driver.find_element_by_name("email").send_keys("0@163.com")
driver.find_element_by_class_name("reg_btn").click()
