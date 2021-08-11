import json
import requests
# Python的字典的格式和JSON格式，稍有不同：
# 字典中的引号支持单引号和双引号，JSON格式只支持双引号
# 字典中的True/False首字母大写，JSON格式为true/false
# 字典中的空值为None, JSON格式为null
# JSON格式操作方法#
# 序列化（字典 -> 文本/文件句柄）： json.dumps()/json.dump()
# 反序列化（文本/文件句柄 -> 字典) : json.loads()/json.load()
print("******序列化演示****")
data={"name":"苏天利","password":"123456","male":"true","money":None }#字典格式
str_data=json.dumps(data)#序列化，转化为合法的json文本（方便http传输）
print(str_data )

print("******序列化演示2****")

res = requests.post("http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=怎么又是你")
print(res.text) # 输出为一行文本
res_dict = res.json() # 将响应转为json对象（字典）等同于`json.loads(res.text)`,这里是反序列化的意思
print(json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False)) # 重新转为文本
# indent: 缩进空格数，indent=0输出为一行
# sork_keys=True: 将json结果的key按ascii码排序
# ensure_ascii=Fasle: 不确保ascii码，如果返回格式为utf-8包含中文，不转化为\u...

print("**********反序列化演示**********")
res_text = '{"name": "\u82cf\u5929\u5229", "password": "123456", "male": true, "money": null}'  # JSON文本格式的响应信息
res_dict = json.loads(res_text) # 转化为字典
print(res_dict['name'])  # 方便获取其中的参数值

print("*******文件序列化：字典-》文件句柄******")#广义上的句柄是一个指针
res_dict = {'name': '张三', 'password': '123456', "male": True, "money": None} # 字典格式
f = open("../../demo1.json", "w")#增加一个demo1.json文件
json.dump(res_dict, f)

print("*******序列化：文件句柄-》字典*********")
f = open("../../demo2.json", "r", encoding="utf-8")  # 文件中有中文需要指定编码
f_dict = json.load(f) # 反序列化将文件句柄转化为字典
print(f['name']) # 读取其中参数
f.close()

# 什么时候使用JSON对象（字典）什么时候使用JSON文本？
# 一般在组装data参数时，建议使用字典格式，发送请求时用json.dumps(data)转化为文本发送，
# 收到请求后使用json.loads(res.text)转化为字典，方便我们获取其中的参数信息