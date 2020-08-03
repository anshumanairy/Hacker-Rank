#!/usr/bin/env python
# coding: utf-8

# In[21]:


import math
def func(): 
    
    T=int(input())
    list1=[""]*T
    for i in range(0,T):
        n=int(input())
        list2=[]
        while n % 2 == 0: 
            list2.append(int(n))
            n = n / 2
            
        for j in range(3,int(math.sqrt(n))+1,2): 
                while n % j== 0: 
                    list2.append(j)
                    n = n / i  
        
        if n > 2: 
            list2.append(int(n))
        
        x=list2[len(list2)-1]
        list1[i]=x
    print(*list1,sep='\n')
func()


# In[ ]:




