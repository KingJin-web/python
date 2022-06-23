import requests

# 请求地址
url = "https://www.xxx.com"  # 代理服务器
ipport = "ip:port"
proxies = {
    'http': ipport,
    'https': ipport
}
res = requests.get(url, proxies=proxies, timeout=5)
print(res.status_code)
print(res.text)
