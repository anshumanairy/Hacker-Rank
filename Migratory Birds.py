def func():
    n=int(input())
    list1=list(map(int,input().split()))
    list2=list(set(list1))
    list3=[]
    for i in range(len(list2)):
        list3.append(list1.count(list2[i]))
    c=max(list3)
    d=list3.count(c)
    if d==1:
        print(list2[list3.index(c)])
    else:
        for i in range(len(list3)):
            if list3[i]==c:
                print(list2[i])
                break
func()
