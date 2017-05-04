import re
import requests
from bs4 import BeautifulSoup
import traceback


def getHTMLtext(url, code='utf-8'):
    try:
        html = requests.get(url)
        html.raise_for_status()
        #html.encoding = code
        html.encoding = html.apparent_encoding
        return html.text
    except:
        return ""


def getStockList(nlst, stockURL):
    html = getHTMLtext(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for item in a:
        try:
            href = item.attrs['href']
            nlst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLtext(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a+', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count +=1
                print('\r当前速度{:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count +=1
            print('\r当前速度{:.2f}%'.format(count*100/len(lst)),end='')
            traceback.print_exc()

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D:/github/The-travelof-Web-Crawlers/re/BaiduStockInfo.txt'
    slist =[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()
