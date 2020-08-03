def func():
    n,k=map(int,input().split())
    list1=list(map(int,input().split()))
    c=max(list1)
    if c-k<0:
        print(0)
    else:
        print(c-k)
func()
