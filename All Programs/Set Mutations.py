#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def func():
    n=int(input())
    list1=set(list(map(int,input().split())))
    N=int(input())
    for i in range(N):
        op,l=map(str,input().split())
        list2=set(list(map(int,input().split())))
        if(op=='intersection_update'):
            list1.intersection_update(list2)
        if(op=='update'):
            list1.update(list2)
        if(op=='symmetric_difference_update'):
            list1.symmetric_difference_update(list2)
        if(op=='difference_update'):
            list1.difference_update(list2)
    print(sum(list1))
func()

