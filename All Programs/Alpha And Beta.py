#!/usr/bin/env python
# coding: utf-8

# In[4]:


def func():
    N=int(input())
    list1=list(set(list(map(int,input().split()))))
    list1.sort()
    if (len(list1)>1):
        c=list1[len(list1)-2]
        print(c)
    else:
        print(0)
func()


# In[ ]:




