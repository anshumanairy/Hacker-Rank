def func():
    n,k=map(int,input().split())
    list1=list(map(int,input().split()))
    b=int(input())
    x=list1[k]
    s=0
    for i in range(len(list1)):
        if i!=k:
            s+=list1[i]
    s=s//2
    if (s!=b):
        s=b-s
        print(s)
    else:
        print('Bon Appetit')
func()
