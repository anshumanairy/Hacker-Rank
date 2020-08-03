#!/usr/bin/env python
# coding: utf-8

# In[17]:


def func():
    N=int(input(""))
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    for i in range(0,N):
        c=input("")
        d=float(input(""))
        list1.append(c)
        list2.append(d)
    list3=list(zip(list2,list1))
    list3.sort()
    list2.sort()
    list4=list(set(list2))
    list4.sort()
    a=list4[1]
    for j in range(0,N):
        if list3[j][0]==a:
            list5.append(list3[j][1])
    print(*list5,sep='\n')
func()


# In[ ]:




