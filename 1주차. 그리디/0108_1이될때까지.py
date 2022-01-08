# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 23:10:10 2022

@author: qwuni
"""

## 1이 될때까지
# n이 1이 될때까지 다음의 두 과정 중 하나를 선택가능
# 1) n에서 1을 뺀다.
# 2) n을 k로 나눈다. ( n % k = 0 일때만 가능)

입력예시 
25 5

출력예시
2


#내가 푼 풀이
n =17
k =4
count =0
while n >= k:
    if n % k ==0:
        n = (n // k)
        count +=1
    else:    
        n = (n-1)
        count +=1

print(count)  






n =17
k =4
count =0
while n >= k:3
    if n % k ==0:   #나머지
        #2 16 % 4 = 0
        #3 4 % 4 = 0
        n = (n // k)   #몫
        #2 n = 16 // 4 = 4
        #3 n = 4 // 4 = 1
        count +=1
        #2 count = 2
        #3 count = 3
    else:
        #1 17 % 4 = 1
        n = (n-1)
        #1 n = 17-1
        count +=1
        #1 count =1

print(count)        


