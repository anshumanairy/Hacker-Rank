#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def func():
    K=int(input())
    list1=list(map(int,input().split()))
    list2=list(set(list1))
    for i in range(len(list1)):
        c=list1.count(list2[i])
        if(c==1):
            print(list2[i])
            break
func()


# In[9]:


from collections import Counter
def func():
    K=int(input())
    list1=list(map(int,input().split()))
    c=Counter(list1)
    for i in c:
        if(c[i]==1):
            print(i)
func()


# In[ ]:




