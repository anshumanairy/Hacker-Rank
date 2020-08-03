#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
def func():
    n=int(input())
    list1=list(set(list(map(int,input().split()))))
    x=sum(list1)
    print(x/len(list1))
func()


# In[5]:


import math
def average(arr):
    list1=list(set(arr))
    return(sum(list1)/len(list1))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[ ]:




