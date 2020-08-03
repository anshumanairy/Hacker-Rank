#!/usr/bin/env python
# coding: utf-8

# In[3]:


def func():
    T=int(input())
    sum1=0
    for i in range(0,T):
        N=int(input())
        
        sum1=sum1+N
    sum1=int(sum1/(10**40))
    s=str(sum1)
    c=[]
    r=0
    for digit in s:
        if r<10:
            c.append (int(digit))
        r=r+1
    print(*c,sep='')
func()


# In[ ]:




