#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy
def func():
    c=input("")
    a=numpy.array(list(map(float,c.split())),float)
    b=a[::-1]
    print(b)
func()


# In[ ]:




