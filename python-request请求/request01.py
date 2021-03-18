import requests


def request(info='hello'):
    apiUrl = 'http://10.192.26.23/robot'
    data = {
        'message': info
    }
    res = requests.post(apiUrl, json=data).text
    print(res)
    inputtext()


def inputtext():
    text = input('请输入需要发送的内容:')
    request(text)


if __name__ == '__main__':
    inputtext()