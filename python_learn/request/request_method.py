import  requests
from json import learn_json

#带参数的get请求
print("******带参数的get请求******")
url1="http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好"  # 参数可以写到url里
res1=requests.get(url=url1)
print(res1.text) #response.text是以str的形式返回响应信息，response.content是以bytes形式返回

url2 = "http://www.tuling123.com/openapi/api"
params = {"key":"ec961279f453459b9248f0aeb6600bbe","info":"你好"} # 字典格式，单独提出来，方便参数的添加修改等操作
res2= requests.get(url=url2, params=params)
print(res2.text)
print("*****传统表单类POST请求（x-www-form-urlencoded）******")

# 传统表单类POST请求（x-www-form-urlencoded）
url3 = "http://httpbin.org/post"
data = {"name": "hanzhichao", "age": 18} # Post请求发送的数据，字典格式
res3 = requests.post(url=url3, data=data) # 这里使用post方法，参数和get方法一样
print(res3.text)
print("*******JSON类型的POST请求（application/json）*********")

# JSON类型的POST请求（application/json）
# 或直接将字典格式的data数据赋给post方法的JSON参数（会自动将字典格式转为合法的JSON文本并添加headers）

url6= "http://openapi.tuling123.com/openapi/api/v2"
data6 = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "信息路"
            }
        }
    },
    "userInfo": {
        "apiKey": "ec961279f453459b9248f0aeb6600bbe",
        "userId": "206379"
    }
}
res = requests.post(url=url6, json=data6) # JSON格式的请求，将数据赋给json参数
print(res.text)


#***************以下方式不建议，麻烦***********************
url4= "http://httpbin.org/post"
data2= '''{
        "name": "hanzhichao",
        "age": 18
        }''' # 多行文本, 字符串格式，也可以单行（注意外层有引号，为字符串） data = '{"name": "hanzhichao", "age": 18}'
res4= requests.post(url=url4, data=data2) #  data支持字典或字符串
print(res4.text)

# data参数支持字典格式也支持字符串格式，如果是字典格式，requests方法会将其按照默认表单urlencoded格式转换为字符串，如果是字符串则不转化
# 如果data以字符串格式传输需要遵循以下几点：
# 必须是严格的JSON格式字符串，里面必须用双引号，k-v之间必须有逗号，布尔值必须是小写的true/false等等
# 不能有中文，直接传字符串不会自动编码
# 一般来说，建议将data声明为字典格式（方便数据添加修改），然后再用json.dumps()方法把data转换为合法的JSON字符串格式
url5 = "http://httpbin.org/post"
data3 = {
        "name": "hanzhichao",
        "age": 18
        }  # 字典格式，方便添加
headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res = requests.post(url=url5, data=learn_json.dumps(data3), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print(res.text)

