import urllib.request
import random
import time

url = 'http://www.whatismyip.com.tw/'
ip_list = ['101.50.1.1:80', '117.127.0.196:80', '43.252.73.91:80'
          '171.217.92.33:9090', '111.200.57.75:3128', '122.72.18.35:80']
#ip_list = ['117.127.0.196:80']
while True:
    ip = random.choice(ip_list)
    proxy_support = urllib.request.ProxyHandler({'http': ip})
    opener = urllib.request.build_opener(proxy_support)
    header = {'Referer': 'http://www.whatismyip.com',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                            '537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/'
                            '537.36 Core/1.53.4620.400'}
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                                       '537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/'
                                       '537.36 Core/1.53.4620.400')]
    urllib.request.install_opener(opener)
    try:
        print("正在尝试使用%s访问" % ip)
        response = urllib.request.urlopen(url)
    except:
        print("error")
    else:
        print(response.read().decode('utf-8'))
        print("success")
    if input("是否继续") == 'n':
        break

