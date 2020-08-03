def func():
    n=int(input())
    list1=list(input())
    d=0
    c=0
    for i in range(len(list1)):
        if list1[i]=='U':
            c+=1
        if list1[i]=='D':
            c-=1
        if c==0:
            if list1[i]=='U':
                d+=1
    print(d)
func()
