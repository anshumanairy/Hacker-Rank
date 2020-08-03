#!/usr/bin/env python
# coding: utf-8

# In[34]:


from itertools import combinations
def func():
    T=int(input())
    for i in range(T):
        N,P=map(int,input().split())
        list1=list(map(int,input().split()))
        c=list1[0]
        for k in range(2,N):
            list3=list(set(list(combinations(list1,k))))
            for j in range(len(list3)):
                d=(list3[j][0] & list3[j][1])
                if d<c:
                    c=d
        print(abs(c-P))
func()


# In[3]:


import numpy
def func():
    T=int(input())
    for i in range(T):
        N,P=map(int,input().split())
        list1=list(set(list(map(int,input().split()))))
        c=list1[0]
        for k in range(1,N):
            for j in range(len(list1)-i,i):
                if list1[j]<=list1[j+i]:
                    if (numpy.bitwise_and(list1[j:j+i]))<c:
                        c=numpy.bitwise_and(list1[j:j+i])
        print(abs(c-P))
func()


# In[53]:


6&7


# In[40]:


2&2


# In[41]:


3&3


# In[ ]:




