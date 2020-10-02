from collections import OrderedDict

n=int(input())
k=OrderedDict()
d=[]
e=[]
for i in range(n):
    name=input()
    d.append(name)
    k[name]=k.get(name,0)+1
for k,v in k.items():
    e.append(v)
print(len(set(d)))
print(*e,sep=" ")


