#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func():
    N=int(input())
    list1=list(map(int,input().split()))
    m1=list1[0]
    c=0
    m2=list1[0]
    d=0
    list2=[]
    for i in range(1,N):
        if(list1[i]>m1):
            m1=list1[i]
            c=c+1
        if(list1[i]<m2):
            m2=list1[i]
            d=d+1
    list2.append(c)
    list2.append(d)
    print(*list2,sep=' ')
func()


# In[ ]:




