# 获取可用的IP代理
import random
import re
import requests

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
]


def getProxyIp():
    header = {
        'User-Agent': random.choice(user_agent_list),
    }

    response = requests.get("http://www.66ip.cn/2.html", headers=header)

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
    return new_ips


# 从代理IP列表中随机取出一个IP并返回
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def getProxyIp2():
    header = {
        'User-Agent': random.choice(user_agent_list),
    }

    response = requests.get("http://www.66ip.cn/" + str(random.randint(1, 100)) + ".html", headers=header)

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
    return new_ips


if __name__ == '__main__':
    ips = getProxyIp()
    print(get_random_ip(ips))

# header = {
#     #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
# }
#
# response = requests.get("http://www.66ip.cn/areaindex_11/1.html", headers=header)
#
# encode_content = response.content.decode('gb18030', 'replace')
#
# ips = re.findall("<td>(?:[0-9]{1,3}\.){3}[0-9]{1,3}</td><td>[0-9]{1,5}</td>", encode_content)
# new_ips = []
# # proxies = []
#
# for i in ips:
#     #     print(i)
#     new_ips.append(i.replace("</td><td>", ":"))
# #     print(i)
#
# for i in range(len(new_ips)):
#     new_ips[i] = new_ips[i].replace("<td>", "")
#     new_ips[i] = new_ips[i].replace("</td>", "")
# for i in new_ips:
#     print(i)
