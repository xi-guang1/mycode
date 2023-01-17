import requests
import re

url = "https://python666.cn/"

res = requests.get(url)
res.encoding = "UTF-8"
text = res.text
a = re.findall(r"""<a class="list-group-item side-color" style="padding-left:30px; color: \#9DAAB6; border-style: none;" href=".*</a>""",text)
with open("test\html\python666所有课程.html","w+",encoding = "UTF-8") as f:
    for az in a:
        az = az.replace(''' class="list-group-item side-color" style="padding-left:30px; color: #9DAAB6; border-style: none;" href="../'''," href=\"https://python666.cn/cls/lesson/")
        f.write(az+"\n")
# print(a)