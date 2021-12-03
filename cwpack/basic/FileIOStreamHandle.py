# -*- coding: utf-8 -*-
import os
import shutil
import sys
# print(os.getcwd())
sys.path.append(os.getcwd())
from  cwpack.basic.FileFolderHandle import *
 

def Print_Line_In_File(file_input):
    '''读文件
    '''
    if Is_File_Exist(file_input):     
        data_input = open(file_input)
        print(type(data_input))
        for each_line in data_input:
            print(each_line)
        data_input.close()

def Return_Str_In_File(file_input):
    '''返回文件内容
    Args:  
    '''
    if Is_File_Exist(file_input):     
        data_input = open(file_input,"r")
        content_str=data_input.read()
        data_input.close()
        return content_str
        
def Write_Content_To_File(content,file_input):
    '''重新写文件
    Args:  
    '''
    try:
        file_using = open(file_input,'w',errors='ignore')
        file_using.write(content)
        file_using.close()
    except IOError:
        print("写入错误")

def Append_Content_To_File(content,file_input):
    '''重新写文件
    Args:  
    '''
    try:
        file_using = open(file_input,'a')
        file_using.write(content)
        file_using.close()
    except IOError:
        print("写入错误")
 
def Say_Something():
    '''修改
    Args:
        
    '''
    print("人生真是无聊啊！")
	
	
if __name__=="__main__":
    Say_Something()

