#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hundred2grade(score:float):
    grade = ''
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    return grade

while True:
    score = float(input('please input your score:'))
    print(f"your grade is {hundred2grade(score)}")

