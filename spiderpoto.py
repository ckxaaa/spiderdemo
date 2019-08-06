import requests
from bs4 import  BeautifulSoup
import re
import os
num = 100;
while num < 150:
    url = 'https://pixabay.com/images/search/?pagi=%d' %(num) ;
    f = requests.get(url);
    num = num + 1;
    #soup = BeautifulSoup(f.content,"html.parser");
    #print(f.content.decode())
    reg = '<img srcset="(.*?) 1x,'
    imglist = re.compile(reg).findall(f.text);
    for i in imglist:
        root = 'D://p3//';
        path = root + i.split('/')[-1];
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(i)
                r.raise_for_status()
                print(r.content);
                print(r.raise_for_status())
                # 使用with语句可以不用自己手动关闭已经打开的文件流
                with open(path, "wb") as f:  #开始写文件，wb代表写二进制文件
                    f.write(r.content)
                print("爬取完成")
            else:
                print("文件已存在")
        except Exception as e:
            print("爬取失败:" + str(e))