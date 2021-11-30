# -*- coding: utf-8 -*-
import os
import sys

 
def Unicode_2_Str(str_input):
    '''
        Unicode转到Str
    '''
    return str_input.encode('gbk')

def Check_Chinese_In_String(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False



	
if __name__=="__main__":
    print("我自己在运行")
     
else:
    print("别的地方在调用我")
  
  
    

 
