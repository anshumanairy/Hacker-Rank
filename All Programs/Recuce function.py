#!/usr/bin/env python
# coding: utf-8

# In[27]:


from fractions import Fraction
from functools import reduce
import math
def func():
    list1=[""]*2
    N=int(input(""))
    d=1
    e=1
    for i in range(0,N):
        c=input("")
        a,b=map(int,c.split())
        d=d*a
        e=e*b
    x=math.gcd(d,e)
    list1[0]=int(d/x)
    list1[1]=int(e/x)
    print(*list1,sep=' ')
func()


# In[ ]:




