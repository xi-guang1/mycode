#!/usr/bin/python3

import requests
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5'
}
def look_up():
    word = input('请输入要查询的单词')
    res = requests.get(f'http://api.tangdouz.com/fy.php?nr={word}',headers=headers)
    res.encoding = 'utf-8'
    print(res.text)
while 1:
    look_up()