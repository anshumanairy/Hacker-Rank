#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def func():
    T=int(input())
    for i in range(T):
        M=int(input())
        list1=set(list(map(int,input().split())))
        N=int(input())
        list2=set(list(map(int,input().split())))
        if(list1.issubset(list2)==True):
            print(True)
        else:
            print(False)
func()

