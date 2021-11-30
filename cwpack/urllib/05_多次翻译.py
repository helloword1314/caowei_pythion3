import urllib.request
import urllib.parse
import json
import time


url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://www.youdao.com/"
while True:
    content = input("输入要翻译的内容：")
    if content == 'q':
        break
    header = {'Referer': 'http://fanyi.youdao.com',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                            '537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/'
                            '537.36 Core/1.53.4620.400'}
    data = {}
    data["type"] = "AUTO"
    data["i"] = content
    data["doctype"] = 'json'
    data["version"] = "2.1"
    data["keyfrom"] = 'fanyi.web'
    data["typoResult"] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data, header)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    # print(html)
    target = (json.loads(html))
    print(target['translateResult'][0][0]['tgt'])
    # print(req.headers)
    time.sleep(5)

