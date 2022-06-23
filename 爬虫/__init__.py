# -*- coding:utf-8 -*-
# @功能描述：爬取电影信息
# @程序作者：老九学堂·窖头
# @版权信息：http://www.xuetang9.com
# @版本信息：0.0.1
import time
import requests

from lxml import html




def get_html(url):
    user_agent = UserAgent(use_cache_server=False)
    headers = {"user-agent.txt": user_agent.random}
    response = requests.get(url, headers=headers)  # 获得响应对象
    # if response.status_code != 200:
    #     raise Exception("请检查传入的url：", url)
    return response.text


if __name__ == '__main__':
    url = "https://movie.douban.com/top250?start={}"
    #
    etree = html.etree
    for i in range(10):
        # print(url.format(i * 25))
        html_str = get_html(url.format(i * 25))
        html = etree.HTML(html_str)
        spans = html.xpath("//*[@id='content']/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span")
        for span in spans:
            print(span.text)
        # 遍历每一个li标签，一个li就对应一个电影的信息
        li_movies = html.xpath("//*[@id='content']/div/div[1]/ol/li")
        for li in li_movies:
            spans = li.xpath("./div/div[2]/div[1]/a/span")
            movie_title = ""
            for span in spans:
                movie_title += span.text
            # 电影信息
            movie_info = li.xpath('./div/div[2]/div[2]/p[1]')[0].text
            # 电影评分
            movie_score = li.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
            # 一句话简评
            movie_intro = li.xpath('./div/div[2]/div[2]/p[2]/span/text()')[0]
            print(movie_title, movie_info, "\n电影评分：", movie_score, "\n一句话简评：", movie_intro)
        time.sleep(5)

    # 构建xpath解析对象

    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
    # //*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[1]/a/span[1]
    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]         # 电影信息的xpath路径
    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]  # 电影评分
    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[2]/span    # 一句话简评
    # spans = html.xpath("//*[@id='content']/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span")
    # for span in spans:
    #     print(span.text)
    # 遍历每一个li标签，一个li就对应一个电影的信息
    # li_movies = html.xpath("//*[@id='content']/div/div[1]/ol/li")
    # for li in li_movies:
    #     spans = li.xpath("./div/div[2]/div[1]/a/span")
    #     movie_title = ""
    #     for span in spans:
    #         movie_title += span.text
    #     # 电影信息
    #     movie_info = li.xpath('./div/div[2]/div[2]/p[1]')[0].text
    #     # 电影评分
    #     movie_score = li.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
    #     # 一句话简评
    #     movie_intro = li.xpath('./div/div[2]/div[2]/p[2]/span/text()')[0]
    #     print(movie_title, movie_info, "\n电影评分：", movie_score, "\n一句话简评：", movie_intro)
    #