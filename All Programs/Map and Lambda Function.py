#!/usr/bin/env python
# coding: utf-8

# In[3]:


def func():
    N=int(input())
    a=0
    b=1
    c=1
    list1=[a]
    for i in range(1,N):
        list1.append(c**3)
        c=a+b
        a=b
        b=c
func()


# In[ ]:




