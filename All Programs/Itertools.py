#!/usr/bin/env python
# coding: utf-8

# In[5]:


from itertools import product
def func():
    a=input("")
    A=[""]*len(a)
    A=list(map(int,a.split()))
    b=input("")
    B=[""]*len(b)
    B=list(map(int,b.split()))
#     print(tuple(product(A,B)))
    print(*product(A,B))
func()


# In[ ]:




