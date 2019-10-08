from com.SendMailUtil import SendMail
from com.ReadFileSendMail import *


class Test(object):

    def __init__(self):
        print("开始运行")
        # SendMail.sendmail("你好", "我是测试", "yx503203440@163.com")
        path = input("输入文件的路径")
        mails = ReadFileSendMail.readfile(path)
        ReadFileSendMail.sendmail("晚上好", "我在测试发送邮件", mails)


if __name__ == "__main__":
    Test()
