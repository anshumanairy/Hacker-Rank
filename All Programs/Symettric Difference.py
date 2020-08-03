#!/usr/bin/env python
# coding: utf-8

# In[3]:


def func():
    m=int(input())
    a=set(list(map(int,input().split())))
    n=int(input())
    b=set(list(map(int,input().split())))
    c=a.difference(b)
    d=b.difference(a)
    e=list(c.union(d))
    e.sort()
    print(*e,sep='\n')
func()


# In[ ]:




