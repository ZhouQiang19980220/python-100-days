#!/usr/bin/env python
# coding: utf-8

# In[13]:


def add(a, b, *args, **kwargs):
    res = 0
    for arg in args:
        res += arg
    return res

l = [i for i in range(10)]
print(add(1, 2, 3, 4, c=1, d=2))


# In[15]:


def fun():
    a = 1
    def bar():
        nonlocal a
        a = 2
    bar()
    print(f'a = {a}')
fun()

