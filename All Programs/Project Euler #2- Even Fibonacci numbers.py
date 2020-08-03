#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func():
    T=int(input())
    list1=[""]*T
    for i in range(0,T):
        N=int(input())
        a=1
        b=1
        list2=[]
        while(a<N):
            if a%2==0:
                list2.append(a)
            c=a+b
            b=a
            a=c
        s=sum(list2)
        list1[i]=s
    print(*list1,sep='\n')
func()


# In[ ]:




