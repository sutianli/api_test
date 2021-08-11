#说明：从test_mockservice_youfen.py的代码上将测试案例进行文件配置化
import sys
import unittest
import requests
from lib.read_excel import * # 导入read_excel中的方法
import json  # 用来转化excel中的json字符串为字典
from config.config import *
from lib.db import check_user
from lib.case_log import log_case_info
import os
# sys.path.append('../..')
from tests.basecase import BaseCase

'''
class TestContrastt(unittest1.TestCase):
    @classmethod    #声明类方法，使用这个类不需要实例化对象再调用；可以直接类名.方法（）来调用，不需要self参数，第一个参数需要是表示自身类的cls参数
    def setUpClass(cls):   # 整个测试类只执行一次
        cls.data_list= excel_to_list(os.path.join(data_path,"test_youfen_data.xlsx"),"Test_contrast")#读取Test_contrast工作簿所有数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_contrast_normal(self):
        case_data = get_test_data(self.data_list, 'test_contrast_normal')   # 从数据列表中查找到该用例数据
        if not case_data:   # 有可能为None
            logging.error("用例数据不存在")
        url = case_data.get('url')   # 从字典中取数据，excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=json.loads(data))  # 表单请求，数据转为字典格式
        self.assertEqual(res.text, expect_res)  # 改为assertEqual断言



class TestContrast_2(unittest1.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list=excel_to_list(os.path.join(data_path,"test_youfen_data.xlsx"),"Test_youfen_Interface")

    def test_youfen_Interface(self):
        case_data = get_test_data(self.data_list, 'test_2_contrast')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        # data = {"name": "张三", "idcard": "123"}
        data= json.loads(case_data.get('data'))  # 转为字典，需要取里面的name进行数据库检查
        expect_res = json.loads(case_data.get('expect_res'))  # 转为字典，断言时直接断言两个字典是否相等
        name = data.get("name")  #

        # 环境检查
        if check_user(name):
            logging.info('check db ok')
        # 发送请求
        res = requests.post(url=url, data=data)  # 用data=data 传字符串也可以
        # res = requests.post(url=url, json=data)  # 如果是json，下面断言也要用json
        # self.assertDictEqual(res.json(), expect_res)
        log_case_info('test_2_contrast',url,data,expect_res,res.text)
        logging.info("测试用例:{}".format('test_2_contrast'))
        logging.info("url:{}".format(url))
        logging.info("请求参数:{}".format(data))
        logging.info("期望结果:{}".format(expect_res))
        logging.info("实际结果:{}".format(res.text))
        # # 响应断言（整体断言）
        self.assertDictEqual(json.loads(res.text), expect_res)
        # 数据库断言
        self.assertTrue(check_user(name))


'''
#封装后直接调用
class Test_contrast(BaseCase):#前面封装已经规定，clss起名必须是sheet名一致
    def test_1_crimeinfo(self):
        case_data=self.get_case_data("test_1_crimeinfo")#get请求
        self.send_request(case_data)


class Test_youfen_Interface(BaseCase):#前面封装已经规定，clss起名必须是sheet名一致
    def test_2_contrast(self):
        """level1:tab标记用例--crimeinfo"""
        case_data=self.get_case_data("test_2_contrast")#post请求
        # 环境检查
        name=json.loads(case_data.get("args")).get('name')
        if check_user(name):
            logging.info('check db ok')
        #发送请求
        self.send_request(case_data)
        # 数据库断言
        self.assertTrue(check_user(name))

if __name__ == '__main__':   # 非必要，用于测试我们的代码
    unittest.main(verbosity=2)