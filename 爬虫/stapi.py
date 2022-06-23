import requests
import re


def getST():
    url = "http://api.lolicon.app/setu/v2"
    params = {"r18": '1', 'num': 1}
    resp = requests.get(url=url, params=params, verify=False)
    data = str(resp.json())
    pic_path = re.findall("https.*\...g", data)
    file_name = re.findall('[0-9]*_..\...g', pic_path[0])
    return {"路径": pic_path, "文件名": file_name}


if __name__ == '__main__':
    print(getST())
