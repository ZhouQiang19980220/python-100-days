#!/usr/bin/env python
# coding: utf-8

# In[6]:


def isPerfectNumber(num:int):
    start = 1
    stop = num // 2 + 1
    sum = 0
    for i in range(start, stop):
        if num % i == 0:
            sum += i
    return sum == num

perfectNumbers = []
for i in range(1, 10000):
    if isPerfectNumber(i):
        perfectNumbers.append(i)
        
print(perfectNumbers)

