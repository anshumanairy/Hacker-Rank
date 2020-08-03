#!/usr/bin/env python
# coding: utf-8

# In[12]:


def func():
    T=int(input())
    list1=[]
    for i in range(T):
        n=input()
        try:
            n=float(n)
            if n*1==0:
                list1.append(False)
            else:
                list1.append(True)
        except:
            list1.append(False)
    print(*list1,sep='\n')
func()


# In[ ]:




