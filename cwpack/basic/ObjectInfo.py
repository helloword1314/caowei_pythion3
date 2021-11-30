# -*- coding: utf-8 -*-
import os
import sys

def Return_Properties_Of_Object(obj):
    '''返回对象的所有属性方法
    '''
    return dir(obj)

def Does_Object_Belong_Class(obj_input,class_input):
    '''对象是否是这个类的实例     
    '''
    return isinstance(obj_input,class_input)

def Say_Something():
    print("python解释器版本------"+())
 
a=[1,2,3]
print(Does_Object_Belong_Class(a,int))
	
if __name__=="__main__":
    print("我自己在运行")
     
else:
    print("别的地方在调用我")
  
  
    

 
