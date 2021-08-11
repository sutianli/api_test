import unittest  # 导入unittest
import requests


class Test_youfen_Interface(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
    url = 'http://127.0.0.1:1888/oreo/personal/crimeInfo?idcard=123&name=%E5%BC%A0%E4%B8%89'
    url2 = 'http://127.0.0.1:1888/oreo/personal/portrait/contrast'

    def test_1_crimeinfo(self):  # 一条测试用例，必须test_开头
        res = requests.get(url=self.url)
        self.assertIn('0000', res.text)  # 断言
        print("crimeinfo：",res.text)

    def test_2_contrast(self):  # 用例执行顺序：并非按书写顺序执行，而是按用例名ascii码先后顺序执行,解决方法，前面加数字_1_按数字定顺序
        data = {"name": "张三", "idcard": "123"}
        res = requests.post(url=self.url2, data=data)
        self.assertIn('提交成功', res.text)  # 断言
        print("contrast:",res.text)

#一个py文件为一个模块
    if __name__ == '__main__':  # __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，
                                # 以下代码块将被运行，当模块是被导入时，代码块不被运行。如果是其他人导入我的这个小红.py文件的时候，
                                # if下面的语句是执行不到的，如果我自己直接运行小红.py这个文件的时候，if 下面的语句就会执行。
        unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别