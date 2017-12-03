from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):  # 构造方法的作用:实例化LoginPage对象的时候,需要把driver作为参数穿进去,便于别的方法使用driver
        # 实例化对象的时候必须要调用构造方法(初始化方法)
        self.driver = driver

    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"

    # 小括号是元祖,里面有两个元素,第一个个控件的定位方式,第二个是控件的具体的值
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_button_click = (By.CLASS_NAME,"login_btn")

    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        self.driver.find_element(*self.username_input_loc).send_keys(username)  # *的作用: 把一个元组中的元素分别传入方法参数中;前面加一个星号表示传入的是元组中的两个元素

    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_click).click()

