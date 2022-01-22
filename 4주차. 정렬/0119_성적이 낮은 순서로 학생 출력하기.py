# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 17:50:05 2022

@author: qwuni
"""

# 성적이 낮은 순서로 학생 출력하기

2
홍길동 95
이순신 77

> 이순신 홍길동 
  

# solution
n = int(input())
array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])) ) # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장

array = sorted(array, key= lambda student: student[1])

for studenet in array:
    print(student[0], end=' ')
    




# 람다 표현식 : 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징
def add(a,b):    # 함수 이용한 일반적인 add() 메서드 사용
    return a + b
print(add(3,7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a,b : a+b)(3,7))




