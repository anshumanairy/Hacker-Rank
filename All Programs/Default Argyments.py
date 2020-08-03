#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def func():
    q=int(input(""))
    list2=[]
    for i in range(0,q):
        c=input("")
        x,y=map(str,c.split())
        y=int(y)
        if x=="odd":
            x1=1
            for j in range(0,y):
                list2.append(x1)
                x1=x1+2
        else:
            x2=0
            for j in range(0,y):
                list2.append(x2)
                x2=x2+2
    print(*list2,sep='\n')
func()

