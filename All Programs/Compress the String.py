#!/usr/bin/env python
# coding: utf-8

# In[2]:


from itertools import groupby
def func():
    for k,c in groupby(input()):
        print(len(list(c)),int(k),end=" ")
func()


# In[ ]:




