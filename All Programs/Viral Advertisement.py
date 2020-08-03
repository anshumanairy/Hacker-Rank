def func():
    n=int(input())
    a=5
    b=2
    c=2
    for i in range(2,n+1):
        a=(a//2)*3
        b=a//2
        c+=b
    print(c)
func()
