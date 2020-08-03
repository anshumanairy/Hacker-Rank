#!/usr/bin/env python
# coding: utf-8

# In[16]:


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def func():
    list1=[]
    N=int(input())
    for i in range(2,round(N/2)):
        if N%i==0:
            if isPrime(i)==True:
                list1.append(i)
    list2=[]
    for i in range(len(list1)):
        for j in range(i,len(list1)):
            list2.append(list1[i]*list1[j])
    c=0
    for i in range(len(list2)):
        if N%list2[i]==0:
            c+=1
    if c>0:
        print("Yes")
    else:
        print("No")
func()


# In[29]:


import math
def factors(n):
    bool = False
    for i in range(2, n):
        if n % i == 0:
            a = i
            b = int(n / a)
            if prime_number(a) and prime_number(b):
                bool = True
                break
    return bool


def prime_number(m):
    prime = True
    for i in range(3, m):
        if m % i == 0:
            prime = False
            break
    return prime


if __name__ == '__main__':
    num = int(input())
    z = math.ceil(num/2)
    a = "No"
    for i in range(1, z):
        x = i
        y = num - i
        if factors(x) and factors(y):
            a = "Yes"
            break
print(a)


# In[ ]:


MAX = 10000
arr = []
sprime = [False] * (MAX)
def computeSemiPrime():
    for i in range(2, MAX):
        cnt, num, j = 0, i, 2
        while cnt < 2 and j * j <= num:
            while num % j == 0:
                num /= j 
                cnt += 1
                j += 1 
        if num > 1:
            cnt += 1
        if cnt == 2:
            sprime[i] = True
            arr.append(i)

def checkSemiPrime(n):
    i = 0
    while arr[i] <= n // 2:
        if sprime[n - arr[i]] == True:
            return True
        i+=1
    return False

if __name__ == "__main__": 
    computeSemiPrime()
    n=int(input())
    if checkSemiPrime(n) == True:
        print("Yes") 
    else:
        print("No")


# In[ ]:




