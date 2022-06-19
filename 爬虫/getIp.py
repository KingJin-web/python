# 获取可用的IP代理
import re
import requests

header = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

response = requests.get("http://www.66ip.cn/areaindex_11/1.html", headers=header)

encode_content = response.content.decode('gb18030', 'replace')

ips = re.findall("<td>(?:[0-9]{1,3}\.){3}[0-9]{1,3}</td><td>[0-9]{1,5}</td>", encode_content)
new_ips = []
# proxies = []

for i in ips:
    #     print(i)
    new_ips.append(i.replace("</td><td>", ":"))
#     print(i)

for i in range(len(new_ips)):
    new_ips[i] = new_ips[i].replace("<td>", "")
    new_ips[i] = new_ips[i].replace("</td>", "")
for i in new_ips:
    print(i)


