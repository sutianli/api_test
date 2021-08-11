import logging
import os
import time
from optparse import OptionParser


# 项目路径
today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())



prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
#生成文件
report_file = os.path.join(prj_path, 'report/report.html'.format(now))  # 也可以每次生成新的报告
log_file = os.path.join(prj_path, 'log.txt'.format(today))  # 也可以每天生成新的日志文件
# report_file = os.path.join(prj_path, 'report','report.html')  # 更改路径到report目录下
# log_file = os.path.join(prj_path, 'log','log.txt')  # 更改路径到log目录下

#读取文件
data_file=os.path.join(prj_path,'data','test_youfen_data.xlsx')
testlist_file=os.path.join(prj_path,'tests','textlist.txt')
last_fails_file=os.path.join(prj_path,'last_failapi.pickle')

#数据路径
data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'tests')   # 用例目录
test_case_path=os.path.join(prj_path,'tests','case')
# data_path = prj_path  # 数据目录，暂时在项目目录下
# test_path = prj_path  # 用例目录，暂时在项目目录下


# 数据库配置
db_host = '127.0.0.1'   # 自己的服务器地址
db_port = 3306
db_user = 'root'
db_passwd = '123456'
db = 'yun_bc_credit'

# 邮件配置
smtp_server = 'smtp.sina.com'
smtp_user = 'test_results@sina.com'
smtp_password = 'hanzhichao123'
sender = smtp_user  # 发件人
receiver = '495225829@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题

send_email_after_run = False#配置邮件开关

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式

if __name__ == '__main__':
    logging.info("hello")


'''
Log Level:

CRITICAL: 用于输出严重错误信息
ERROR: 用于输出错误信息
WARNING: 用于输出警示信息
INFO: 用于输出一些提升信息
DEBUG: 用于输出一些调试信息
优先级 CRITICAL > ERROR > WARNING > INFO > DEBUG
指定level = logging.DEBUG所有等级大于等于DEBUG的信息都会输出
若指定level = logging.ERROR WARNING,INFO,DEBUG小于设置级别的信息不会输出

日志格式:

%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息
'''

# 命令行选项
parser = OptionParser()
parser.add_option('--collect-only', action='store_true', dest='collect_only', help='仅列出所有用例')
parser.add_option('--rerun-fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
parser.add_option('--testlist', action='store_true', dest='testlist', help='运行test/testlist.txt列表指定用例')
parser.add_option('--testsuite', action='store', dest='testsuite', help='运行指定的TestSuite')
parser.add_option('--tag', action='store', dest='tag', help='运行指定tag的用例')
(options, args) = parser.parse_args()  # 应用选项（使生效）