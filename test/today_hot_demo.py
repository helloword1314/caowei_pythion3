#!/usr/bin/python
# -*- coding:utf-8 -*-
# [url=home.php?mod=space&uid=267492]@file[/url]   : today_hot_demo.py
# [url=home.php?mod=space&uid=238618]@Time[/url]   : 2021/8/5 20:57
import os
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from requests import get
from lxml import etree

sys.path.append(os.getcwd())
import cwpack.basic.FileIOStreamHandle as fileio
 
 
#头文件
lock = threading.Lock()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
 
 
class ShowHotMessage(object):
    def __init__(self):
        self.all_url = {
            '百度实时热点...': 'https://tophub.today/n/Jb0vmloB1G',
            '知乎热榜...': 'https://tophub.today/n/mproPpoq6O',
            '虎嗅热文...': 'https://tophub.today/n/5VaobgvAj1',
            '雪球.......': 'https://tophub.today/n/RrvWOwRv5z',
            '微博热搜...': 'https://tophub.today/n/KqndgxeLl9',
            '微信热搜...': 'https://tophub.today/n/WnBe01o371',
            '头条新闻...': 'https://tophub.today/n/x9ozB4KoXb',
            '抖音热搜...': 'https://tophub.today/n/K7GdaMgdQy',
            '哔哩哔哩全站排行...': 'https://tophub.today/n/74KvxwokxM',
            '豆瓣新片...': 'https://tophub.today/n/mDOvnyBoEB'
        }
 
    def spider(self, hot_url):
        response = get(url=hot_url, headers=HEADERS)
        html = etree.HTML(response.content.decode('utf-8'))
        mt_txt=""
        #print(response.content.decode('utf-8'))
        for oes_title in range(1, 12):
            try:
                title = html.xpath(
                    f'//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[{oes_title}]/td[2]/a//text()')[
                    0]
                hot_index = html.xpath(
                    f'//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[{oes_title}]/td[3]//text()')[
                    0]
                short_title_url = html.xpath(
                    f'//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[{oes_title}]/td[2]/a//@href')[
                    0]
 
                title_url = 'https://tophub.today' + short_title_url
                mt_txt+="<tr><td>"+hot_index+"</td>"+"<td><a href='"+title_url+"' target='_blank' >"+title+"</a></td></tr>"

                #print(' %8s | %26s|%s' % (hot_index, title,title_url))
                #mt_txt = ' %8s | %6s\n' % (hot_index, title)
                
 
            except:
                pass
        return  mt_txt
  


 
def open_html():
    hot = ShowHotMessage()
    list_keys=list(hot.all_url.keys())
    strcontent="<head><title>我的热点</title> <style>body {font-family: 微软雅黑;font-size: 18px;color:gray;} a{color:Brown;font-family: 微软雅黑;font-size: 18px;}</style></head>"
    for top_name in list_keys:
        strcontent+="<br/><br/>"+top_name+"<br/>"
        strcontent+="<table border=1 width='100%'><tr><th style='width:20%'> 热度 </th><th style='width:80%'>新闻</th> </tr>"
        title_url = hot.all_url[top_name]
        strcontent+=hot.spider(hot_url=title_url)
        strcontent+="</table>"
    fileio.Write_Content_To_File(strcontent,"../wwwroot/BaiduNetdiskWorkspace/hot.html")
 
if __name__ == "__main__":
    open_html()