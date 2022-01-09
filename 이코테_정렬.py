# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:18:43 2021

@author: qwuni
"""

# 계수 정렬
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]* (max(array) +1)  #모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
for i in range(len(array)):
    count[array[i]] += 1   
for i in range(len(count)):  #0 > 1 > 2 > ... > 9
    for j in range(count[i]):    # for j in range(count[0])  
        print(i, end=' ')

# 선택정렬 : 매번 '가장 작은 것을 선택'
array = [7,5,9,0,3,1,6,2,4,8]        
for i in range(len(array)):
    min_index = i   # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프
print(array)            

# 스와프 : 특정한 리스트가 주어졌을 때 두 변수의위치를 변경하는 작업
array = [3,5]
array[0],array[1] = array[1],array[0]
print(array)

# 삽입정렬 : 삽입 정렬은 특정한 데이터를 적절한 위치에 '삽입' 한다는 의미
# 삽입정렬은 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):  # 삽입 정렬은 두 번째 데이터부터 시작( 첫번째 데이터는 그 자체로 정렬되어 있다고 판단하기 때문)
    for j in range(i, 0, -1): 3 > 2 >1 
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break # 반복을 종료
print(array)            

5,7,9,0 > 5,7,0,9 > 5,0,7,9 > 0,5,7,9

# 퀵 정렬 : 쳣 번째 데이터를 피벗(기준)으로 설정한 다음, 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array):
    if len(array) <= 1 :  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
        return array
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트
    left_side = [x for x in tail if x <= pivot]  #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    return quick_sort(left_side) + [pivot] +quick_sort(right_side)
print(quick_sort(array))

# 파이썬의 정렬 라이브러리
#1 sorded() 함수 : 집합 자료형이나 딕셔너리 자료형을 입력받아도 반환되는 결과는 리스트 자료형
array =[7,5,9,0,3,1,6,2,4,8]
result = sorted(array)
print(result)

#2 sort() : 리스트 변수가 하나 있을 때, 내부 원소를 바로 정렬 / 리스트 객체의 내장함수
array =[7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)

# sorted()나 sort()를 이용할 때 key 매개변수를 입력으로 받는 경우, key값으로는 하나의 함수가 들어가야 하며, 이는 정렬 기준이 된다.
array = [('바나나',2), ('사과', 5) , ('당근',3)]
def setting(data):
    return data[1]  # 각 데이터의 두 번째 원소를 기준으로 설정하는 경우
result = sorted(array, key=setting)
print(result)

# 정렬_위에서 아래로
n = int(input())
import random
list_a=[]
for i in range(n):
    a= random.randint(1,100001)
    print(a)
    list_a.append(a)
print(list_a)    
result = sorted(list_a, reverse=True)
print(result)

# solution
n = int(input())

list_a =[]
for i in range(n):
    list_a.append(int(input()))
result = sorted(list_a, reverse=True)

for i in result:
    print(i, end=' ')

# 정렬_성적이 낮은 순서로 학생 출력하기
n = int(input())
array={'홍길동': 95, '이순신':77}
for i in range(n):
    array.append(str(name),int(score))
for key in array:
    print('{} {}'.format(key, array[key]))  
2
홍길동 95
이순신 77
> 이순신 홍길동    
array = [('홍길동', 95), ('이순신', 77)]
name = str(input())
score = int(input())    
for i in range(n):
    array.append(name, score, end=' ')
def setting(data):
    return data[1]
result= sorted(array, key=setting)
print(result)


