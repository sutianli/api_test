#发邮件步骤介绍
'''
import smtplib  # 用于建立smtp连接
from email.mime.text import MIMEText  # 邮件需要专门的MIME格式

# 1. 编写邮件内容（Email邮件需要专门的MIME格式）
msg = MIMEText('this is a tests email', 'plain', 'utf-8')  # plain指普通文本格式邮件内容

# 2. 组装Email头（发件人，收件人，主题）
msg['From'] = 'test_results@sina.com'  # 发件人
msg['To'] = '2375247815@qq.com'  # 收件人
msg['Subject'] = 'Api Test Report'  # 邮件主题

# 3. 连接smtp服务器并发送邮件
smtp = smtplib.SMTP_SSL('smtp.sina.com')  # smtp服务器地址 使用SSL模式
smtp.login('自己的邮箱地址', '自己的邮箱密码')  # 用户名和密码
smtp.sendmail("接收邮件地址1", "接收邮件地址2", msg.as_string())
smtp.quit()
'''
import unittest

'''中文邮件主题、HTML邮件内容，及附件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题

# 1.  编写邮件内容
with open('report.html', encoding='utf-8') as f:  # 打开html报告
    email_body = f.read()  # 读取报告内容

msg = MIMEMultipart()  # 混合MIME格式
msg.attach(MIMEText(email_body, 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

# 2. 组装Email头（发件人，收件人，主题）
msg['From'] = 'test_results@sina.com'  # 发件人
msg['To'] = '2375247815@qq.com'  # 收件人
msg['Subject'] = Header('接口测试报告', 'utf-8')  # 中文邮件主题，指定utf-8编码

# 3. 构造附件1，传送当前目录下的 tests.txt 文件
att1 = MIMEText(open('report.html', 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
msg.attach(att1)

# 4. 连接smtp服务器并发送邮件
smtp = smtplib.SMTP_SSL('smtp.sina.com')  # smtp服务器地址 使用SSL模式
smtp.login('test_results@sina.com', 'hanzhichao123')  # 用户名和密码
smtp.sendmail("test_results@sina.com", "2375247815@qq.com", msg.as_string())
smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
smtp.quit()
'''

#封装发邮件方法
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import sys
sys.path.append('..')
from config.config import *

#首先需要确认用来发送邮件的邮箱是否启用了smtp服务
def send_email(report_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))

    msg['From'] = 'stl298458@163.com'
    msg['To'] = '495225829@qq.com'
    msg['Subject'] = Header(subject, 'utf-8')  # 从配置文件中读取

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 从配置文件中读取
    att1["Content-Type"] = 'application/octet-stream'
    # 方式一
    # now_time=time.strftime('%Y-%m-%d %H:%M:%S')
    # filename='report'+now_time+'.html'
    # att1["Content-Disposition"] = 'attachment; filename="'+filename
    #方式二
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(report_file))  # 获取报告文件名字，参数化一下report_file
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)  # 从配置文件中读取
        smtp.login(smtp_user, smtp_password)  # 从配置文件中读取
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':   # 非必要，用于测试我们的代码
    unittest.main(verbosity=2)