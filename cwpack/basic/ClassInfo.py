# -*- coding: utf-8 -*-
import os
import sys
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):   #self 代表的是类的实例
        return 'hello world'

    #构造方法在init类实例化时会自动调用
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
# 实例化类
x = MyClass(3,4)
 
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
print(x.r, x.i)   # 输出结果：3.0 -4.5
	
    
if __name__=="__main__":
    print("我自己在运行")   
else:
    print("别的地方在调用我")
  
  
    

 
