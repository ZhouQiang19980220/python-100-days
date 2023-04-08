#!/usr/bin/env python
# coding: utf-8

# In[9]:
import os
import time

def main():
    content = '北京欢迎您'.center(50, ' ')
    while True:
        print(content)
        time.sleep(0.1)
        os.system('clear')
        content = content[1:] + content[0]
    


if __name__ == '__main__':
    main()