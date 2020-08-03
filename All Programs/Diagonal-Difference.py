def func():
    n=int(input())
    list1=[]
    for i in range(n):
        list2=list(map(int,input().split()))
        list1.append(list2)
    a=0
    b=0
    for i in range(n):
        for j in range(n):
            if i==j:
                a=a+list1[i][j]
            if i+j==(n-1):
                b=b+list1[i][j]
    print(abs(a-b))
func()
