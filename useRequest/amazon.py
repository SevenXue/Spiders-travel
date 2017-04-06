# -*- coding:utf-8 -*-

# header的使用，避免来源审核

import requests
url = "https://www.amazon.cn/dp/B06Y29LRQY/ref=sr_1_1?s=automotive&ie=UTF8&qid=1491444553&sr=1-1&th=1"

try:
    kv = {'user-agent':'Mozilla/7.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.headers)
except:
    print("error")
