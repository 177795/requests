import requests

# 设置请求头
url1 = 'http://121.196.13.152:8080/admin/auth/login'
data1 = {"username": "admin123", "password": "admin123"}
headers = {"Content-Type": "application/json"}
response1 = requests.post(url1, json=data1, headers=headers)
print("test=", response1.text)

# 提交git