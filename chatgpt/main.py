import requests
import json

url = "https://cc-api.sbaliyun.com/completions"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "301",
    "Content-Type": "application/json",
    "Host": "cc-api.sbaliyun.com",
    "Origin": "https://chatgpt.sbaliyun.com",
    "Referer": "https://chatgpt.sbaliyun.com/",
    "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

data = {"frequency_penalty": 0,
        "max_tokens": 2048,
        "model": '"text-davinci-003"',
        "presence_penalty": 0,
        "prompt": '"csDlRcGOwldRZ8OAp6/aQRS3VtiYgKSjCR01GTWOZpWRh8u158s6gVQSZ8PczTU7cZx2CQr+TzQ0wSf0X95/rpAHrdRWCbvgWSmiFrK3A9PZ0gOo2JYSQaS7q2ws1n1fAmq2uD8d7/zLvyAyec2MT9Fa0iSKj/Z5RIVNEC4b7jQ="',
        "temperature": 0.5,
        "top_p": 1
        }

cookie = '__gads=ID=f0caf4729bbcc7bf-22ec4a6904d9006e:T=1671860945:RT=1671860945:S=ALNI_MbHuY14j18g0PcN0kt5WJElGpOLWA; Hm_lvt_05df94d9887ea8acd5a75f70e8a6bb11=1671860944,1672471478; __gpi=UID=00000b96887636f1:T=1671860945:RT=1672471479:S=ALNI_MaUn3ZAkhwOMjQXk-ZDd6vGvPjD3Q; Hm_lpvt_05df94d9887ea8acd5a75f70e8a6bb11=1672476853'

res = requests.post(url,json=json.dumps(data),headers=headers)
print(res.text)