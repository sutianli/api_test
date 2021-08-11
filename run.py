import pickle
import sys

from config.config import *
from lib.HTMLTestReportCN import *
import logging
from lib.send_email import  send_email
from tests.suite.test_suites import *

#简单的运行所有用例
'''
logging.info("====================== 测试开始 =======================")
suite = unittest.defaultTestLoader.discover("./")

with open("report.html", 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)

send_email('report.html')  # 发送邮件
logging.info("======================= 测试结束 =======================")
'''

def discover():
    return unittest.defaultTestLoader.discover(test_case_path)#return suite
    # suite=unittest1.defaultTestLoader.discover(test_path)

def save_failures(result, file):   # file为序列化保存的文件名，配置在config/config.py中
    suite = unittest.TestSuite()
    for case_result in result.failures:   # 组装TestSuite
        suite.addTest(case_result[0])   # case_result是个元祖，第一个元素是用例对象，后面是失败原因等等

    with open(file, 'wb') as f:
        pickle.dump(suite, f)    # 序列化到指定文件

def rerun_fails():  # 失败用例重跑方法
    sys.path.append(test_case_path)   # 需要将用例路径添加到包搜索路径中，不然反序列化TestSuite会找不到用例
    with open(last_fails_file, 'rb') as f:
        suite = pickle.load(f)    # 反序列化得到TestSuite
    run(suite)



#列出所有用例
def collect():   # 由于使用discover() 组装的TestSuite是按文件夹目录多级嵌套的，我们把所有用例取出，放到一个无嵌套的TestSuite中，方便之后操作
    suite = unittest.TestSuite()

    def _collect(tests):   # 递归，如果下级元素还是TestSuite则继续往下找
        if isinstance(tests, unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)  # 如果下级元素是TestCase，则添加到TestSuite中

    _collect(discover())
    return suite



#按testlist用例列表运行
def makesuite_by_testlist(testlist_file):  # test_list_file配置在config/config.py中
    with open(testlist_file) as f:
        testlist = f.readlines()

    testlist = [i.strip() for i in testlist if not i.startswith("#")]   # 去掉每行结尾的"/n"和 #号开头的行

    suite = unittest.TestSuite()
    all_cases = collect()  # 所有用例
    for case in all_cases:  # 从所有用例中匹配用例方法名
        if case._testMethodName in testlist:
            suite.addTest(case)
    return suite

#用例按标签执行，通过判断用例方法中的docstring中加入特定的标签来重新组织TestSuite的方式
def makesuite_by_tag(tag):
    suite = unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:  # 如果用例方法存在docstring,并且docstring中包含本标签
            suite.addTest(case)
    return suite

def run(suite):
    logging.info("====================测试开始=========================")
    with open(report_file,'wb') as f: #改为with open格式
        result=HTMLTestRunner(stream=f,title='Api Test',description="测试描述",tester="老男孩").run(suite)
    #运行后保存失败用例序列化文件
    if result.failures:  # 保存失败用例序列化文件
        save_failures(result, last_fails_file)

    if send_email_after_run:  # 是否发送邮件
        send_email(report_file)
    logging.info("==================测试结束=================================")

def collect_only():   # 仅列出所用用例
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i), case.id()))
    print("----------------------------------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time()-t0))

def run_all():#运行所有用例
    run(discover())

def run_suite(suite_name):  # 运行`test/suite/test_suites.py`文件中自定义的TestSuite
    suite = get_suite(suite_name)
    if suite:
        run(suite)
    else:
        print("TestSuite不存在")

def run_by_testlist():
    run(makesuite_by_testlist(testlist_file))

def run_by_tag(tag):
    run(makesuite_by_tag(tag))

def run_by_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb') as f:
        suite=pickle.load(f)
    run(suite)


def main():
    if options.collect_only:    # 如果指定了--collect-only参数
        collect_only()
    elif options.rerun_fails:    # 如果指定了--rerun-fails参数
        rerun_fails()
    elif options.testlist:    # 如果指定了--testlist参数
        run(makesuite_by_testlist(testlist_file))
    elif options.testsuite:  # 如果指定了--testsuite=***
        run_suite(options.testsuite)
    elif options.tag:  # 如果指定了--tag=***
        run(makesuite_by_tag(options.tag))
    else:   # 否则，运行所有用例
        run_all()

if __name__ == '__main__':
    main()   # 调用main()


