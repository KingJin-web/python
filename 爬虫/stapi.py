import requests
import re


def getST():
    num = int(input())
    while num > 0:
        url = "http://api.lolicon.app/setu/v2"
        params = {"r18": '1', 'num': num}
        resp = requests.get(url=url, params=params, verify=False)
        data = str(resp.json())
        print(data)
        pic_path = re.findall("https.*\...g", data)
        print(pic_path)
        file_name = re.findall('[0-9]*_..\...g', pic_path[0])
        num = int(input())
        print(file_name)



if __name__ == '__main__':
    getST()