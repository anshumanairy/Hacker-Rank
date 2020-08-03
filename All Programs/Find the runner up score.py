#!/usr/bin/env python
# coding: utf-8

# In[5]:


def func():
    n=int(input(""))
    c=input("")
    list1=[""]*n
    list1=list(map(int,c.split()))
    set1=set(list1)
    list2=list(set1)
    list2.sort()
    print(list2[len(list2)-2])
func()


# In[ ]:




