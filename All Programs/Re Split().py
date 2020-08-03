#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
def func():
    s=input()
    list1=s.split(',')
    print(list1)
func()


# In[7]:


import re
print(*re.split("[,.]+", input()), sep="\n")

