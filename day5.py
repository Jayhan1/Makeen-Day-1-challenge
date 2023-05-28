# -*- coding: utf-8 -*-
"""
Created on Sun May 28 23:41:42 2023

@author: Hp
"""

for i in range(1, 6):
    print(" " * (5 - i), end="")
    print("*" * i, end="")
    print(" " *5, end="")
    print("*" * i)

 
print("*****- - -*****")
print("*****- - -*****")

for i in range(5, 0, -1):
    print(" " * (5 - i), end="")
    print("*" * i, end="")
    print(" " * 5, end="")
    print("*" * i)