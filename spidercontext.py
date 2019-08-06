import requests
from bs4 import  BeautifulSoup
import re
import os
import random
from multiprocessing import process,pool
def getcontext(url):
    f = requests.get(url);
    #print(f.content.decode());
    reg = '<div class="p">(.*?)<p></p>';
    textlist = re.compile(reg,re.DOTALL).findall(f.content.decode());
    #print(textlist);
    for i in textlist:
        test = re.compile('>(.*?)<')
        aa = test.findall(i);
        root = 'D://test//context4//';
        conetxt = ''.join(aa);
        rand = random.sample('zyxwvutsrqponmlkjihgfedcba', 5)
        name = ''.join(rand)
        path = root  + name + '.txt';
        #print(path)
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            with open(path, "w") as f:
                f.write(conetxt)
                print("爬取完成")
        except Exception as e:
            print("爬取失败:" + str(e))
def getpage():
    url = 'https://www.17k.com/list/2503923.html';
    f = requests.get(url);
    reg = '(/chapter/.*?)"'
    #print(f.content.decode())
    page = re.compile(reg).findall(f.content.decode())
    for p in page:
        url = 'https://www.17k.com' + p;
        getcontext(url);
if __name__ == '__main__':
    getpage();