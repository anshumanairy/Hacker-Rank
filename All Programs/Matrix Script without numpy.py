#!/usr/bin/env python
# coding: utf-8

# In[15]:


import itertools
import re
def func():
    a=input("")
    N,M=map(int,a.split())
    list1=[""]*3
    list2=[]
    for i in range(0,N):
        b=input("")
        list1=list(b)
        list2.append(list1)
    list2=list(zip(*list2))
    list2=(list(itertools.chain.from_iterable(list2)))
    list2.insert(0,' ')
    list2.insert(len(list2)+1,' ')
    list3=[]
    list4=[]
    
#     y = ( x > 6 ) ? 8 : 27
    for j in range(1,(N*M)+1):
        if (list2[j].isalnum()==True):
            if len(list4)>0:
                list3.append(' ')
                list4=[]
            list3.append(list2[j])
        else:
            list4.append(list2[j])
            
    if len(list4)>0:
        list3.extend(list4)
    print(*list3,sep='')
func()


# In[ ]:




