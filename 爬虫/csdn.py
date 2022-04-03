import requests
import re
import time
import sys

print(sys.argv[0])
# print("传入的文章链接" + sys.argv[1])

payload = ""
# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Cookie": "l=AurqcPuigwQdnQv7WvAfCoR1OlrRQW7h; "
              "isg=BHp6mNB79CHqYXpVEiRteXyyyKNcg8YEwjgLqoRvCI3ddxqxbLtOFUBGwwOrZ3ad; thw=cn; "
              "cna=VsJQERAypn0CATrXFEIahcz8; t=0eed37629fe7ef5ec0b8ecb6cd3a3577; tracknick=tb830309_22; "
              "_cc_=UtASsssmfA%3D%3D; tg=0; ubn=p; ucn=unzbyun; "
              "x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; "
              "miid=981798063989731689; hng=CN%7Czh-CN%7CCNY%7C156; "
              "um"
              "=0712F33290AB8A6D01951C8161A2DF2CDC7C5278664EE3E02F8F6195B27229B88A7470FD7B89F7FACD43AD3E795C914CC2A8BEB1FA88729A3A74257D8EE4FBBC; enc=1UeyOeN0l7Fkx0yPu7l6BuiPkT%2BdSxE0EqUM26jcSMdi1LtYaZbjQCMj5dKU3P0qfGwJn8QqYXc6oJugH%2FhFRA%3D%3D; ali_ab=58.215.20.66.1516409089271.6; mt=ci%3D-1_1; cookie2=104f8fc9c13eb24c296768a50cabdd6e; _tb_token_=ee7e1e1e7dbe7; v=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
}


# headers = {
#     "Accept":
#         "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding":
#         "gzip, deflate, br",
#     "Accept-Language":
#         "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#     "Cache-Control":
#         "max-age=0",
#     "Connection":
#         "keep-alive",
#     "Cookie":
#         "uuid_tt_dd=10_9932274730-1620644548688-766587; log_Id_pv=110; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1627836202,1629691789,1629691823,1629817484; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22Hello_world12385%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_99322…; log_Id_click=51; UserName=Hello_world12385; UserInfo=923d413f55464301b51d365437e1b1ef; UserToken=923d413f55464301b51d365437e1b1ef; UserNick=Hello_world12385; AU=31F; UN=Hello_world12385; BT=1620870566553; p_uid=U010000; dc_session_id=10_1629817481459.842298; dc_sid=49a92272c85587864f2fa5a9e15c34aa; c_first_ref=default; c_first_page=https%3A//blog.csdn.net/qq_44737094/article/details/119063750; c_segment=11; c_page_id=default; dc_tos=qycn7v; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1629817484; is_advert=1",
#     "Host":
#         "blog.csdn.net",
#     "Sec-Fetch-Dest":
#         "document",
#     "Sec-Fetch-Mode":
#         "navigate",
#     "Sec-Fetch-Site":
#         "none",
#     "Sec-Fetch-User":
#         "?1",
#     "Upgrade-Insecure-Requests":
#         "1",
#     "User-Agent":
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
# }


# 获得文章列表urls
def getUrls(url):
    # 发送请求
    resp = requests.request("POST", url, data=payload, headers=headers)
    # 设置解码方式
    resp.encoding = resp.apparent_encoding
    # 这里会用设置的解码方式解码
    html_source = resp.text
    # 正则表达式，取出网页中的url链接（一些寻找注入点的工具也是这么做出来的）
    urls = re.findall("https://[^>\";\']*\d", html_source)
    new_urls = []
    for url in urls:
        if 'details' in url:
            if url not in new_urls:
                new_urls.append(url)
    return new_urls


urls = getUrls("https://blog.csdn.net/qq_44737094/article/details/123367196")
while True:
    for url in urls:
        requests.request("GET", url, data=payload, headers=headers)
        print(url, "Ok")
        time.sleep(5)
    time.sleep(5)
