import urllib.request
import urllib.parse
import json

content=input("输入要翻译的内容：")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://www.youdao.com/"
data = {}
data["type"] = "AUTO"
data["i"] = content
data["doctype"] = 'json'
data["version"] = "2.1"
data["keyfrom"] = 'fanyi.web'
data["typoResult"] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
#print(html)
target = (json.loads(html))
print(target['translateResult'][0][0]['tgt'])