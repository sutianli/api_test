import unittest
# Test Fixtures(用例包裹方法)
# Test Fixtures即setUp（用例准备）及tearDown（测试清理）方法，用于分别在测试前及测试后执行
# 按照不同的作用范围分为：
# setUp()/tearDown(): 每个用例执行前/后执行一次
# setUpClass()/tearDownClass(): 每个测试类加载时/结束时执行一次
# setUpMoudle()/tearDownMoudle(): 每个测试模块（一个py文件为一个模块）加载/结束时执行一次
def setUpModule():  # 当前模块执行前只执行一次
    print('=== setUpModule ===')


def tearDownModule():  # 当前模块执行后只执行一次
    print('=== tearDownModule ===')


class TestClass1(unittest.TestCase):
    @classmethod  # 声明为类方法（必须）
    def setUpClass(cls):  # 类方法，注意后面是cls，整个类只执行一次
        print('--- setUpClass ---')

    @classmethod
    def tearDownClass(cls):
        print('--- tearDownClass ---')

    def setUp(self):  # 该类中每个测试用例执行一次
        print('... setUp ...')

    def tearDown(self):
        print('... tearDown ...')

    def test_a(self):  # 测试用例
        print("a")

    def test_B(self):  # 大写B的ascii比小写a靠前，会比test_a先执行
        print("B")


class TestClass2(unittest.TestCase):  # 该模块另一个测试类
    def test_A(self):
        print("A")


if __name__ == '__main__':
    unittest.main()