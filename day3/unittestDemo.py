#测试框架:组织和执行测试用例
#导入unittest框架
import unittest
#Java中类名和文件名的关系,public的类名和文件名一样
#python中的可以一样,但是推荐:文件名首字母小写,类名首字母大写,剩下一样
#继承unittest中的父类:python中的继承直接用小括号表示
#我们在unittestDemo中编写测试用例

class UnittestDemo(unittest.TestCase):

    #重写父类中的方法(setUp和tearDowm)
    def setUp(self):   #def是方法的关键字,setUp是创建,类似于手动测试中的预置条件
        print("这个方法将会在测试用例执行前先执行")

    def tearDown(self):
        print("这个方法将会在测试用例方法之后执行")

    #编写测试用例方法
    #只有以test开头命名的方法才是测试用例方法,测试用例方法可以直接被运行,普通方法不能直接被运行,只有被调用才能被执行
    def test_log_in(self):
        print("登录测试用例")
        self.reg()

    def reg(self):
        print("注册测试用例")

    def test_search(self):
        print("搜索测试用例")

if __name__ == '__main__':   #python内置变量,如果直接执行这个文件那么就会执行下面的语句,否则执行其他文件时,import这个文件的时候,下面的语句就不会被执行
    #unittest.main()  #执行当前文件中所有的unittest的测试用例
    UnittestDemo().reg()  #实例化注册的方法然后调用


