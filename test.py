#-*- codeing = utf-8 -*-
#@Time : 2020/12/16 上午 11:14
#@File : test.py
#@Softwore : PyCharm


import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/5403177.html'
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html,features="lxml")
     texts = bf.find_all('div', class_ = 'showtxt')
     print(texts[0].text.replace('\xa0'*8,'\n\n'))