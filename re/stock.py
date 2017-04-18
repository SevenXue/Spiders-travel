import re
import requests
from bs4 import BeautifulSoup
import traceback


def getHTMLtext(url):
    try:
        html = requests.get(url)
        html.raise_for_status()
        html.encoding = html.apparent_encoding
        return html.text
    except:
        return ""


def getStockList(nlst, stockURL):
    html = getHTMLtext(stockURL)
    for line in html:
        reg = re.compile(r"quote.eastmoney.com/(\D+\d+)", re.S)
        number = re.search(reg, line).group(1)
        if len(number) != 0:
            print(number)
        nlst.append(number)

def getStockInfo(lst, stockURL, Fpath):
    print()

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D:/github/The-travelof-Web-Crawlers/re/BaiduStockInfo.txt'
    slist =[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()
