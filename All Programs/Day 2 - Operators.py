#!/usr/bin/env python
# coding: utf-8

# In[7]:


def func():
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    total_cost=meal_cost+(meal_cost*tip_percent/100)+(meal_cost*tax_percent/100)
    print(round(total_cost))
func()


# In[ ]:




