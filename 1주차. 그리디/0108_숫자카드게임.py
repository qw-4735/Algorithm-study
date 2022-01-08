# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:58:41 2022

@author: qwuni
"""

## 숫자 카드 게임
# n: 행의 개수, m: 열의 개수
# 각 행마다 가장 작은 수를 뽑은 뒤, 이중 가장 큰 수를 고르기

입력예시
3 3
3 1 2
4 1 4
2 2 2

출력예시
2


# solution
n,m = map(int, input().split())

result=0

for i in range(3):  # 한 행씩 입력받아 확인
    data = list(map(int, input().split()))  # *** 암기할것 ***
    min_value = min(data)  # 현재 행에서 '가장 작은 수' 찾기
    result = max(result, min_value) # '가장 작은 수'들 중에서 가장 큰 수 찾기
print(result)    