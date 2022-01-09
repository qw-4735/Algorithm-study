# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 00:28:14 2022

@author: qwuni
"""

# 거스름돈

n = int(input())
count = 0
left = 1000-n

coin_types = [500,100,50,10,5,1]
for coin in coin_types:
    count += left//coin 
    left %= coin  
   
print(count)    




입력예시 
380

출력예시
4