import os
import smtplib
import unittest
# HTMLTestRunner 是基于unittest 框架的一个扩展,可以自己在网上自行下载,网上几乎都是python2的
import time
from email.header import Header
from email.mime.text import MIMEText
from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open (path ,'rb')
    mail_body = f.read()  # 将文件的内容一次性全部读出
    f.close()
    # 把二进制内容转成mime(Multipurse Internet Mail Extension)格式进行发送,mime是对邮件协议的一个扩展,使邮件不仅支持文本格式,还支持多种格式,比如图片 音频 或者二进制文件等
    msg = MIMEText(mail_body,'html','utf-8')

    # 上面是邮件正文,下面是主题,收件人,发件人
    msg['Subject'] = Header("自动化测试报告",'utf-8')  # Header是主题,msg是字典的类型,字典类似于数组,字典是无序的,Subject是字典的一个id
    # 如果想用客户端软件或者自己写代码登录邮箱,很多类型的邮箱需要单独设置一个客户端授权码(为了邮箱安全着想)
    msg['from'] = 'bwftest126@126.com'
    msg['To'] = 'liuji6903@163.com'

    # 邮件内容已经准备好了,下面开始发送邮件:打开登录页面(即连接邮箱服务器,网络传输协议:http https ftp socket; 发邮件的协议一般有三种,先查看邮箱支持哪种协议:POP3 SMTP IMAP)-登录邮箱-发送邮件-退出邮箱

    # 首先导入smtplib 代码库
    smtp = smtplib.SMTP()  # 实例化一个SMTP类的对象
    smtp.connect("smtp.126.com")  # 连接126邮箱的服务器地址

    smtp.login('bwftest126@126.com','abc123asd654')  # 登录邮箱

    smtp.sendmail('bwftest126@126.com', 'liuji6903@163.com', msg.as_string())  # 发送邮件

    smtp.quit()  # 退出邮箱
    print("email has sent out!")


if __name__ == '__main__':
    # 时间戳, str 是string ,f 是 formate 格式
    # strftime() 通过这个方法定义时间的格式
    # Y -- year , m -- month , d -- day , H -- hour , M -- minute , S -- second
    now = time.strftime("%Y-%m-%d_%H-%M-%S")

    suite = unittest.defaultTestLoader.discover('./day5','*Test.py')  # 若要找到目录下的所有package,可以只写.
    # unittest.TextTestRunner  # 文本的测试用例运行器
    base_path = os.path.dirname(__file__)
    path = base_path + "/report/report"+ now +".html"
    file = open(path ,'wb')
    HTMLTestRunner(stream=file , title="海盗商城测试报告", description="测试环境:win2008R2 + Chrome").run(suite)  # html的测试用例运行器,需要指定测试报告的路径

    file.close()

    # 这时生成的测试报告只显示类名和方法名,只能专业人士看,需要把中文标题加到测试报告里,去测试用例脚本里面加文档注释就可以了

    # 自动化测试用例是从手工测试用例中挑出来的,手工测试用例怎么写我们就怎么编写代码,所以我们的代码里应该要体现手工测试用例的标题

    # 在测试方法里加一个print()打印语句就可以将这句话加入到测试报告里

    # 新的测试报告会覆盖原来的,如果想把所有的测试报告保存起来怎么做:(1)可以改测试报告的名字
                    # (2) 可以加一个时间戳,按照当前时间计算一个数字,把数字作为文件名的一部分,就可以避免文件名重复

    # html测试报告生成了,接下来当测试用例全部执行完成,应该生成一封邮件提醒
    # 把html报告作为邮件正文进行发送
    send_mail(path)



