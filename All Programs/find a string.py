#!/usr/bin/env python
# coding: utf-8

# In[5]:


def func():
    a=input("")
    b=input("")
    x=0
    y=len(b)
    for i in range(0,len(a)-y+2):
        x=x+a.count(b,i,i+y)
    print(x)
func()


# In[ ]:




