#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
def simplePrimaryTest(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    i = 3
    sqrtOfNumber = math.sqrt(number)
    
    while i <= sqrtOfNumber:
        if number % i == 0:
            return False
        i = i+2
        
    return True  

def func():
    T=int(input())
    list1=[""]*T
    list3=[]
    for i in range(0,T):
        list1[i]=int(input())
    a=max(list1)
    list2=[]
    k=0
    l=1
    while(k<a):
        l=l+1
        if (simplePrimaryTest(l)==True):
            k=k+1
            list2.append(l)
    for r in range(0,T):
        list3.append(list2[list1[r]])
    print(*list1,sep='\n')
func()


# In[ ]:




