# -*- coding = utf-8 -*-
# @Time : 2020/12/16 下午 02:36
# @File : test2.py
# @Software : PyCharm


from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    req.encoding = 'gbk'
    html = req.text
    div_bf = BeautifulSoup(html, features="lxml")
    div = div_bf.find_all('div', class_='listmain')
    a_bf = BeautifulSoup(str(div[0]), features="lxml")
    a = a_bf.find_all('a')
    f = open("test.txt", "a")  # 以写入的方式打开文件，文件存在则覆盖，文件不存在则新建
    i=0
    for each in a:
        print(i,each.string, server + each.get('href'))
        c = each.string, server + each.get('href')
        f.writelines(c)
        i+=1
    f.close()  # 关闭文件
