#!/usr/bin/env python
# coding: utf-8

# In[8]:


def func():
    T=int(input())
    list1=[""]*T
    for i in range(0,T):
        N=int(input())
        sum1=(N*(N+1)//2)**2
        sum2=N*(N+1)*(2*N+1)//6
        list1[i]=sum1-sum2
    print(*list1,sep='\n')
func()


# In[ ]:




