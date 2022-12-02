import requests
import time
from tqdm import tqdm


t = time.localtime(time.time())
t = time.asctime(t)
url="http://api.tangdouz.com/sjer.php"
headers={
 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"
 }
i=int(input("请输入爬取照片的个数"))


def patupian(x):
    wz=requests.get(url,headers=headers)
    if wz.status_code != 200:
        if wz.status_code == 403:
            print('访问过于频繁，程序已中止，请稍后再试')
        else:
            print(f'未知错误，错误码{wz.status_code}')
        return wz.status_code
    with open(f"./爬取的图片/{t}.html", mode='a+') as file:
        file.write(f"< img src=\"{wz.text}\" alt=\"Smiley face\" width=\"100%\" loading=\"lazy\">\n")
    print(f"第{x}张已完成")
    return

for x in tqdm(range(i)):
    if patupian(x):
        break