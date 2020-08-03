#!/usr/bin/env python
# coding: utf-8

# In[7]:


from itertools import permutations
def func():
    c=input("")
    list1=[]
    s,k=map(str,c.split())
    k=int(k)
    list1=list(permutations(s,k))
    list2=[""]*len(list1)
    for i in range(0,len(list1)):
        list2[i]=''.join(list1[i])
    list2.sort()
    print(*list2,sep='\n')
func()


# In[ ]:




