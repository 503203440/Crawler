#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 上面这两行是因为python在默认的情况下不支持源码中的中文编码，加上后会忽略中文编码


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders


class SendMail(object):

    # 静态方法不需要第一个参数self，可以直接类名调用
    @staticmethod
    def sendmail(title, content, users):
        # 申明第三方服务关键信息

        # mail_host = "smtp.qq.com"
        # mail_user = "503203440@qq.com"
        # mail_pass = "***"
        # sender = "503203440@qq.com"  # 发送者邮箱

        mail_host = "smtp.163.com"
        mail_user = "yx503203440@163.com"
        mail_pass = "***"
        sender = 'yx503203440@163.com'  # 发送者邮箱

        receivers = users  # 接收者邮箱(数组)

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header('小熊科技', 'utf-8')
        # message['To'] = Header('YOU', 'utf-8') # 这里可以不用设置
        subject = title
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))
        # # 构造附件
        # file_name = 'zcpd_backup.sql'
        # attr = MIMEText(open('C:/Users/YX/Desktop/zcpd_20190715_003047.sql', 'rb').read(), 'base64', 'utf-8')  # 文件路径
        # attr['Content-Type'] = 'application/octet-stream'
        #
        # # 这么写不行，附件会变成.bin后缀名的文件
        # # attr['Content-Disposition'] = 'i;filename=sql备份.sql' # + file_name
        #
        # # 这样设置附件名
        # attr.add_header('Content-Disposition', 'attachment', filename=file_name)
        #
        # # encoders.encode_base64(attr)
        #
        # # 添加附件
        # message.attach(attr)
        # 如果有多个附加，可以按此方式构造多个附件多次调用message.attach()

        # try:
        #     smtpObj = smtplib.SMTP()
        #     smtpObj.connect(mail_host)
        #     smtpObj.login(mail_user, mail_pass)
        #     smtpObj.sendmail(sender, receivers, message.as_string())
        #     print('发送成功')
        # except smtplib.SMTPException:
        #     print('发送失败')

        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('发送成功')
