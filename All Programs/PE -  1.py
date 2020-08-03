#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func():
    T=int(input())
    list3=[""]*T
    for i in range(0,T):
        N=int(input())
        list1=[]
        a=3
        b=5
        while(a<N):
            list1.append(a)
            a=a+3
        while(b<N):
            list1.append(b)
            b=b+5
        list2=list(set(list1))
        list3[i]=sum(list2)
    print(*list3,sep='\n')
func()


# In[2]:


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        long t = sc.nextLong();
        for(long i=0;i<t;i++){
            long n = sc.nextLong();
            long a=0, b=0, d=0;
            a=(n-1)%3;
            a=n-1-a;
            a=a/3;
            b=(n-1)%5;
            b=n-1-b;
            b=b/5;
            d=(n-1)%15;
            d=n-1-d;
            d=d/15;
            long c= 3*a*(a+1)/2 + 5*b*(b+1)/2 - 15*d*(d+1)/2;
            System.out.println(c);
        }
    }
}


# In[ ]:




