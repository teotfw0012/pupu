import json
from time import strftime, sleep

import requests
# 导入

def request_url():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/db1fabfb-0892-4110-95f6-0f55f294358f'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    res = requests.get(url, headers=head)
    dictionary = json.loads(res.text)
    name = dictionary["data"]["name"]
    gg = dictionary["data"]["spec"]
    price = str(int(dictionary["data"]["price"]) / 100)
    marketPrice = str(int(dictionary["data"]["market_price"]) / 100)
    content = dictionary["data"]["share_content"]
    print("-------------商品：" + name + "-------------")
    print("规格：" + gg)
    print("原价：" + price)
    print("原价/折扣价：" + price + "/" + marketPrice)
    print("详细内容：" + content)


def time():
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/db1fabfb-0892-4110-95f6-0f55f294358f'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    res = requests.get(url, headers=head)
    dictionary = json.loads(res.text)
    name = dictionary["data"]["name"]
    price = str(int(dictionary["data"]["price"]) / 100)
    print("-------------" + name + "-------------")
    try:
        while (True):
            currentTime = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + price)
            print(currentTime)
            sleep(5)
    except:
        print("程序结束")


if __name__ == '__main__':
    request_url()
    print("\n")
    time()