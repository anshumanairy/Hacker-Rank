#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy
def func():
    c=input("")
    N,M=map(int,c.split())
    a=[]
    for i in range(0,N):
        d=input("")
        list1=[""]*M
        list1=list(map(int,d.split()))
        b=numpy.array(list1)
        a.append(b)
    a=numpy.array(a)
    t=numpy.transpose(a)
    t.shape=(M,N)
    f=a.flatten()
    print(t)
    print(f)
func()

