#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
def func():
    list1=[]
    T=int(input())
    for i in range(T):
        c=input()
        d="True"
        try:
            reg=re.compile(c)
        except re.error:
            d="False"
        list1.append(d)
    print(*list1,sep='\n')
func()

