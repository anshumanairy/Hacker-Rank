#!/usr/bin/env python
# coding: utf-8

# In[3]:


import calendar
def func():
    month,day,year=map(int,input().split())
    x=calendar.weekday(year, month, day)
    list1=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    print(list1[x])
func()


# In[ ]:




