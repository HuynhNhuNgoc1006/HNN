# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:28:38 2024

@author: LENOVO
"""

print("hello world")
distance=float(input("Nhập độ dài đoạn đường đến trường(m):"))
if distance>1200:
    print("Đường đến trường quá xa.")
else:
    print("Không xác định được xa-gần.")
    if distance<300:
        print("Đường đến trường quá gần. Thôi! Đi bộ")
    elif distance>1200:
        print("Đường đến trường quá xa. Thôi! Đi xe máy")
    elif distance>=300 and distance<=700:
        print("Đường đến trường không xa. Thôi! Đi xe đạp")
    else:
        print("Không xác định")
    
   