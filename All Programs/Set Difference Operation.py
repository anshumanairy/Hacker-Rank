#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def func():
    M=int(input())
    list1=set(list(map(int,input().split())))
    N=int(input())
    list2=set(list(map(int,input().split())))
    print(len(list1.difference(list2)))
func()

