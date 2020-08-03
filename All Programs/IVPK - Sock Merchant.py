#!/usr/bin/env python
# coding: utf-8

# In[3]:


def func():
    N=int(input())
    list1=[""]*N
    c=input()
    list1=list(map(int,c.split()))
    list2=list(set(list1))
    list2.sort()
    list3=[""]*len(list2)
    for i in range(0,len(list2)):
        list3[i]=list1.count(list2[i])
    c=0
    for j in range(0,len(list3)):
        if list3[j]>2:
            if list3[j]%2==0:
                c=c+(list3[j]//2)
            else:
                c=c+((list3[j]-1)//2)
        if list3[j]==2:
            c=c+1
    print(c)
func()


# In[ ]:




