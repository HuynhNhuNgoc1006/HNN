# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:58:27 2024

@author: LENOVO
"""

import math
a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
c=float(input("Nhập hệ số c:"))
if a==b==c:
            print("Là tam giác điều")
elif a==b or a==c or b==c:
            print("Là tam giác cân")
elif a**2+b**2==c**2:
            print("Là tam giác vuông")
else: print("Là tam giác thường")
      