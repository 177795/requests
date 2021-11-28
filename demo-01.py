import requests

#
# # get方法请求百度
# baidu = requests.get("http://www.baidu.com")
# # 将返回的结果已text的方式打印出来
# print(baidu.text)


# post方法请求tpshop登录接口
url = 'http://localhost/index.php?m=Home&c=User&a=do_login'
data = {"username": "admin", "password": "123456", "verify_code": "1234"}
response = requests.post(url, data=data)
print("test=", response.text)

url1 = 'http://121.196.13.152:8080/admin/auth/login'
data1 = {"username": "admin123", "password": "admin123"}
response1 = requests.post(url1, json=data1)
print("test=", response1.text)
