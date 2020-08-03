def func():
    b,n,m=map(int,input().split())
    k=list(map(int,input().split()))
    d=list(map(int,input().split()))
    list1=[]
    x=0
    for i in range(len(k)):
        for j in range(len(d)):
            r=k[i]+d[j]
            if r<=b:
                x+=1
                list1.append(r)
    if x==0:
        print(-1)
    else:
        print(max(list1))
func()
