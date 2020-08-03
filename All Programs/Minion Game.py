#!/usr/bin/env python
# coding: utf-8

# In[2]:


from itertools import permutations
def minion_game(s):
    c=0
    e=0
    for j in range(0,len(s)):
        list1=list(set(list(permutations(s,j+1))))
        for i in range(0,len(list1)):
            d=''.join(list1[i]) 
            if d in s:
                if (d[0]=='a' or d[0]=='e' or d[0]=='i' or d[0]=='o' or d[0]=='u' or d[0]=='A' or d[0]=='O' or d[0]=='E' or d[0]=='I' or d[0]=='U'):
                    e=e+(s.count(d))
                else:
                    c=c+(s.count(d))
    e=e+1
    if (c>e):
        print("Stuart",c)
    elif(e>c):
        print("Kevin",e)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[5]:


s =input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print ("Kevin", kevsc)
elif kevsc < stusc:
    print ("Stuart", stusc)
else:
    print("Draw")


# In[ ]:




