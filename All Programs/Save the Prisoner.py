def func():
    T=int(input())
    for i in range(T):
        n,m,s=map(int,input().split())
        if (m+s-1)%n==0:
            print(n)
        else:
            print((m+s-1)%n)
func()
