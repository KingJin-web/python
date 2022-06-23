#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import requests
import random
import string
import 爬虫.getIp as getIp
import requests
import json

count = 0

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

ips = [
    "190.104.1.19:999",
    "31.14.124.3:8080",
    "103.146.196.33:8080",
    "104.129.198.56:8800",
    "36.94.40.123:9812",
    "165.225.56.64:10605",
    "173.212.245.135:3128",
    "115.223.7.32:80",
    "125.26.4.219:443",
    "202.138.240.189:8888",
    "194.114.128.149:61213",
    # 170.246.85.38:50991",
    # 38.10.246.142:9991",
    # 120.194.55.139:6969",
    # 177.54.229.1:9292",
    # 190.61.101.205:8080",
    # 124.205.155.147:9090",
    # 47.254.93.239:7328",
    # 51.75.206.209:80",
    # 190.210.8.91:8080",
    # 89.111.105.89:41258",
    # 47.254.74.22:7328",
    # 165.225.112.9:10605",
    # 103.215.24.190:9812",
    # 147.161.251.73:80",
    # 213.6.28.94:8080",
    # 43.224.10.27:6666",
    # 101.35.159.152:3128",
    # 161.97.74.153:81",
    # 24.51.32.59:8080",
    # 36.95.133.234:8080",
    # 52.7.124.246:5555",
    # 68.183.128.249:80",
    # 103.4.167.46:8080",
    # 103.152.232.162:8080",
    # 1.179.148.9:55636",
    # 190.120.188.186:999",
    # 138.219.244.154:6666",
    # 49.231.174.182:80",
    # 158.69.71.245:9300",
    # 139.255.109.27:8080",
    # 47.101.129.140:8118",
    # 88.255.102.120:8080",
    # 179.1.129.134:999",
    # 47.88.89.119:7328",
    # 195.178.33.86:8080",
    # 88.199.164.140:8081",
    # 171.92.21.43:9000",
    # 103.139.25.81:8080",
    # 213.241.205.1:8080",
    # 117.54.114.97:80",
    # 190.120.186.29:999",
    # 45.248.138.150:8080",
    # 117.57.62.155:8499",
    # 138.117.84.161:999",
    # 46.99.158.49:8080",
    # 125.25.32.214:8080",
    # 184.183.3.211:8080",
    # 104.129.206.67:8800",
    # 165.225.76.160:10605",
]

proxy = {
    'http': '123.56.175.31:3128',
}


def getQQNumber():
    return random.randint(10000000, 9999999999)


def getQQPwd():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(random.randint(6, 10)):
        sa.append(random.choice(seed))
    return ''.join(sa)


def test():
    # http://xh73a.xyz/
    # http://180.215.197.247/shoy.php
    # url = "http://qwq.tianyab.store/update/index.php"
    url = "http://180.215.197.247/update/index.php"
    data_json = {'username': getQQNumber(), 'pass': getQQPwd(), 'user': '你爹',
                 'type': "你他妈真是傻逼"}
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        'User-Agent': random.choice(user_agent_list)
    }
    r1 = requests.post(url, data_json, headers=header, proxies=proxy)
    # print("r1返回的内容为-->")
    print(r1.text)
    return 1


def test2():
    url = "http://xh73a.xyz/load.asp"
    # [111.68.6.222]
    data_json = {'QQNumber': getQQNumber(), 'QQPassWord': getQQPwd(), 'actionid': 'ok'}

    r = requests.get("http://xh73a.xyz/")
    cookie = r.cookies
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",

        'User-Agent': random.choice(user_agent_list),
        'Cookie':cookie
    }

    print(cookie)
    r1 = requests.post(url, data_json, headers=header, proxies=proxy )
    # print("r1返回的内容为-->")
    print(r1.status_code)
    return 1


def get_random_ip(ip_list):
    # 获取代理IP地址
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


if __name__ == '__main__':
    # count = count + test()
    # count = count + test2()
    # print("运行了 ", count, "次")
    # ips = getIp.getProxyIp2()

    while True:
        try:
            proxy = get_random_ip(ips)
            print(proxy)
            proxy = {
                'http': '123.56.175.31:3128',
            }

            count = count + test()
            count = count + test2()
            print("运行了 ", count, "次")
        except Exception as e:
            print(e.args)
