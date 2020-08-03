#!/usr/bin/env python
# coding: utf-8

# In[3]:


def func():
    c=input("")
    list1=[""]*3
    list1=list(map(int,c.split()))
    d=input("")
    list2=[""]*3
    list2=list(map(int,d.split()))
    a=0
    b=0
    for i in range(0,3):
        if list1[i]>list2[i]:
            a=a+1
        if list1[i]<list2[i]:
            b=b+1
    print(a,b,sep=' ')
func()


# In[ ]:




