def func():
    i,j,k=map(int,input().split())
    list1=list(range(i,j+1))
    j=0
    for i in list1:
        if abs(i - int((str(i))[::-1]))%k==0:
            j+=1
    print(j)
func()
