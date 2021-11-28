import requests

# 1、传递整个url
# reponse = requests.get('http://localhost/Home/Goods/search.html?q=iPhone')
# print(reponse.text)


# 2、参数与url分开传递， params接收的是字符串
# url = 'http://localhost/Home/Goods/search.html'
# key = 'q=iphone'
# re = requests.get(url, params=key)
# print(re.text)


# 3、参数与url分开传递， params接收的是字典
url = 'http://localhost/Home/Goods/search.html'
dict = {"q": "iphone"}
res = requests.post(url, params=dict)
print(res.text)