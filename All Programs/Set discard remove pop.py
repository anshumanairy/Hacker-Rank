#!/usr/bin/env python
# coding: utf-8

# In[2]:


def func():
    n=int(input())
    list1=set(list(map(int,input().split())))
    N=int(input())
    for i in range(0,N):
        list2=list(map(str,input().split()))
        if list2[0]=='discard':
            list1.discard(int(list2[1]))
        try:
            if list2[0]=='pop':
                list1.pop()
            if list2[0]=='remove':
                 list1.remove(int(list2[1]))
        except KeyError as e:
            pass
    print(sum(list1))
func()


# In[ ]:




