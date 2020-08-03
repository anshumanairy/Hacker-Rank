#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
def func():
    n,m=map(int,input().split())
    list1=[]
    list2=[]
    for i in range(0,n):
        list3=list(map(int,input().split()))
        a = numpy.array(list3,)
        list1.append(a)
    for i in range(0,n):
        list3=list(map(int,input().split()))
        a = numpy.array(list3,)
        list2.append(a)
    c="["
    d="]"
    for i in range(0,n):
        print(numpy.add(list1[i],list2[i]))
        print(numpy.subtract(list1[i],list2[i]))
        print(numpy.multiply(list1[i],list2[i]))
        print(list1[i]//list2[i])
        print(numpy.mod(list1[i],list2[i]))
        print(numpy.power(list1[i],list2[i]))
func()


# In[ ]:




