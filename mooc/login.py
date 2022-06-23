import requests


def login():
    url = 'https://mooc.wuzhaoqi.top/api/user/login.do'
    headers = {
        'Content-Type': "application/json"
    }
    payload = {
        "username": "king",
        "password": "11111"
    }
    try:
        res = requests.post(url, headers=headers, json=payload)
        cookies = res.cookies
        print(res.text)
        return cookies
    except Exception as err:
        print('获取cookie失败：\n{0}'.format(err))


if __name__ == '__main__':
    login()
