#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def func():
    a=input()
    list1=set(list(map(int,input().split())))
    b=input()
    list2=set(list(map(int,input().split())))
    print(len(list(list1.intersection(list2))))
func()

