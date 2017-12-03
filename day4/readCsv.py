# 1.准备一个csv文件
# 2.导入csv包,是python语言内置的包,比较常用
import csv

# 3.要想读取文件信息,首先要知道文件的存放路径
path = r"C:\Users\51Testing\PycharmProjects\case\data\member_info.csv"  # 字符串前面加r 表示反斜杠是普通字符,不看做转义字符

# 4.要想读文件的内容,首先要通过路径打开文件
file = open(path,'r')  # path是变量名不需要加双引号,r是默认值可以不写

# 5.通过csv代码库来读取csv文件
data_table = csv.reader(file)

# 6.遍历data_table,分别打印每一行数据
for row in data_table:
    print(row)

