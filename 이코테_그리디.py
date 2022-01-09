# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:25:44 2021

@author: qwuni
"""

n = 1260
count = 0
coin_types = [500,100,50,10]

for coin in coin_types:
    # 500 > 100 > 50 > 10
    count += n//coin  
    #1 count = 1260//500 =2  
    #3 count = 2 + 260//100 = 4
    #5 count = 4 + 60//50 = 5
    #7 count = 5 + 10//10 = 6
    n %= coin 
    #2 n= 1260 % 500 = 260   
    #4 n = 260 % 100 = 60
    #6 n = 60 % 50 = 10
    #8 n = 10 % 10 = 0

print(count)    

# 그리디_큰수의 법칙
n,m,k = map(int, input().split())
n = 5
m = 8
k = 3
data = list(map(int, input().split()))
data = [2,4,5,4,6]
data.sort(reverse=True)
print(data)
first = data[0]
second = data[1]
sol=0  
while True:
    for i in range(1,k+1):
        if m//k >= :
            sol = first * k
8//3 = 2, 8%3 = 2            6+6+6 + 5 + 6+6+6 + 5
for 몫,나머지 in enumerate([m//k, m%k]):
    sol += (first * k * 몫) + (second * 나머지)
print(sol)
secondsmㄴ 무조건 한번 더하기

while True:
    for i in range(k):
        if m//k > 0 and m%k >0:
            sol += first *k +second
        elif

while True:
    for i in range(k):
        if m == 0:
            break
        sol += first 
        m -= 1
    if m == 0:
        break
    sol += second
    m -= 1

print(sol)                

n =17
k =4
count =0
while n >= k:
    if n % k ==0:
        #2 16 % 4 = 0
        #3 4 % 4 = 0
        n = (n // k)
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



        