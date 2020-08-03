#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N%2!=0:
        print("Weird")
    else:
        if (N>=2 and N<6):
            print("Not Weird")
        if (N>=6 and N<21):
            print("Weird")
        if (N>=21):
            print("Not Weird")

