def func():
    s,t=map(int,input().split())
    a,b=map(int,input().split())
    m,n=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    c=0
    d=0
    for i in range(len(list1)):
        if list1[i]+a>=s and list1[i]+a<=t:
            c+=1
    for i in range(len(list2)):
        if list2[i]+b>=s and list2[i]+b<=t:
            d+=1
    print(c)
    print(d)
func()
