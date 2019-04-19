def func():
    n,k=map(int,input().split())
    list1=list(map(int,input().split()))
    a=0
    for i in range(len(list1)):
        for j in range(len(list1)):
            if (i<j) and ((list1[i]+list1[j])%k==0):
                a+=1
    print(a)
func()
