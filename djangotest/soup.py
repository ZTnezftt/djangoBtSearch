from lxml import etree
import json
from urllib.parse import quote
from urllib import request


# 解析的方法

# obj dict
# name 搜索的名字
# sort 排序方式 date or sort
# page 页码
def parse(obj, name, sort, page):
    print("--------开始解析----------")
    url = obj['url'].format(name="" + quote(name, encoding='utf-8'),
                            sort=obj['dateSort'] if sort == 'date' else obj['sizeSort'], page=page)
    print(url)
    r = request.Request(url)

    r.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                               'AppleWebKit/536.26 (KHTML, like Gecko)'
                               ' Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(r) as res:
        data = res.read().decode()

    html = etree.HTML(data)

    itemListPath = obj['itemListPath']
    itemTitle = obj['itemTitle']
    itemSize = obj['itemSize']
    itemHot = obj['itemHot']
    itemDate = obj['itemDate']
    itemTorrent = obj['itemTorrent']

    itemList = html.xpath(itemListPath)

    data = []
    for i in itemList:
        try:
            item = {}
            title = i.xpath(itemTitle)[0].xpath('string()')
            size = i.xpath(itemSize)[0].replace('\\xa0', '')
            hot = i.xpath(itemHot)[0].replace('\\xa0', '')
            date = i.xpath(itemDate)[0].replace('\\xa0', '')
            torrent = i.xpath(itemTorrent)[0] + ""
            item['title'] = title
            item['size'] = size
            item['hot'] = hot
            item['date'] = date
            item['torrent'] = torrent
            data.append(item)
        except Exception:
            continue
    res = {}
    res['status'] = 200
    res['data'] = data
    return json.dumps(res)


def init():
    res = {}
    data = []
    # 返回状态
    res["status"] = 200
    # 数据数组
    res["data"] = data

    # 构建解析字典
    dict1 = {}
    dict1["url"] = "http://www.btsou5.net/list/{name}/{page}/{sort}"
    dict1["title"] = "bt"
    dict1["itemListPath"] = "/html/body//ul[@class='mlist']/li"
    dict1['itemTitle'] = ".//div[@class='T1']/a"
    dict1['itemSize'] = "./dl//span[1]/text()"
    dict1['itemHot'] = "./dl//span[4]/text()"
    dict1['itemDate'] = "./dl//span[3]/text()"
    dict1['itemTorrent'] = "./div[@class='dInfo']/a[1]/@href"
    dict1['dateSort'] = "time_d"
    dict1['sizeSort'] = "size_d"
    data.append(dict1)
    return json.dumps(res)  # 转化成json
