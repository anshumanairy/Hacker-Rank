n,k,q=map(int,input().split())
a =list(map(int,input().split()))
a = a[n-(k%n):n]+a[0:n-(k%n)]
for a0 in range(q):
    m = int(input().strip())
    print(a[m])
