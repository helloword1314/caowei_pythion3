# -*- coding: utf-8 -*-

import os
import sys

def Return_Version(): 
    '''版本
    '''
    return sys.version

def Return_Python_EXE_Path():
    '''exe路径
    '''
    return sys.executable

def Return_Current_Working_Path():
    '''当前工作空间
    '''
    return os.getcwd()


def Return_Current_File_Path():
    '''当前文件的路径
    '''
    return os.path.realpath(__file__)

def Return_All_Builtins_Funcitons():
    '''返回python模块的内置函数
    '''
    return dir("__builtins__")

def Say_Something():
    print("python解释器版本------"+Return_Version())
    print("python解释器地址是-----"+Return_Python_EXE_Path())
    print("当前的工作空间是-----"+Return_Current_Working_Path())
    print("当前文件的绝对了路径是-----"+Return_Current_File_Path())

	
if __name__=="__main__":
    print("我自己在运行")
    Say_Something()
else:
    print("别的地方在调用我")
    Say_Something()
  
    

 
