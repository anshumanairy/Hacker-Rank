#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy
def prg():
    c=input("")
    N,M,P=map(int,c.split())
    c=[]
    d=[]
    for i in range(0,N):
        r=input("")
        list1=[""]*P
        list1=list(map(int,r.split()))
        a=numpy.array(list1)
        c.append(a)
    for j in range(0,M):
        r=input("")
        list2=[""]*P
        list2=list(map(int,r.split()))
        b=numpy.array(list2)
        d.append(b)
    print(numpy.concatenate((c,d)))
prg()


# In[ ]:




