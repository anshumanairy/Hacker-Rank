#!/usr/bin/env python
# coding: utf-8

# In[46]:


def func():
    T=int(input())
    list2=list('hackerrank')
    list3=[]
    for i in range(T):
        list1=list(input())
        k=0
        for j in range(0,len(list1)):
            if list1[j]==list2[k]:
                k+=1
            if k==len(list2):
                break
        if k==len(list2):
            list3.append("YES")
        else:
            list3.append("NO")
    print(*list3,sep='\n')
func()


# In[22]:



def func():
    q=int(input())
    p='hackerrank'
    m=[]
    for i in range(q):
        s=input()
        for i,j in zip(range(len(p)),range(len(s))):
            if(p[i]==s[j]):
                pass
            else:
                i=i-1
                if(j==len(s)):
                    break
        if(j==len(s)and i<len(p)):
            m.append("NO")
        else:
            m.append("YES")
    print(*m,sep='\n')
func()


# In[ ]:




