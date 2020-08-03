def func():
    n=int(input())
    list1=list(map(int,input().split()))
    d,m=map(int,input().split())
    c=0
    for i in range(0,len(list1)-m+1):
        if sum(list1[i:m+i])==d:
            c+=1
    print(c)
func()
