#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func():
    T=int(input())
    list1=[""]*T
    for i in range(0,T):
        c=input()
        N,K=map(int,c.split())
        list2=[""]*N
        d=input()
        list2=list(map(int,d.split()))
        k=0
        for j in range(0,N-K-1):
            p=list2[j]+list2[j+1]+list2[j+2]+list2[j+3]+list2[j+4]
            if p>k:
                k=p
        list1[i]=k
    print(*list1,sep='\n')
func()


# In[ ]:




