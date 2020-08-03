#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict,Counter
def func():
    n,m=map(int,input().split())
    d=defaultdict(list)
    list1=[]
    for i in range(1,n+1):
        c=input()
        d[c].append(i)
    for i in range(m):
        list1.append(input())
    for i in list1:
        if i in d:
            print(" ".join(map(str,d[i])))
        else:
            print(-1)
func()


# In[ ]:




