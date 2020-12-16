#-*- codeing = utf-8 -*-
#@Time : 2020/12/16 下午 05:05
#@File : test4.py
#@Softwore : PyCharm

import requests
import time
from tqdm import tqdm
from multiprocessing import Process, Lock, Queue,Pool
from functools import  partial
from bs4 import BeautifulSoup

def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0'*4)
    return content

def init(l):
    global lock #定义lock为全局变量，供所有进程用
    lock = l
if __name__ == '__main__':
    server = 'https://www.xsbiquge.com'
    book_name = '诡秘之主.txt'
    target = 'https://www.xsbiquge.com/15_15338/'
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')

        lock = Lock()
        pool = Pool(processes=20, initializer=init, initargs=(lock,))  # 设定进程数为20
        pool.map(partial(get_content, target=url))  # 利用偏函数传递多个参数给get_content函数
        pool.close()
        pool.join()

        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')