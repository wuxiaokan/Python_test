# coding:utf-8

# 导包
import requests

# 请求url
url = 'http://www.baidu.com'
# get请求
r = requests.get(url)

print("请求url", r.url)
print("请求状态码", r.status_code)
print("请求html文本", r.text)

# 带参请求  不建议写成'http://www.baidu.com?id=1001'
params = {'id': 1001}  # 一般为字典格式

# get请求
r1 = requests.get(url, params)

print("请求url", r1.url)
print("请求状态码", r1.status_code)
print("请求html文本", r1.text)

# 带同个id多个参数
params1 = {'id': '1001,1002'}

# get请求
r2 = requests.get(url, params1)
print("请求url", r2.url)
print("请求状态码", r2.status_code)
print("请求html文本", r2.text)

# 带多个字段参数
params2 = {'id': 1001, 'kw': '杭州'}
r3 = requests.get(url, params2)
print("请求url", r3.url)
print("请求状态码", r3.status_code)
print("请求html文本", r3.text)

# post请求
# url请求地址
url1 = 'https://test.joinf.com:8805/email/get'

# 请求headers
headers = {'Content-Type': 'application/json'}

# 请求json
data = {
        "data": [{
            "id": 20037708
        }]

}

r4 = requests.post(url1, json=data, headers=headers)

print('状态码', r4.status_code)

print('获取响应对象', r4.json())

print('git提交测试')
