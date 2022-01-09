# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:26:01 2021

@author: qwuni
"""

n = int(input())
count = []
max_x = 0
max_y = 0

for i in range(n):
    x,y = tuple(map(int, input().split()))
    if x[i] > max_x:
        max_x = x[i]
    else:
        count[i] +=1
        continue
        if y[i] > max_y:
            max_y = y[i]
        else:    
            count[i] += 1

print(count) # 2 2 1 2 5     

5
55 185
58 183
88 186
60 175
46 155      
만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.
count = [1 for i in range(5)]

for i in range(n):
    #1 0 > 1 >2 >3 >4
    if x[i] > max_x:
        max_x = x[i]
        #2 max_x = x[0]=55
        #4 max_x = x[1] = 58
        #6 max_x = x[2] = 88
    else:
        count[i] +=1
        #8 count[3] = 1 + 1 =2
        #9 count[4] = 1 + 1 =2
        continue
        if y[i] > max_y:
            max_y = y[i]
            #3 max_y = y[0] = 185
            #7 max_y = y[2] = 186
        else:
            count[i] += 1
            count[i-1] 
            #5 count[1] = 2
# count[0]= 1  > count[1] =2 > count[2] =1 > count[3] =2 > count[4] =2
print(count) # 2 2 1 2 5  

55 185
58 183
88 186
60 175
46 155  
x,y = list(map(int, input().split()))
count = [1 for i in range(5)]
만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.

for i in range(n):
    x,y = list(map(int, input().split()))
    max_x = 0
    max_y = y[i0
    if x[i] > max_x:
        max_x = x[i]
    if y[i] > max_y:
        max_y = y[i]
print(max_x, max_y)   

for i in range(n):
    if x[i] < max_x:
        
        
        
######
n = int(input())     
count = [1 for i in range(5)]      
55 185
58 183
88 186
60 175
46 155 
n_list = []
for i in range(n):
    x,y = map(int, input().split())
    n_list.append((x,y))
for j in n_list:
    for k in n_list:
        if x[j] < x[k] and y[j] < y[k]:
            count[j] += 1
    print(count, end=' ')
for i in count:
    print(i , end= ' ')     


###############################################

# solution1
n = int(input())     
counts = [1 for i in range(5)] 
person = [] 
for i in range(n):
    x,y = map(int, input().split())
    person.append((x,y))
    
for j in range(n):
    for k in range(n):
        if person[j][0] < person[k][0] and person[j][1] < person[k][1]:
            counts[j] += 1
            
for count in counts:
    print(count, end=' ')


# solution2 (다은님 풀이)
import sys

n = int(sys.stdin.readline())
x = [0 for i in range(n)]   # x = []      
y = [0 for i in range(n)]   # y = []
counts = [1 for i in range(n)]

for i in range(n):
    x[i],y[i] = map(int, sys.stdin.readline().split())
    
for j in range(n):
    for k in range(n):
        if x[j] < x[k] and y[j] < y[k]:
            count[j] += 1

for count in counts:
    print(count, end=' ')    





















for i in range(n):
    max_x = x[i]
    max_y = y[i]
    if x[i+1] > max_x:
        max_x = x[i+1]
        #1 max_x = x[1] = 58
        #3 max_x = x[2] = 88
    else: 
        max_x = x[i]
        #6 max_x = x[2] = 88
        continue
        if y[i+1] > max_y:
            max_y = y[i+1]
            #4 max_y = y[2] =186
            count[i-1] += 1
            count[i] += 1
            #5 count[0] = 2 / count[1] = 2
        else: 
            max_y = y[i]
            #2 max_y = y[0] = 185
count[0] = 1 >     