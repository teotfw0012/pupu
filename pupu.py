import json
from time import strftime, sleep

import requests
# 导入需要的包

def request_url():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/cbfa34f9-9f12-4200-a683-54b53695adb2'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }   #json文件
    res = requests.get(url, headers=head)
    dictionary = json.loads(res.text)
    name = dictionary["data"]["name"]  #名字
    gg = dictionary["data"]["spec"]  #规格
    price = str(int(dictionary["data"]["price"]) / 100)  #价钱
    marketPrice = str(int(dictionary["data"]["market_price"]) / 100)   #市场价
    content = dictionary["data"]["share_content"]  #内容
    print("-------------商品：" + name + "-------------")
    print("规格：" + gg)
    print("原价：" + price)
    print("原价/折扣价：" + price + "/" + marketPrice)
    print("详细内容：" + content)


def time():  #时间
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/cbfa34f9-9f12-4200-a683-54b53695adb2'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    res = requests.get(url, headers=head)
    dictionary = json.loads(res.text)
    name = dictionary["data"]["name"]  #名字
    price = str(int(dictionary["data"]["price"]) / 100)  #价钱
    print("-------------" + name + "-------------")
    try:
        while (True):
            currentTime = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + price)
            print(currentTime)
            sleep(5)
    except:
        print("程序结束")


if __name__ == '__main__':   #主程序
    request_url()
    print("\n")
    time()