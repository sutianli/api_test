import requests
import json
'''
res = requests.get("https://www.baidu.com")
print(res.status_code, res.reason) # 200 OK
print(res.text) # 文本格式，有乱码
print(res.content) # 二进制格式
print(res.encoding) # 查看解码格式 ISO-8859-1
print(res.apparent_encoding) # utf-8
res.encoding='utf-8' # 手动设置解码格式为utf-8
print(res.text) # 乱码问题被解决
print(res.cookies.items()) # cookies中的所有的项 [('BDORZ', '27315')]
print(res.cookies.get("BDORZ")) # 获取cookies中BDORZ所对应的值 27315
'''

# requests.session(): 用于保持会话（session）
print("***************带登录认证的接口：Cookie/Session认证***************")
s = requests.session() # 新建一个会话
s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":"123456"}) # 发送登录请求
res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs") # 使用同一个会话发送get请求，可以保持登录状态
print(res.text)
# 如果不使用session()而单独发一个post登录请求一个get请求,（requests.get()或post()每次都会建立一个新会话）

print("***************提取Cookie***************")
url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
cookies = {"PHPSESSID":"9bf6b19ddb09938cf73d55a094b36726"}#先浏览器登录提取cookie
res = requests.get(url=url, cookies=cookies) # 携带cookies发送请求
print(res.text)
# 使用session方式：每次都要发送两次请求，效率较低
# 使用携带cookies方式：需要手动抓包，提取组装，cookies中是session有一定有效期，过期之后要重新抓取和更换cookies
# 如果很多或所有请求都需要登录，可以发一次请求，保持该session为全局变量，其他接口都使用该session发送请求（同样要注意登录过期时间）

print("***************获取token，再访问需要token头信息的url***************")
app_key = 'kPoFYw85FXsnojsy5bB9hu6x'
secret_key = 'l7SuGBkDQHkjiTPU3m6NaNddD6SCvDMC'
img_url = 'http://upload-images.jianshu.io/upload_images/7575721-40c847532432e852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
# 获取token
get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(app_key,secret_key)
#format,将括号内的参数，顺序填充到前面字符串的{}内
token = requests.get(url=get_token_url).json().get("access_token")  # 从获取token接口的响应中取得token值
# 识别图片文字
orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}'.format(token)
data = {"url": img_url}
res = requests.post(url=orc_url, data=data)
print(json.dumps(res.json(), indent=2, ensure_ascii=False)) # 格式化输出


print("*******reqeusts支持Basic Auth（基本授权）和Digist Auth（摘要授权）*************")
# 基本授权可以直接在请求方法中使用`auth = (user,password)`
res = requests.get("https://api.github.com/user", auth=("hanzhichao", "hanzhichao123"))
print(json.dumps(res.json(), indent=2, ensure_ascii=False))  # 格式化输出
