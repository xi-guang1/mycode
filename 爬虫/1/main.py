import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm


# 模拟浏览器访问
cqjtu_Headers ={ 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
}
#csv的表头
cqjtu_head=["日期","标题"]
#存放内容
cqjtu_infomation=[]
def get_page_number():
    r=requests.get(f"http://news.cqjtu.edu.cn/xxtz.htm",headers=cqjtu_Headers)
    r.raise_for_status()
    r.encoding="utf-8"
    page_array={
    'type':'text/javascript'
    }
    soup = BeautifulSoup(r.text, 'html5lib')
    page_num=soup.find_all('script',page_array)
    page_number=page_num[4].string#只靠标签这些定位好像不是唯一，只能手动定位了
    page_number=page_number.strip('function a204111_gopage_fun(){_simple_list_gotopage_fun(')#删掉除页数以外的其他内容
    page_number=page_number.strip(',\'a204111GOPAGE\',2)}')
    page_number=int(page_number)#转为数字
    return page_number
def get_time_and_title(page_num,cqjtu_Headers):#页数，请求头
    if page_num==66 :
        url='http://news.cqjtu.edu.cn/xxtz.htm'
    else :
        url=f'http://news.cqjtu.edu.cn/xxtz/{page_num}.htm'
    r=requests.get(url,headers=cqjtu_Headers)
    r.raise_for_status()
    r.encoding="utf-8"
    array={#根据class来选择
        'class':'time',
        }
    title_array={
     'target':'_blank'
    }
    page_array={
    'type':'text/javascript'
    }
    soup = BeautifulSoup(r.text, 'html.parser')
    time=soup.find_all('div',array)
    title=soup.find_all('a',title_array)
    temp=[]
    for i in range(0,len(time)):
        time_s=time[i].string
        time_s=time_s.strip('\n                                    ')
        time_s=time_s.strip('\n                                ')
        #清除空格
        temp.append(time_s)
        temp.append(title[i+1].string)
        cqjtu_infomation.append(temp)
        temp=[]
def write_csv(cqjtu_info):
    with open('./2.csv', 'w', newline='',encoding='utf-8') as file:
        fileWriter = csv.writer(file)
        fileWriter.writerow(cqjtu_head)
        fileWriter.writerows(cqjtu_info)
        print('爬取信息成功')
page_num=get_page_number()#获得页数
for i in tqdm(range(page_num,0,-1)):
    get_time_and_title(i,cqjtu_Headers)
write_csv(cqjtu_infomation)