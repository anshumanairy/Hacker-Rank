#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import Counter
def func():
    X=int(input(""))
    c=input("")
    list1=[""]*X
    list1=list(map(int,c.split(' ')))
    list1.sort()
    N=int(input(""))
    s=0
    for i in range(0,N):
        d=input("")
        a,b=map(int,d.split(' '))
        r=list1.count(a)
        if(r>0):
            s=s+b
            list1.remove(a)
    print(s)
func()


# In[ ]:




