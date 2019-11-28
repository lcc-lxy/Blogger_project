'''
模拟30个请求
随机发给: http://127.0.0.1:8000/test/
        http://127.0.0.1:8000/test/
        http://127.0.0.1:8000/test/
        http://127.0.0.1:8000/test/
'''
import random
from threading import Thread
import requests
# from multiprocessing import process
#线程事件函数 - 随机向8000或8001发请求
def get_request():
    url = 'http://127.0.0.1:8000/test'
    url1 = 'http://127.0.0.1:8001/test'
    get_url = random.choice([url,url1])
    #真正发请求
    html = requests.get(get_url).text
    print(html)
t_list = []
for i in range(30):
    t =Thread(target=get_request)
    t_list.append(t)
    t.start()
for t in t_list:
    t.join()
import time
def f1():
    time.sleep(1)
    print(1)
t_list = []
for i in range(30):
    t =Thread(target=f1)
    t_list.append(t)
    t.start()
for t in t_list:
    t.join()

