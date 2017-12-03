import unittest


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("./day5", pattern='*Test.py')  # 默认的测试用例加载器,找到day5目录下的所有测试用例
    # TextTestRunner 首字母大写,说明他是一个类,类不能直接调用方法,必须实例化对象才能调用,后面直接加上小括号
    unittest.TextTestRunner().run(suite) # 文本的测试用例运行器

