def func():
    n=int(input())
    a=[]
    b=[]
    c=[]
    e=[]
    for i in range(0,n):
        f=input()
        a.append(f)
        g=float(input())
        b.append(g)
        c.append(g)
    c=list(set(c))
    c.sort()
    d=c[1]
    for j in range(0,n):
        if b[j]==d:
            e.append(a[j])
    e.sort()
    print(*e,sep='\n')
func()