import re
import requests

#~ 关注parsePage()，使用两种不同的正则表达式

def getHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:

        plt = re.findall(r'"view_price":"(\d+\.\d+)"', html)
        tlt = re.findall(r'"raw_title":"(.*?)"', html)
        for i in range(len(plt)):
            price = plt[i]
            title = tlt[i]
            ilt.append([price,title])
        '''
        plt = re.search(r'"view_price":"(\d+\.\d+)"', html)
        tlt = re.search(r'"raw_title":"(.*?)"', html)
        '''
    except:
        print("error")

    '''
    #不同的正则表达式，一样的效果
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            #eval去掉双引号
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("error")
    '''


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(i*44)
            html = getHtmlText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

if __name__ == '__main__':
    main()

