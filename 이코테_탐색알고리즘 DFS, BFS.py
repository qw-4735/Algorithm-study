# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:09:38 2021

@author: qwuni
"""

# 이코테_탐색알고리즘 DFS/BFS
# DFS 예제

# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end= ' ')
    for i in graph[v]:   # 현재 노드아 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i , visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [[], [2,3,8], [1,7], [1,4,7], [3,5], [3,4], [7], [2,6,8], [1,7]] 

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9           

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)   # 1 2 7 6 8 3 4 5

# 이코테_음료수 얼려 먹기

n,m = map(int,input().split())
00110
00011
11111
00000
graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
icecream = 0

for i in range(n):
    graph.append(list(map(int, input())))
def dfs(x,y):
    if x < 1 or x > n or y < 1 or y > m:
        return False
    while graph[x][y] == 0:
          graph[x][y] = 1
          dfs(x+1,y)
          dfs(x-1,y)
          dfs(x,y+1)
          dfs(x,y-1)
          return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            icecream += 1
print(icecream)            
            


# BFS 예제 : 가까운 노드부터 탐색
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])  # 큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True  # 현재 노드를 방문 처리
    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력
        print(v, end=' ')
        for i in graph[v]:  # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [[], [2,3,8], [1,7], [1,4,7], [3,5], [3,4], [7], [2,6,8], [1,7]] 

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9           

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)  # 1 2 3 8 7 4 5 6



# 이코테_미로탈출
n,m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x,y):
    if x < 1 or y < 1 or x > n or y > m:
        return False
    if graph[x][y] == 1:
        result += 1
        bts(x,y+1) 
        bfs(x+1,y)
        return result-1
        return True
    return False

print(result)











