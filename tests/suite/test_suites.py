import unittest
import sys
sys.path.append("../..")
from tests.case.test_youfen_api import Test_youfen_Interface
from tests.case.test_youfen_api import Test_contrast

smoke_suite = unittest.TestSuite()  # 自定义的TestSuite
smoke_suite.addTests([Test_contrast('test_1_crimeinfo'),Test_youfen_Interface('test_2_contrast')])

def get_suite(suite_name):    # 获取TestSuite方法
    return globals().get(suite_name)