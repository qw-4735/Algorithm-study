# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 19:15:40 2022

@author: qwuni
"""

##큰 수의 법칙
#주어진 수(n개)들을 m번 더하여 가장 큰 수를 만드는 법칙
#단, 연속해서 k번 초과하여 더해질 수 없다.

입력예시
5,8,3

출력예시
2,4,5,4,6

    

# solution
n,m,k = map(int, input().split())  # n,m,k를 공백으로 구분하여 입력받기
data = list(map(int, input().split())) # n개의 수를 공백으로 구분하여 입력받기

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0

while True:
    for i in range(k): # k =3 , m = 8
        if m == 0:  # m =8 > m =7 > m =6
            break
        result += first  # 0 += 6  > 6 + 6  > 6+6+6
        m -= 1   # m =7 > m =6 > m=5
    if m == 0 :   # m =5
        break
    result += second  6+6+6+5
    m -= 1  # m =4
    
print(result)   

 

# 내가 시도한 풀이
n,m,k = map(int, input().split())
data = [2,4,5,4,6]
# 6+6+6+5+6+6+6+5
data.sort(reverse=True)
first = data[0]
second = data[1]
count = 0
result = 0

while count < 9 :
    result = first * k
    count +=k


    
    