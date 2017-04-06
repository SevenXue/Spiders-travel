# -*- coding:utf-8 -*-

# 使用params关键字！
import requests

kv = {'wd':'Python'}
try:

    r = requests.get("https://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("error")
