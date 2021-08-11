import  unittest

from lib.HTMLTestReportCN import HTMLTestRunner
from test.test_mockservice_youfen2 import Test_contrast #从模块导入测试类
from test.test_mockService_youfen import  Test_youfen_Interface

#测试集有4种方法添加
# # 1.使用makeSuite来制作用例集
suite1=unittest.makeSuite(Test_youfen_Interface,'test_1_crimeinfo')#使用测试类单条用例制作测试集
suite2=unittest.makeSuite(Test_youfen_Interface)#使用整个测试类所有用例制作测试集
#运行测试集
# unittest1.TextTestRunner(verbosity=2).run(suite1)#verbosity显示级别，运行顺序为添加到suite的顺序
# unittest1.TextTestRunner(verbosity=2).run(suite2)

#2.使用TestLoder(用例加载器)生成测试集
suite3=unittest.TestLoader().loadTestsFromTestCase(Test_youfen_Interface)#加载该测试类所以测试用例并生成测试集
# unittest1.TextTestRunner(verbosity=2).run(suite3)

#3.使用discover(用例发现)遍历所有的用例
# 子目录中需要包含__init__.py文件，及应为的Python包
# 所有用例因为test_*.py,包含测试类应以Test开头，并继承unittest.TestCase, 用例应以test_开头
# suite4=unittest1.defaultTestLoader.discover("./")#遍历当前目录及子包中所有test_*.py中所有unittest用例
# unittest1.TextTestRunner(verbosity=2).run(suite4)

# 4.使用TestSuite并添加测试用例集
suite5=unittest.TestSuite()
suite5.addTest(Test_contrast('test_contrast_normal'))#添加单个用例
suite5.addTests([Test_youfen_Interface('test_1_crimeinfo'),Test_youfen_Interface('test_2_contrast')])#添加多个用例
#5.测试集嵌套
suite=unittest.TestSuite([suite1,suite2,suite3,suite5])#组合多给测试集为一个
# unittest1.TextTestRunner(verbosity=2).run(suite)

#生成测试结果到文本文件
# with open("result.txt","w")as f:
#     unittest1.TextTestRunner(stream=f,verbosity=2).run(suite)#输出流stream输出到文件
f = open("report.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="Api Test",description="测试描述",tester="老男孩").run(suite)
f.close()