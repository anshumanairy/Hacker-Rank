#!/usr/bin/env python
# coding: utf-8

# In[13]:


def func():
    N=int(input())
    for i in range(1,N+1):
        for j in range(1,N+1):
            if(j>(N-i)):print("#",end="")
            else:print(end=" ")
        print("\n",end="")
func()

