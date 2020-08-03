#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func():
    N=int(input(""))
    list1=[""]*N
    list2=[""]*N
    list3=[""]*N
    for i in range(0,N):
        c=input("")
        list1=list(map(str,c.split()))
        s=float(list1[1])+float(list1[2])+float(list1[3])
        list2[i]=list1[0]
        list3[i]=s/3
    d=input("")
    for j in range(0,N):
        if list2[j]==d:
            print("%.2f" % list3[j])
func()


# In[ ]:




