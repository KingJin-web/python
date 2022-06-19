import requests

url = "http://httpbin.org/ip"
res = requests.get(url)
print(res.text)

proxy = {
    'http': '123.56.175.31:3128'
}

res = requests.get(url,proxies=proxy)
print(res.text)

response = requests.get("http://mooc.wuzhaoqi.top/api/course/recommend1.do",proxies=proxy)
print(response.text)
