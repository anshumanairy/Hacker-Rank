#!/usr/bin/env python
# coding: utf-8

# In[3]:


from math import gcd
def func():
    T=int(input())
    list1=[""]*T
    for i in range(0,T):
        N=int(input())
        lcm=1
        for j in range(1,N+1):
            lcm=int(lcm*j/gcd(lcm,j))
        list1[i]=lcm
    print(*list1,sep='\n')
func()

