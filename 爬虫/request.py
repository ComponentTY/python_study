import requests
import re
from requests.exceptions import RequestException


def getonepage(url):
    try:
        response = requests.get(url)
        response.encoding = 'gb2312'
        if response.status_code == 200:
            html = response.text
            # print(html)
            parser(html)
        else:
            return None
    except RequestException:
        return None


def parser(html):
    # pattern = re.compile("<table.*?><tr>.*?href='(.*?)'>(.*?).*?red.*?>(.*?)
    # </font>(.*?)</a><tr><tr>.*?colspan.*?>(.*?)</td></tr>.*?</table>", re.S)
    pattern = re.compile('<tr.*?13043029091535013630428".*?>.*?num">(\d+)</span>.*?rpic".*?src="(.*?)" ' +
                         '</tr>', re.S)
    items = re.findall(pattern, html)
    print(items)


def main():
    url = 'https://music.163.com/#/discover/toplist'
    getonepage(url)


if __name__ == '__main__':
    main()
