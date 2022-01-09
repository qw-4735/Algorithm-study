# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:18:19 2021

@author: qwuni
"""



N,M = map(int, input().split())
M_list = list(map(int, input().split()))
max = 0

import itertools
result = list(itertools.combinations(M_list, 3))

for i in range(len(result)):
    if max < sum(result[i]) <= M :
        max = sum(result[i])
print(max)