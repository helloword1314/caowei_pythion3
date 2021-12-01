import urllib.request

url = 'http://www.whatismyip.com.tw/'
proxy_support = urllib.request.ProxyHandler({'http': '117.127.0.196:80'})
opener = urllib.request.build_opener(proxy_support)

opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                                       '537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/'
                                       '537.36 Core/1.53.4620.400')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
print(response.read().decode('utf-8'))

