#!/usr/bin/env python
# coding: utf-8

# In[19]:


import math
import datetime
def func():
    T=int(input())
    list1=[]
    for i in range(T):
        sec=0
        d1,day1,month1,year1,time1,zone1=map(str,input().split())
        d2,day2,month2,year2,time2,zone2=map(str,input().split())
        year1=int(year1)
        year2=int(year2)
        day1=int(day1)
        day2=int(day2)
        #time zone difference
        z=abs(int(zone1)-int(zone2))
        sec=sec-((int(z)%100)*60+int((int(z)/100))*60*60)
        #time difference
        h1,m1,s1=map(int,time1.split(':'))
        h2,m2,s2=map(int,time2.split(':'))
        sec=sec+abs(h1-h2)*60*60+abs(m1-m2)*60+abs(s1-s2)
        #Year difference
        sec=sec+abs(year1-year2)*365*24*60*60+abs(day1-day2)*24*60*60
        list1.append((abs(int(sec))))
    print(*list1,sep='\n')
func()


# In[ ]:


from datetime import datetime as dt
#correct answer

fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - 
                   dt.strptime(input(), fmt)).total_seconds())))

