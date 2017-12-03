# 1.之前的 readcsv 不能被其他测试用例调用,应该给这段代码封装到一个方法里
# 2.每个测试用例的路径不同,所以path应该作为参数传入到这个方法中
# 3.打开了一个文件,但是并没有关闭,最终会造成内存泄露
import csv
import os


def read(file_name):
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/"+ file_name )
    # file = open(path,'r')
    # with语句是一个代码块,代码块中的内容都要缩进4个空格,with代码块可以自动关闭with中声明的变量file
    # try... finally... 可读性较差 ,现在用with代替

    result = []   # 声明一个列表变量接收返回值

    with open(path,'r') as file:
        data_table = csv.reader(file)
        for row in data_table:
            result.append(row)
    return result

    # 如果在打开程序代码过程中发生了异常导致后面的代码不能正常运行,file.close()也不会被执行,这时文件仍然不能关闭,应该用with... as... 语句实现文件的关闭
    # file.close()

if __name__ == '__main__':
    # path = r"C:\Users\51Testing\PycharmProjects\case\data\member_info.csv"  # 这个路径是绝对路径,应该在代码中自动找到相对路径
    #首先找到当前文件路径,dir是directory目录,__file__是python内置变量指的是当前文件
    # current_file_path = os.path.dirname(__file__)
    # print(current_file_path)  # 打印出来是这个   C:/Users/51Testing/PycharmProjects/case/day4

    # 真正想要的csv路径
    # path = current_file_path.replace("day4","data/member_info.csv")
    # print(path)
    member_info = read("member_info.csv")
    # print(member_info)

    for row in member_info:
        print(row[0])

    # 4.通过数据驱动测试,所以应该把数据作为方法的返回值方便进一步调用,return result
