#!/usr/bin/env python
# coding: utf-8

# In[9]:


from math import sqrt

def isPrime(num:int):
    # 处理特殊情况
    if num == 1:
        return False
    
    start = 2
    stop = int(sqrt(num)) + 1
    for i in range(start, stop):
        if num % i == 0:
            return False
    return True

num = int(input("please input a number:"))
res = isPrime(num)
print(res)

