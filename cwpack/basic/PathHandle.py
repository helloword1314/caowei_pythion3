# -*- coding: utf-8 -*-
import os
import sys

 
def Change_Dir_Path(path_input):
    '''修改当前工作目录绝对路径
    '''
    return os.chdir(path_input)

def Back_Upper_Path(strPath):
    '''返回上一级目录
    '''
    return '\\'.join(strPath.split('\\')[:-1])


	
if __name__=="__main__":
    print("我自己在运行")
     
else:
    print("别的地方在调用我")
  
  
    

 
