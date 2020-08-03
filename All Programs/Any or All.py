#!/usr/bin/env python
# coding: utf-8

# In[5]:


def palindrome(j):
    d=str(j)
    if (d[::-1]==d):
        return True
    else:
        return False
def func():
    n=int(input())
    list1=list(map(int,input().split()))
    if all(i > 0 for i in list1):
        if any(palindrome(j)==True for j in list1):
            print("True")
        else:
            print("False")
    else:
        print("False")
func()


# In[ ]:




