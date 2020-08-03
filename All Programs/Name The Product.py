#!/usr/bin/env python
# coding: utf-8

# In[22]:


def func():
    N=int(input())
    list1=list(input())
    list3=[]
    for i in range(1,N):
        list2=list(input())
        list1 = [''.join(i) for i in zip(list1,list2)]
    for i in range(5):
        d=122
        for j in range(N):
            if(ord(list1[i][j])==d):
                d=d-1
        list3.append(chr(d))
    print(*list3,sep='')
func()


# In[20]:


c='z'
if ('z'==c):
    a=ord(c)
    a=a-1
    print(chr(a))


# In[ ]:




