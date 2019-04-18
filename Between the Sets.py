from math import gcd
def func():
    m,n=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    list3=[]
    lcm=list1[0]
    for i in range(1,len(list1)):
        lcm=lcm*list1[i]//gcd(lcm,list1[i])
    i=lcm
    if i<=min(list2)//2:
        while i<=min(list2)//2:
            list3.append(i)
            i+=lcm
        list3.append(min(list2))
        x=0
        for i in list3:
            k=0
            for j in range(len(list2)):
                if list2[j]%i!=0:
                    k+=1
            if k==0:
                x+=1
        print(x)
    else:
        print(0)
func()
