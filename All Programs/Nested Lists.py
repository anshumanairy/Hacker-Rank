#!/usr/bin/env python
# coding: utf-8

# In[6]:


def func():
    N=int(input(""))
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for i in range(0,N):
        c=input("")
        d=float(input(""))
        list1.append(c)
        list2.append(d)
    list3=list2
    list3.sort()
    list3=list(set(list3))
    a=list3[1]
    for j in range(0,N):
        if list2[j]==a:
            list4.append(list1[j])
    list4.sort()
    print(*list4,sep='\n')
func()


# In[ ]:




