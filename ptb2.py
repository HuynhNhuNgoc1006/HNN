# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:04:55 2024

@author: LENOVO
"""
import math
a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
c=float(input("Nhập hệ số c:"))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
            x=-c/b
            print("Phương trình có nghiệm duy nhất")
else:
    denta=b**2-4*a*c
    if denta>0:
        x1=(-b+math.sprt(denta))/(2*a)
        print("Nghiệm thứ nhất",x1)
        x2=(-math.sprt(denta))/(2*a)
        print("Nghiệm thứ hai",x2)
    elif denta==0:
        x=-b/(2*a)
        print("Nghiệm kép",x)
    else:
        print("Vô nghiệm")
      