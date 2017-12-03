# 1.首先导入pymysql代码库
import pymysql


def connDb():
    # 要想连接数据库,需要知道数据库哪些信息:IP ,port ,admin ,password ,name
    conn = pymysql.Connect(host="localhost", user="root", password="root",database="pirate", port=3306,charset='utf8')

    # 查询hd_user表中的所有数据并且倒叙打印
    sql = "select * from hd_user order by id desc"

    # 在代码中执行这条sql语句,首先要获取数据库的游标cursor
    curs = conn.cursor()

    # 通过游标来执行sql语句
    curs.execute(sql)

    # 想获取数据库中最新的记录,要用 fetchone() 方法,把数据库所有记录倒叙排列然后用fetchone() 方法获取第一条记录,即最新的记录
    # 若想获取所有的查询结果,用fetchall() 方法
    result = curs.fetchone()

    return result


if __name__ == '__main__':
    print(connDb())
