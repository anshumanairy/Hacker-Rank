#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
def func():
    c=input("")
    N,M=map(int,c.split())
    list1=[""]*M
    a=[]
    z=[]
    for i in range(0,N):
        d=input("")
        list1=list(d)
        b=numpy.array(list1)
        a.append(b)
    a=numpy.array(a)
    t=numpy.transpose(a)
    r=list(t)
    list2=[]
    for j in range(0,M):
        for k in range(0,N):
            list2.append(r[j][k])
    list3=[]
    for l in range(0,M*N):
        if ((list2[l]>='A' and list2[l]<='Z')or(list2[l]>='a' and list2[l]<='z')or(list2[l]>='0' and list2[l]<='9')):
            list3.append(list2[l])
        else:
            if ((list2[l-1]>='A' and list2[l-1]<='Z')or(list2[l-1]>='a' and list2[l-1]<='z')or(list2[l-1]>='0' and list2[l-1]<='9'))and((list2[l+1]>='A' and list2[l+1]<='Z')or(list2[l+1]>='a' and list2[l+1]<='z')or(list2[l+1]>='0' and list2[l+1]<='9')):
                list3.append(' ')
            else:
                list3.append(list2[l])
func()


# In[ ]:




