import json
import unittest
import requests

#数据准备
from lib.db import check_user

TEST_USER="张三"
PW=123

class Test_contrast(unittest.TestCase):
    url = 'http://127.0.0.1:1888/oreo/personal/portrait/contrast'
    def test_contrast_normal(self):
        #环境检查
        if check_user(TEST_USER):
            print("*****数据存在********")
        #发送请求
        data={"name":"张三","idcard":"123"}
        res=requests.post(url=self.url,data=data)#mockservice的post接口是默认x-www-form-rulencoded方式提交
        print(res.text)

        excep_res={"resCode":"0000","resMsg":"提交成功","data":{"statusCode":"2012","statusMsg":"查询成功","result":{"score":"78"}}}#字典格式
        #响应断言(整体断言)
        res_dict=json.loads(res.text)#文本转换为dict字典格式
        self.assertDictEqual(res_dict,excep_res)

if __name__=='__main__':
    unittest.main(verbosity=2)#运行所有用例
