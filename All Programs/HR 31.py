#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
def func():
    c=input()
    n,k=map(int,c.split())
    list1=[""]*k
    d=input()
    list1=list(map(int,d.split()))
    list2=list(set(list1))
    list2.sort()
    s=0
    for i in range(0,len(list2)-1):
        y=list1.count(list2[i])
        z=list2[i]*y
        s=s+(z/2)    
    print(s)
func()


# In[ ]:




