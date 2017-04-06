# -*- coding:utf-8 -*-

import requests
import os
import sys
reload(sys)
type = sys.setdefaultencoding('utf8')

root = 'D:/picture/'
url = 'http://image.nationalgeographic.com.cn/2017/0405/20170405033529443.jpg'
path = root + url.split('/')[-1]

#r = requests.get(url)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print(u"文件成功保存")
    else:
        print(u"文件已存在")
except:
    print('error')



