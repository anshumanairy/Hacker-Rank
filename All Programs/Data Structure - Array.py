#!/usr/bin/env python
# coding: utf-8

# In[3]:


def func():
    N=int(input())
    list1=[""]*N
    c=input("")
    list1=list(map(int,c.split()))
    list1.reverse()
    print(*list1,sep=' ')
func()


# In[ ]:




