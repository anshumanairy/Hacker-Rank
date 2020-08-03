#!/usr/bin/env python
# coding: utf-8

# In[13]:


def func():
    s=input("")
    list1=list(s)
    list2=[""]*5
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in range(0,len(s)):
        if list1[i].isalnum()==True:
            a=1
            list2[0]='True'
        if list1[i].isalpha()==True:
            b=1
            list2[1]='True'
        if list1[i].isdigit()==True:
            c=1
            list2[2]='True'
        if list1[i].islower()==True:
            d=1
            list2[3]='True'
        if list1[i].isupper()==True:
            e=1
            list2[4]='True'
    if a==0:
        list2[0]='False'
    if b==0:
        list2[1]='False'
    if c==0:
        list2[2]='False'
    if d==0:
        list2[3]='False'
    if e==0:
        list2[4]='False'
    print(*list2,sep='\n')
func()


# In[12]:


'q'.isalnum()


# In[ ]:




