#!/usr/bin/env python
# coding: utf-8

# In[11]:


from itertools import permutations
def func():
    T=int(input())
    l=int(input())
    list1=[]
    list2=[]
    for i in range(l):
        list1.append(int(input()))
    for i in range(0,len(list1)):
        list2=list(set(list(permutations(list1,i+1)))) 
        print(list2)

func()


# # for j in range(0,len(s)):
#         list1=list(set(list(permutations(s,j+1))))
#         for i in range(0,len(list1)):
#             d=''.join(list1[i]) 
