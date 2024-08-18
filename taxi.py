# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:15:23 2024

@author: LENOVO
"""

duong=float(input("Hãy nhập quãng đường đi:"))
if duong==1:
    x=20
    print("tiền taxi:",x)
elif duong>1 and duong<=3:
    x=duong*13
    print("tiền taxi:",x)
    
elif duong>=4 and duong<=8:
        x=3*13+(duong-3)*12
        print("tiền taxi:",x)
else:
        x=duong*10
        if x>100:
            x=x*0.92
            print("tiền taxi:",x)
        else:
            print("tiền taxi:",x)
            
        