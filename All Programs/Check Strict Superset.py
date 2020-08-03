#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def func():
    list1=set(list(map(int,input().split())))
    N=int(input())
    c=0
    for i in range(N):
        list2=set(list(map(int,input().split())))
        if(list1.intersection(list2)==list2):
            c=c+1
    if(c==N):
        print("True")
    else:
        print("False")
func()

