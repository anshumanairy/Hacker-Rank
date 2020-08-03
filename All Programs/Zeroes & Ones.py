#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy
def func():
    c=input("")
    list1=[]
    list1=list(map(int,c.split()))
    print(numpy.zeros(list1,dtype=numpy.int))
    print(numpy.ones(list1,dtype=numpy.int))
func()


# In[ ]:




