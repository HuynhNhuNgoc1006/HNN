# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:23:21 2024

@author: LENOVO
"""

import random
chon=["keo","bua","bao"]
you=input("nhập lựa chọn của bạn(keo,bua,bao):")
computer=random.choice(chon)
print("May:",computer)
if you not in chon:
    print("Lựa chọn của bạn không hợp lệ.")
else:
    if you==computer:
        print("hòa")
    elif(you=="kéo"and computer=="bao")or\
            (you=="búa"and computer=="kéo")or\
            (you=="bao"and computer=="búa"):
                    print("You win")
    else:
                    print("Computer win")