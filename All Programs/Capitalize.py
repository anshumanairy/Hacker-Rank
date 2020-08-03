#!/usr/bin/env python
# coding: utf-8

# In[9]:


def func():
    S=input("")
    S=S+" "
    list1=list(S)
    if list1[0].isalpha():
        list1[0]=list1[0].upper()
    for i in range(1,len(S)-1):
        if list1[i]==' ':
            if list1[i+1].isalpha():
                list1[i+1]=list1[i+1].upper()
    list1.pop()
    print(*list1,sep='')
func()


# In[ ]:




