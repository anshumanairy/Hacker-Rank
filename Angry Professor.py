def func():
    T=int(input())
    for i in range(T):
        n,k=map(int,input().split())
        list1=list(map(int,input().split()))
        j=0
        for i in list1:
            if i<=0:
                j+=1
        if j<k:
            print("YES")
        else:
            print("NO")
func()
