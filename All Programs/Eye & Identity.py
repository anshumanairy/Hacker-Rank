#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy
def func():
    c=input("")
    N,M=map(int,c.split())
    numpy.set_printoptions(sign=' ')
    print(numpy.eye(N, M, k = 0))
func()


# In[ ]:




