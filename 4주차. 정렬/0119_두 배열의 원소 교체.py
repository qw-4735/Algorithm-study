# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:22:56 2022

@author: qwuni
"""
# 두 배열의 원소 교체

입력예시
5 3
1 2 5 4 3
5 5 6 6 5

출력예시
26


n,k= map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

a.sort()   # 1 2 3 4 5
b.sort(reverse=True)  # 6 6 5 5 5

for i in range(k):  #k=3
    a[i],b[i] = b[i],a[i]   
print(sum(a))