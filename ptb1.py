# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:57:32 2024

@author: LENOVO
"""
import math
a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
if a==0:
    if b==0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Phương trình có nghiệm duy nhất x:",x)
        
        

   
       
   
    
