#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
def func():
    N,X=map(int,input().split())
    list1=list(map(float,input().split()))
    for i in range(1,X):
        list2=list(map(float,input().split()))
        list1 = [sum(i) for i in zip(list1,list2)]
    list1=np.divide(list1,X)
    print(*list1,sep='\n')
func()


# In[13]:


def func():
    N,X=map(int,input().split())
    list1=list(map(float,input().split()))
    for i in range(1,X):
        list2=list(map(float,input().split()))
        list1 = [sum(i) for i in zip(list1,list2)]
    for j in range(N):
        list1[j]=list1[j]/X
    print(*list1,sep='\n')
func()


# In[ ]:




