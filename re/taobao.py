import re
import requests

def getHtmlText(url):
    print()

def parsePage(ilt, html):
    print()

def printGoodsList(ilt):
    print()

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
            
