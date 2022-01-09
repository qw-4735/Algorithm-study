# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 00:50:22 2022

@author: qwuni
"""

# 전자레인지

***
입력예시
100  
출력예시
0 1 4

입력예시
234 
출력예시
-1
***


t =   100
button = [300,60,10]
result = [0]*3


for i in range(3):  
    if t < button[i]:  
        result[i] = 0  
    else:    
        result[i] += (t // button[i])  
        t %= button[i] 

if t >0 :      # ** 결과값이 list와 int 두 가지 경우가 나와, list를 풀어주는 for문을 사용**
    print(-1)
else:
    for i in result:
        print(i, end=' ')
