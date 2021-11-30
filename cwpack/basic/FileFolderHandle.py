# -*- coding: utf-8 -*-
import os
import shutil
import sys

def Is_File_Exist(file_input):
    '''文件是否存在
    '''
    return os.path.exists(file_input)

def Copy_File(from_file,to_folder):
    '''复制文件到另一个文件夹
       to_folder可以是文件，也可以是文件夹
    '''
    shutil.copy(from_file,to_folder)

def Copy_Folder(from_folder,to_folder):
    '''复制文件夹到另一个文件夹，to_folder名称必须不存在
    '''
    shutil.copytree(from_folder,to_folder)

def Move_FileFolder(from_folder,to_folder):
    '''移动文件或者文件夹A到文件夹B，
       如果B不存在，相当于把A改成B的名字
       如果B存在，把A放进去
    '''
    shutil.move(from_folder,to_folder)

def Delete_FileFolder(filefolder):
    '''删除文件或者文件夹
    '''
    if os.path.isfile(filefolder):
        os.remove(filefolder)
    elif os.path.isdir(filefolder):
        shutil.rmtree(filefolder)

def Rename_FileFolder(from_folder,to_folder):
    '''修改文件或者文件夹名称，
    '''
    os.rename(from_folder,to_folder)


def Delete_ALL_In_Folder(folder_input):
    '''删除目录下面所有文件
    '''
    for f in os.listdir(folder_input):
        file_path = os.path.join(folder_input,f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def Delete_Startswith_In_Folder(folder_input,startswith_str):
    '''删除以某某开头的文件
    Args:
        startswith_str是某某开头
    '''
    for f1 in os.listdir(folder_input):
        file_path = os.path.join(folder_input,f1)
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            if file_name.find(startswith_str)>-1:
                os.remove(file_path)
        elif os.path.isdir(file_path):
            Delete_Startswith_In_Folder(file_path,startswith_str)

def Delete_Except_Startswith_In_Folder(folder_input,startswith_str):
    '''删除以某某开头的文件之外的文件
    Args:
        startswith_str是某某开头
    '''
    for f1 in os.listdir(folder_input):
        file_path = os.path.join(folder_input,f1)
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            if file_name.find(startswith_str)==-1:
                os.remove(file_path)
        elif os.path.isdir(file_path):
            Delete_Except_Startswith_In_Folder(file_path,startswith_str)

def Delete_SOME_TYPE_In_Folder(folder_input,kind_array):
    ''' 删除多种特定类型文件
        kind_array是[".txt",".abc"]
    '''
    for f1 in os.listdir(folder_input):
        file_path = os.path.join(folder_input,f1)
        if os.path.isfile(file_path):
            for kind_filter in kind_array:
                if file_path.endswith(kind_filter):
                    os.remove(file_path)
        elif os.path.isdir(file_path):
            Delete_SOME_TYPE_In_Folder(file_path,kind_array)


    
def Say_Something():
    '''修改
    '''
    print("人生真是无聊啊！")
	
	
if __name__=="__main__":
    print("1-删除所有的文件")
    print("2-删除特定类型的文件")
    print("3-删除某某开头的文件")
    print("4-删除某某开之外的文件")
    print("5-移动文件夹")
    while True :
        method_file= input("what do you want:")
        if method_file== "1":
            path_input = input("input folder:")
            Delete_ALL_In_Folder(path_input)
            print("-------------------all deleted------------------")
        elif method_file== "2":
            path_input = input("input folder:")
            kind_type = input("input kind,such as '.USX' :")
            kind_filters=[kind_type]
            Delete_SOME_TYPE_In_Folder(path_input,kind_filters)
            print("-------------------all deleted------------------")
        elif method_file== "3":
            path_input = input("input folder:")
            capital = input("input capital,such as 'tttt' :")
            Delete_Startswith_In_Folder(path_input,capital)
            print("-------------------all deleted------------------")
        elif method_file== "4":
            path_input = input("input folder:")
            capital = input("input capital,such as 'tttt' :")
            Delete_Except_Startswith_In_Folder(path_input,capital)
            print("-------------------all deleted------------------")
        elif method_file== "5":
            from_folder = input("from folder:::::")
            to_folder = input("to folder::::")
            Copy_Folder_To_Another_Folder(from_folder,to_folder)
            print("-------------------all deleted------------------")
         
         
